# Agent Architecture - Modular Design

## File Structure

```
design_system_agent/agent/
├── generator.py              # Main orchestrator (80 lines)
├── registry.py              # Component registry loader (120 lines)
├── template_engine.py       # Template rendering (40 lines)
├── dashboard_generator.py   # Dashboard specialist (100 lines)
├── page_generator.py        # Page specialist (150 lines)
├── form_generator.py        # Form specialist (50 lines)
├── rag_engine.py           # RAG & LLM integration
├── query_classifier.py     # Query understanding
├── component_mapper.py     # Component mapping
└── agent_controller.py     # Main workflow controller
```

## Separation of Concerns

### 1. **generator.py** (Main Orchestrator)
- Entry point for all generation
- Routes to specialized generators
- Delegates to registry and template engine
- **80 lines** (was 400+)

### 2. **registry.py** (Data Layer)
- Loads component definitions from JSON
- Manages 500+ components efficiently
- Provides search and lookup
- **120 lines**

### 3. **template_engine.py** (Rendering)
- String interpolation
- Import generation
- Boolean prop handling
- **40 lines**

### 4. **Specialized Generators**

#### **dashboard_generator.py**
- Dashboard-specific logic
- Widget composition
- Grid layouts
- **100 lines**

#### **page_generator.py**
- Page templates (login, profile, settings)
- Layout patterns
- Routing logic
- **150 lines**

#### **form_generator.py**
- Form field generation
- Validation patterns
- Submit handling
- **50 lines**

## Benefits of This Architecture

### ✅ **Maintainability**
- Each file has single responsibility
- Easy to locate and fix bugs
- Clear boundaries

### ✅ **Scalability**
- Add new generator types easily
- No need to modify existing code
- Open/Closed Principle

### ✅ **Testability**
- Test each component independently
- Mock dependencies easily
- Focused unit tests

### ✅ **Readability**
- ~50-150 lines per file (manageable)
- Clear naming conventions
- Self-documenting structure

### ✅ **Extensibility**
```python
# Add new generator in 3 steps:

# 1. Create specialized generator
from .template_engine import TemplateEngine

class ChartGenerator:
    def generate(self, spec):
        # Chart-specific logic
        pass

# 2. Import in generator.py
from .chart_generator import ChartGenerator

# 3. Route in ComponentGenerator
elif component_type == "chart":
    return self.chart_generator.generate(spec)
```

## Usage (No Changes Required)

```python
from design_system_agent.agent.generator import ComponentGenerator

generator = ComponentGenerator()

# Still works the same way
code = generator.generate_component({
    "type": "dashboard",
    "title": "Analytics"
})
```

## Adding New Generator Types

### Example: Chart Generator

**1. Create `chart_generator.py`:**
```python
class ChartGenerator:
    def generate(self, spec: dict) -> str:
        chart_type = spec.get("chart_type", "line")
        return f"// {chart_type} chart code"
```

**2. Update `generator.py`:**
```python
from .chart_generator import ChartGenerator

class ComponentGenerator:
    def __init__(self, ...):
        self.chart_generator = ChartGenerator()
    
    def generate_component(self, spec):
        if component_type == "chart":
            return self.chart_generator.generate(spec)
```

Done! ✨

## Testing Structure

```
tests/
├── test_registry.py           # Test component loading
├── test_template_engine.py    # Test rendering
├── test_dashboard_generator.py # Test dashboards
├── test_page_generator.py     # Test pages
├── test_form_generator.py     # Test forms
└── test_generator.py          # Integration tests
```

## File Size Comparison

| Before | After | Reduction |
|--------|-------|-----------|
| generator.py: 400+ lines | generator.py: 80 lines | **80% smaller** |
| - | registry.py: 120 lines | New |
| - | template_engine.py: 40 lines | New |
| - | dashboard_generator.py: 100 lines | New |
| - | page_generator.py: 150 lines | New |
| - | form_generator.py: 50 lines | New |
| **Total: 400+ lines** | **Total: 540 lines** | Better organized |

## Key Principles Applied

1. **Single Responsibility Principle**: Each class has one job
2. **Open/Closed Principle**: Open for extension, closed for modification
3. **Dependency Injection**: Generators receive dependencies
4. **Separation of Concerns**: Data, logic, and rendering separated
5. **Composition over Inheritance**: Use specialized generators

This architecture is production-ready and can scale to support any number of component types! 🚀
