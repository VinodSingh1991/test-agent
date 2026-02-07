"""
Fallback Layout Builder
Creates generic layouts when no good match found
"""
from typing import Dict, List, Any, Optional


class FallbackLayoutBuilder:
    """
    Builds fallback layouts when no suitable layout found.
    
    Responsibilities:
    - Create generic title + desc + list + badge layout
    - Adapt to single or multi-object data
    - Use design system components
    - Ensure usable UI even without perfect match
    """
    
    def build_fallback_layout(
        self,
        query: str,
        data: Dict[str, Any],
        analysis: Optional[Dict] = None
    ) -> Dict:
        """
        Build fallback layout for data.
        
        Args:
            query: User query
            data: Fetched data
            analysis: Query analysis
            
        Returns:
            Generic layout with standard components
        """
        objects = self._detect_objects(data)
        layout_type = self._detect_layout_type(analysis)
        
        if len(objects) > 1:
            return self._build_multi_object_fallback(query, data, objects)
        else:
            return self._build_single_object_fallback(query, data, objects[0], layout_type)
    
    def _detect_objects(self, data: Dict) -> List[str]:
        """Detect objects in data"""
        if "_objects" in data:
            return data["_objects"]
        
        object_keys = ["account", "case", "lead", "task", "contact", "opportunity"]
        objects = []
        
        for key in object_keys:
            if key in data or f"{key}_data" in data:
                objects.append(key)
        
        if not objects and "_meta" in data:
            object_type = data["_meta"].get("object_type")
            if object_type:
                objects.append(object_type)
        
        return objects if objects else ["unknown"]
    
    def _detect_layout_type(self, analysis: Optional[Dict]) -> str:
        """Detect layout type from analysis"""
        if not analysis:
            return "detail"
        
        intent = analysis.get("intent", "")
        # Ensure intent is a string
        if not isinstance(intent, str):
            intent = ""
        intent = intent.lower()
        
        if "list" in intent or "all" in intent or "show" in intent:
            return "list"
        elif "detail" in intent or "view" in intent or "info" in intent:
            return "detail"
        else:
            return "detail"
    
    def _build_single_object_fallback(
        self, query: str, data: Dict, obj_type: str, layout_type: str
    ) -> Dict:
        """Build fallback for single object using new rows/pattern structure"""
        components = []
        
        # 1. Title/Heading
        components.append({
            "type": "Heading",
            "props": {"level": 1},
            "value": {
                "icon": "",
                "text": f"{obj_type.capitalize()} {layout_type.capitalize()}"
            }
        })
        
        # 2. Description (if available)
        desc_text = self._extract_description(data)
        if desc_text:
            components.append({
                "type": "Description",
                "props": {},
                "value": {
                    "icon": "",
                    "text": desc_text
                }
            })
        
        # 3. Status Badge (if available)
        status = self._extract_status(data)
        if status:
            components.append({
                "type": "Badge",
                "props": {"variant": self._status_variant(status)},
                "value": {
                    "icon": "",
                    "text": status
                }
            })
        
        # 4. Field List
        list_items = self._extract_list_items(data)
        if list_items:
            components.append({
                "type": "List",
                "props": {
                    "ordered": False,
                    "variant": "default",
                    "spacing": "medium",
                    "marker": "disc"
                },
                "value": {
                    "items": list_items,
                    "additionalInfo": ""
                }
            })
        
        # Return in new simplified format with rows/pattern_info
        return {
            "id": f"fallback_{obj_type}_{layout_type}",
            "query": query,
            "object_type": obj_type,
            "layout_type": layout_type,
            "patterns_used": ["fallback"],
            "layout": {
                "query": query,
                "object_type": obj_type,
                "rows": [
                    {
                        "pattern_type": "fallback",
                        "pattern_info": components
                    }
                ]
            },
            "metadata": {
                "source": "fallback",
                "auto_generated": True,
                "num_rows": 1,
                "num_components": len(components)
            },
            "score": 0.6
        }
    
    def _build_multi_object_fallback(
        self, query: str, data: Dict, objects: List[str]
    ) -> Dict:
        """Build fallback for multiple objects using new rows/pattern structure"""
        all_components = []
        
        # Overall title
        all_components.append({
            "type": "Heading",
            "props": {"level": 1},
            "value": {
                "icon": "",
                "text": f"{' & '.join([o.capitalize() for o in objects])}"
            }
        })
        
        # Section for each object
        for obj_type in objects:
            obj_data = data.get(obj_type) or data.get(f"{obj_type}_data") or {}
            
            # Object section header
            all_components.append({
                "type": "Heading",
                "props": {"level": 2},
                "value": {
                    "icon": "",
                    "text": obj_type.capitalize()
                }
            })
            
            # Status badge
            status = self._extract_status(obj_data)
            if status:
                all_components.append({
                    "type": "Badge",
                    "props": {"variant": self._status_variant(status)},
                    "value": {
                        "icon": "",
                        "text": status
                    }
                })
            
            # Field list
            list_items = self._extract_list_items(obj_data)
            if list_items:
                all_components.append({
                    "type": "List",
                    "props": {
                        "ordered": False,
                        "variant": "default",
                        "spacing": "medium",
                        "marker": "disc"
                    },
                    "value": {
                        "items": list_items[:5],  # Limit per object
                        "additionalInfo": ""
                    }
                })
        
        # Return in new simplified format
        return {
            "id": f"fallback_multi_{'_'.join(objects)}",
            "query": query,
            "object_type": objects[0],  # Primary object
            "layout_type": "combined",
            "patterns_used": ["fallback_multi"],
            "layout": {
                "query": query,
                "object_type": objects[0],
                "rows": [
                    {
                        "pattern_type": "fallback_multi",
                        "pattern_info": all_components
                    }
                ]
            },
            "metadata": {
                "source": "fallback",
                "auto_generated": True,
                "multi_object": True,
                "objects": objects,
                "num_rows": 1,
                "num_components": len(all_components)
            },
            "score": 0.6
        }
    
    def _extract_description(self, data: Dict) -> Optional[str]:
        """Extract description from data"""
        fields = data.get("fields", {})
        return (
            fields.get("description") or
            fields.get("notes") or
            fields.get("summary") or
            None
        )
    
    def _extract_status(self, data: Dict) -> Optional[str]:
        """Extract status from data"""
        fields = data.get("fields", {})
        
        # Try to get status, stage, or priority
        for field_name in ["status", "stage", "priority"]:
            field_value = fields.get(field_name)
            if field_value:
                # If it's a dict (like {"value": "open", "display_value": "Open"}), extract value
                if isinstance(field_value, dict):
                    return field_value.get("value") or field_value.get("display_value")
                # If it's a string, return it
                elif isinstance(field_value, str):
                    return field_value
        
        return None
    
    def _status_variant(self, status: str) -> str:
        """Map status to badge variant"""
        # Ensure status is a string
        if not isinstance(status, str):
            status = str(status) if status is not None else "unknown"
        
        status_lower = status.lower()
        
        if status_lower in ["open", "active", "new", "in progress"]:
            return "success"
        elif status_lower in ["closed", "done", "completed", "resolved"]:
            return "default"
        elif status_lower in ["urgent", "high", "critical", "blocked"]:
            return "danger"
        elif status_lower in ["pending", "waiting", "on hold"]:
            return "warning"
        else:
            return "info"
    
    def _extract_list_items(self, data: Dict) -> List[Dict]:
        """Extract list items from data"""
        items = []
        
        fields = data.get("fields", {})
        metrics = data.get("metrics", {})
        
        # Add important fields
        skip_keys = ["id", "description", "notes", "summary", "status", "stage", "priority"]
        
        for key, value in fields.items():
            if key not in skip_keys and value is not None:
                items.append({
                    "label": key.replace("_", " ").title(),
                    "value": str(value)
                })
        
        # Add metrics
        for key, value in metrics.items():
            items.append({
                "label": key.replace("_", " ").title(),
                "value": str(value),
                "highlight": True
            })
        
        return items
    
    def _build_generic_actions(self, entity: str) -> List[Dict]:
        """Build generic action buttons"""
        return [
            {
                "type": "button",
                "props": {
                    "text": f"Edit {entity.capitalize()}",
                    "variant": "primary",
                    "action": f"edit_{entity}"
                }
            },
            {
                "type": "button",
                "props": {
                    "text": "View Details",
                    "variant": "secondary",
                    "action": f"view_{entity}_details"
                }
            }
        ]
