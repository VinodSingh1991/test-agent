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
    - Adapt to single or multi-entity data
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
        entities = self._detect_entities(data)
        view_type = self._detect_view_type(analysis)
        
        if len(entities) > 1:
            return self._build_multi_entity_fallback(query, data, entities)
        else:
            return self._build_single_entity_fallback(query, data, entities[0], view_type)
    
    def _detect_entities(self, data: Dict) -> List[str]:
        """Detect entities in data"""
        if "_entities" in data:
            return data["_entities"]
        
        entity_keys = ["account", "case", "lead", "task", "contact", "opportunity"]
        entities = []
        
        for key in entity_keys:
            if key in data or f"{key}_data" in data:
                entities.append(key)
        
        if not entities and "_meta" in data:
            entity_type = data["_meta"].get("entity_type")
            if entity_type:
                entities.append(entity_type)
        
        return entities if entities else ["unknown"]
    
    def _detect_view_type(self, analysis: Optional[Dict]) -> str:
        """Detect view type from analysis"""
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
    
    def _build_single_entity_fallback(
        self, query: str, data: Dict, entity: str, view_type: str
    ) -> Dict:
        """Build fallback for single entity"""
        components = []
        
        # 1. Title/Heading
        components.append({
            "type": "heading",
            "props": {
                "text": f"{entity.capitalize()} {view_type.capitalize()}",
                "level": 1,
                "className": "fallback-title"
            }
        })
        
        # 2. Description (if available)
        desc_text = self._extract_description(data)
        if desc_text:
            components.append({
                "type": "description",
                "props": {
                    "text": desc_text,
                    "className": "fallback-description"
                }
            })
        
        # 3. Status Badge (if available)
        status = self._extract_status(data)
        if status:
            components.append({
                "type": "badge",
                "props": {
                    "text": status,
                    "variant": self._status_variant(status),
                    "className": "fallback-badge"
                }
            })
        
        # 4. Field List
        list_items = self._extract_list_items(data)
        if list_items:
            components.append({
                "type": "list",
                "props": {
                    "items": list_items,
                    "className": "fallback-list"
                }
            })
        
        # 5. Action Buttons (generic)
        components.extend(self._build_generic_actions(entity))
        
        return {
            "id": f"fallback_{entity}_{view_type}",
            "pattern": "fallback_generic",
            "entity": entity,
            "view_type": view_type,
            "layout": "vertical_stack",
            "components": components,
            "metadata": {
                "source": "fallback",
                "query": query,
                "auto_generated": True
            }
        }
    
    def _build_multi_entity_fallback(
        self, query: str, data: Dict, entities: List[str]
    ) -> Dict:
        """Build fallback for multiple entities"""
        components = []
        
        # Overall title
        components.append({
            "type": "heading",
            "props": {
                "text": f"{' & '.join([e.capitalize() for e in entities])}",
                "level": 1,
                "className": "fallback-multi-title"
            }
        })
        
        # Section for each entity
        for entity in entities:
            entity_data = data.get(entity) or data.get(f"{entity}_data") or {}
            
            # Entity section header
            components.append({
                "type": "heading",
                "props": {
                    "text": entity.capitalize(),
                    "level": 2,
                    "className": f"fallback-section-{entity}"
                }
            })
            
            # Status badge
            status = self._extract_status(entity_data)
            if status:
                components.append({
                    "type": "badge",
                    "props": {
                        "text": status,
                        "variant": self._status_variant(status)
                    }
                })
            
            # Field list
            list_items = self._extract_list_items(entity_data)
            if list_items:
                components.append({
                    "type": "list",
                    "props": {
                        "items": list_items[:5],  # Limit per entity
                        "className": f"fallback-list-{entity}"
                    }
                })
        
        return {
            "id": f"fallback_multi_{'_'.join(entities)}",
            "pattern": "fallback_multi_entity",
            "entity": entities[0],  # Primary entity
            "view_type": "combined",
            "layout": "vertical_stack",
            "components": components,
            "metadata": {
                "source": "fallback",
                "query": query,
                "entities": entities,
                "auto_generated": True
            }
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
