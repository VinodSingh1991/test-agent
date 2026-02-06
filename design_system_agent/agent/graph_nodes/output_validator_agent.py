"""
Output Validator Agent
Specialized agent for validating generated layouts
"""
from typing import Dict, Optional
from pydantic import BaseModel, Field


class ValidationResult(BaseModel):
    """Result from output validation"""
    is_valid: bool = Field(description="Whether output is valid")
    validation_score: float = Field(description="Validation score 0-1")
    issues: list = Field(default_factory=list, description="List of issues found")
    warnings: list = Field(default_factory=list, description="List of warnings")
    metadata: Dict = Field(default_factory=dict, description="Additional metadata")


class OutputValidatorAgent:
    """
    Agent responsible for validating the final layout output.
    Ensures structure integrity and completeness.
    """
    
    def validate_output(
        self,
        layout: Dict,
        query: str,
        analysis: Optional[Dict] = None
    ) -> ValidationResult:
        """
        Validate the generated layout output.
        
        Args:
            layout: The filled layout to validate
            query: Original user query
            analysis: Query analysis
            
        Returns:
            ValidationResult with validation status and details
        """
        
        issues = []
        warnings = []
        
        # Check required fields (only id, layout, score, query)
        required_fields = ["id", "layout"]
        for field in required_fields:
            if field not in layout or not layout.get(field):
                issues.append(f"Missing required field: {field}")
        
        # Validate layout structure
        layout_structure = layout.get("layout", {})
        if not layout_structure:
            issues.append("Layout structure is empty")
        elif "Tabs" in layout_structure:
            # Validate Tabs→Sections→Rows→Cols hierarchy
            tabs = layout_structure.get("Tabs", [])
            if not tabs:
                warnings.append("Layout has Tabs structure but no tabs defined")
            else:
                for tab_idx, tab in enumerate(tabs):
                    if "TabName" not in tab:
                        warnings.append(f"Tab {tab_idx} missing TabName")
                    if "Sections" not in tab or not tab.get("Sections"):
                        warnings.append(f"Tab {tab_idx} has no sections")
        
        # Calculate validation score
        validation_score = self._calculate_score(layout, issues, warnings)
        
        # Determine if valid
        is_valid = len(issues) == 0 and validation_score >= 0.5
        
        return ValidationResult(
            is_valid=is_valid,
            validation_score=validation_score,
            issues=issues,
            warnings=warnings,
            metadata={
                "layout_id": layout.get("id"),
                "has_tabs_structure": "Tabs" in layout_structure
            }
        )
    
    def _calculate_score(
        self, layout: Dict, issues: list, warnings: list
    ) -> float:
        """Calculate validation score"""
        
        base_score = 1.0
        
        # Deduct for issues
        base_score -= len(issues) * 0.2
        
        # Deduct for warnings
        base_score -= len(warnings) * 0.1
        
        # Bonus for complete Tabs structure
        if "Tabs" in layout.get("layout", {}):
            base_score += 0.1
        
        # Clamp between 0 and 1
        return max(0.0, min(1.0, base_score))
    
    def create_validated_output(
        self,
        layout: Dict,
        validation: ValidationResult,
        data: Optional[Dict] = None
    ) -> Dict:
        """
        Create final validated output structure.
        
        Args:
            layout: The validated layout
            validation: Validation result
            data: Optional data that was used
            
        Returns:
            Final output structure
        """
        
        return {
            "success": validation.is_valid,
            "layout": layout,
            "data": data,
            "score": validation.validation_score,
            "validation": {
                "is_valid": validation.is_valid,
                "score": validation.validation_score,
                "issues": validation.issues,
                "warnings": validation.warnings
            }
        }
