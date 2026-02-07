"""
Default Layout Builder
Creates a simple default layout when no RAG matches are found.
Contains: Heading, Description, Badge, List, Link
"""
from typing import Dict, Any, Optional, List


class DefaultLayoutBuilder:
    """
    Builds a simple default layout when no RAG matches are found.
    
    New Layout Structure:
    layout -> rows -> pattern_info (components)
    Each row has pattern_type and pattern_info containing primitive components
    """
    
    def build_default_layout(
        self,
        query: str,
        data: Optional[Dict[str, Any]] = None,
        analysis: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Build default layout with heading, description, badge, list, and link.
        Returns layout in new simplified format (layout -> rows -> pattern_info)
        
        Args:
            query: User's query
            data: Fetched data (optional)
            analysis: Query analysis (optional)
            
        Returns:
            Layout dictionary with simplified rows/pattern structure
        """
        # Extract information
        obj_type = self._extract_object_type(data, analysis)
        status = self._extract_status(data)
        items = self._extract_list_items(data)
        description_text = self._get_description_text(query, obj_type, data)
        
        # Build components for pattern_info
        components = [
            {
                "type": "Heading",
                "props": {"level": 1},
                "value": {
                    "icon": "",
                    "text": query or f"{obj_type.capitalize()} Information"
                }
            },
            {
                "type": "Description",
                "props": {},
                "value": {
                    "icon": "",
                    "text": description_text
                }
            },
            {
                "type": "Badge",
                "props": {"variant": self._get_badge_variant(status)},
                "value": {
                    "icon": "",
                    "text": status or "Active"
                }
            },
            {
                "type": "List",
                "props": {
                    "ordered": False,
                    "variant": "default",
                    "spacing": "medium",
                    "marker": "disc"
                },
                "value": {
                    "items": items or ["No items available"],
                    "additionalInfo": ""
                }
            },
            {
                "type": "Link",
                "props": {"href": f"/view-all-{obj_type}"},
                "value": {
                    "icon": "arrow-right",
                    "text": f"View All {obj_type.capitalize()}"
                }
            }
        ]
        
        # Return layout in new simplified format
        return {
            "id": "default_layout",
            "query": query,
            "object_type": obj_type,
            "layout_type": "default",
            "patterns_used": ["default"],
            "layout": {
                "query": query,
                "object_type": obj_type,
                "rows": [
                    {
                        "pattern_type": "default",
                        "pattern_info": components
                    }
                ]
            },
            "metadata": {
                "source": "default_builder",
                "auto_generated": True,
                "num_rows": 1,
                "num_components": len(components)
            },
            "score": 0.7
        }
    
    def _extract_object_type(self, data: Optional[Dict], analysis: Optional[Dict]) -> str:
        """Extract object type from data or analysis"""
        if data and "_meta" in data:
            obj_type = data["_meta"].get("object_type", "data")
            if obj_type:
                return obj_type
        
        # Fallback: detect from keywords
        keywords = ["lead", "account", "opportunity", "case", "task", "contact"]
        if analysis and "intent" in analysis:
            intent_str = str(analysis["intent"]).lower()
            for keyword in keywords:
                if keyword in intent_str:
                    return keyword
        
        return "data"
    
    def _extract_status(self, data: Optional[Dict]) -> str:
        """Extract status from data"""
        if not data:
            return "Active"
        
        fields = data.get("fields", {})
        return fields.get("status", "Active")
    
    def _extract_list_items(self, data: Optional[Dict]) -> List[str]:
        """Extract list items from data"""
        if not data:
            return ["No data available"]
        
        fields = data.get("fields", {})
        items = []
        
        # Extract key-value pairs
        for key, value in fields.items():
            if key not in ["id", "_id", "status"]:
                items.append(f"{key.replace('_', ' ').title()}: {value}")
        
        return items if items else ["No data available"]
    
    def _get_description_text(self, query: str, obj_type: str, data: Optional[Dict]) -> str:
        """Generate description text"""
        if data and "fields" in data:
            desc = data["fields"].get("description")
            if desc:
                return desc
        
        return f"Showing information for: {query}"
    
    def _get_badge_variant(self, status: str) -> str:
        """Get badge variant based on status"""
        status_lower = status.lower() if status else "active"
        
        if status_lower in ["active", "open", "new"]:
            return "success"
        elif status_lower in ["pending", "in progress"]:
            return "warning"
        elif status_lower in ["closed", "resolved", "completed"]:
            return "info"
        elif status_lower in ["inactive", "cancelled"]:
            return "secondary"
        else:
            return "primary"
