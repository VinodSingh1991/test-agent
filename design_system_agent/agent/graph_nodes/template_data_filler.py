"""
Simple Template Data Filler
Fills fixed templates with actual CRM data (without LLM)
"""
from typing import Dict, Any, List, Optional
import copy


def fill_template_with_data(template: Dict[str, Any], data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fill a fixed template with actual CRM data.
    
    Args:
        template: Layout template from layout_templates.py
        data: Fetched CRM data
        
    Returns:
        Layout with data filled in
    """
    if not data:
        print("[TemplateFiller] No data to fill, returning empty template")
        return template
    
    # Deep copy to avoid modifying original template
    filled = copy.deepcopy(template)
    
    # Extract metadata
    meta = data.get("_meta", {})
    object_type = meta.get("object_type", "unknown")
    record_count = meta.get("record_count", 0)
    
    # Check if list or detail data
    records = data.get("records", [])
    fields = data.get("fields", {})
    
    if not filled or "layout" not in filled or "rows" not in filled["layout"]:
        print("[TemplateFiller] Invalid template structure")
        return template
    
    rows = filled["layout"]["rows"]
    
    # Fill each row
    for row in rows:
        pattern_type = row.get("pattern_type", "")
        pattern_info = row.get("pattern_info", [])
        
        if pattern_type == "header":
            _fill_header(pattern_info, object_type, record_count, len(records))
        elif pattern_type == "description":
            _fill_description(pattern_info, object_type, fields)
        elif pattern_type == "data_list":
            _fill_data_list(pattern_info, records, fields, object_type)
        elif pattern_type == "content":
            _fill_content(pattern_info, records, fields)
    
    print(f"[TemplateFiller] ✓ Filled template with {record_count or len(records)} record(s)")
    return filled


def _fill_header(pattern_info: List[Dict], object_type: str, record_count: int, records_len: int):
    """Fill header components (Heading + Badge)"""
    for component in pattern_info:
        comp_type = component.get("type", "")
        
        if comp_type == "Heading":
            # Update heading text
            if "value" in component:
                current_text = component["value"].get("text", "")
                # Keep the text as is (e.g., "Leads", "Cases")
                print(f"[TemplateFiller]   Header: {current_text}")
        
        elif comp_type == "Badge":
            # Update badge with record count
            if "value" in component:
                count = record_count if record_count > 0 else records_len
                component["value"]["text"] = f"{count} record{'s' if count != 1 else ''}"
                print(f"[TemplateFiller]   Badge: {count} records")


def _fill_description(pattern_info: List[Dict], object_type: str, fields: Dict):
    """Fill description components"""
    for component in pattern_info:
        comp_type = component.get("type", "")
        
        if comp_type == "Text":
            if "value" in component:
                if fields:
                    # Show summary of available fields
                    field_names = list(fields.keys())[:5]
                    component["value"]["text"] = f"Viewing {object_type} data with fields: {', '.join(field_names)}..."
                else:
                    component["value"]["text"] = f"{object_type.capitalize()} information will be displayed here"


def _fill_data_list(pattern_info: List[Dict], records: List[Dict], fields: Dict, object_type: str):
    """Fill data list components"""
    for component in pattern_info:
        comp_type = component.get("type", "")
        
        if comp_type == "List":
            if "value" in component:
                if records:
                    # Fill with record data
                    items = []
                    for record in records:
                        # Create item from record fields
                        item_text = _format_record(record, object_type)
                        items.append(item_text)
                    
                    component["value"]["items"] = items
                    print(f"[TemplateFiller]   List: {len(items)} items")
                elif fields:
                    # Single record detail view
                    items = []
                    for key, value in fields.items():
                        if key not in ["id", "_id"]:
                            items.append(f"{key.replace('_', ' ').title()}: {value}")
                    component["value"]["items"] = items
                    print(f"[TemplateFiller]   List: {len(items)} fields")
                else:
                    component["value"]["items"] = []


def _fill_content(pattern_info: List[Dict], records: List[Dict], fields: Dict):
    """Fill content components"""
    for component in pattern_info:
        comp_type = component.get("type", "")
        
        if comp_type == "Text":
            if "value" in component:
                if records:
                    component["value"]["text"] = f"Found {len(records)} records matching your query"
                elif fields:
                    component["value"]["text"] = f"Displaying record details"
                else:
                    component["value"]["text"] = "No records found. Please check your query or data source."


def _format_record(record: Dict, object_type: str) -> str:
    """Format a single record for display"""
    # Define primary fields for each object type
    primary_fields = {
        "lead": ["name", "company", "email", "status"],
        "case": ["subject", "status", "priority", "customer"],
        "account": ["name", "industry", "revenue", "status"],
        "contact": ["name", "email", "title", "account"],
        "opportunity": ["name", "amount", "stage", "probability"],
        "task": ["subject", "status", "priority", "due_date"],
        "loan": ["borrower", "amount", "type", "status"],
        "policy": ["policy_number", "holder", "type", "status"]
    }
    
    fields_to_show = primary_fields.get(object_type, ["id", "name", "status"])
    
    parts = []
    for field in fields_to_show:
        if field in record and record[field]:
            value = record[field]
            parts.append(f"{field.replace('_', ' ').title()}: {value}")
    
    # If no fields matched, show all non-id fields
    if not parts:
        for key, value in record.items():
            if key not in ["id", "_id"] and value:
                parts.append(f"{key.replace('_', ' ').title()}: {value}")
    
    return " | ".join(parts) if parts else str(record)
