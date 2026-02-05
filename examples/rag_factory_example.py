"""
Example: Using Factory-Generated JSONL for RAG Training

This example demonstrates how to use ComponentFactory-generated JSONL
for training a RAG system that can answer "How do I create X?" questions.
"""

import json
from pathlib import Path
from design_system_agent.core.component_factory import ComponentFactory


# ============================================================================
# STEP 1: Generate Training Data
# ============================================================================

def create_training_dataset():
    """Create a comprehensive training dataset using ComponentFactory"""
    
    examples = []
    
    # Button variations
    button_queries = [
        ("How do I create a primary button?", "primary"),
        ("Make a success button", "success"),
        ("Create a danger button for delete", "danger"),
        ("Build an outline style button", "outline"),
    ]
    
    for query, variant in button_queries:
        examples.append({
            "question": query,
            "answer": f"ComponentFactory.create_button(text='Button', variant='{variant}')",
            "component": ComponentFactory.create_button(text='Button', variant=variant)
        })
    
    # Input variations
    input_queries = [
        ("How to create an email input?", "email"),
        ("Make a password field", "password"),
        ("Create a search box", "search"),
    ]
    
    for query, input_type in input_queries:
        examples.append({
            "question": query,
            "answer": f"ComponentFactory.create_input(input_type='{input_type}', placeholder='Enter {input_type}')",
            "component": ComponentFactory.create_input(input_type=input_type, placeholder=f'Enter {input_type}')
        })
    
    # Layout examples
    examples.append({
        "question": "How do I create a 3-column grid?",
        "answer": "ComponentFactory.create_grid(children=[...], columns='3', gap='16')",
        "component": ComponentFactory.create_grid(
            children=[
                {"type": "div", "children": "Column 1"},
                {"type": "div", "children": "Column 2"},
                {"type": "div", "children": "Column 3"}
            ],
            columns='3',
            gap='16'
        )
    })
    
    # Chart examples
    examples.append({
        "question": "Show sales data in a line chart",
        "answer": "ComponentFactory.create_chart(chart_type='line', data=[100, 150, 200], labels=['Jan', 'Feb', 'Mar'])",
        "component": ComponentFactory.create_chart(
            chart_type='line',
            data=[100, 150, 200],
            labels=['Jan', 'Feb', 'Mar'],
            title='Sales Trend'
        )
    })
    
    # Table example
    examples.append({
        "question": "Create a leads table",
        "answer": "ComponentFactory.create_table(columns=[...], data=[...], sortable=True)",
        "component": ComponentFactory.create_table(
            columns=[
                {"key": "name", "label": "Name", "sortable": True},
                {"key": "company", "label": "Company", "sortable": True}
            ],
            data=[
                {"id": "1", "name": "John Doe", "company": "Tech Corp"}
            ],
            sortable=True,
            pagination=True
        )
    })
    
    return examples


# ============================================================================
# STEP 2: Save to JSONL
# ============================================================================

def save_training_data(examples, output_path='design_system_agent/dataset/rag_training.jsonl'):
    """Save examples to JSONL for RAG training"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for example in examples:
            json_line = json.dumps(example, ensure_ascii=False)
            f.write(json_line + '\n')
    
    print(f"✅ Saved {len(examples)} training examples to {output_path}")
    return output_path


# ============================================================================
# STEP 3: Load Training Data for RAG
# ============================================================================

def load_training_examples(file_path):
    """Load JSONL training data for RAG system"""
    examples = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                example = json.loads(line)
                examples.append(example)
            except json.JSONDecodeError:
                continue
    
    return examples


# ============================================================================
# STEP 4: Simple RAG Query Matching
# ============================================================================

def find_matching_example(query, examples, threshold=0.3):
    """
    Simple keyword-based matching (replace with vector search in production)
    
    Args:
        query: User query like "create a button"
        examples: List of training examples
        threshold: Minimum similarity score
        
    Returns:
        Best matching example or None
    """
    query_lower = query.lower()
    query_words = set(query_lower.split())
    
    best_match = None
    best_score = 0
    
    for example in examples:
        question = example.get('question', '').lower()
        question_words = set(question.split())
        
        # Calculate simple word overlap score
        common_words = query_words & question_words
        score = len(common_words) / max(len(query_words), 1)
        
        if score > best_score:
            best_score = score
            best_match = example
    
    if best_score >= threshold:
        return best_match, best_score
    
    return None, 0


# ============================================================================
# STEP 5: RAG-Powered Q&A System
# ============================================================================

def answer_question(query, training_file='design_system_agent/dataset/rag_training.jsonl'):
    """
    Answer user question using RAG system
    
    Args:
        query: User question like "How do I create a primary button?"
        training_file: Path to JSONL training data
        
    Returns:
        Dict with answer and component JSON
    """
    # Load training data
    examples = load_training_examples(training_file)
    
    # Find matching example
    match, score = find_matching_example(query, examples)
    
    if match:
        return {
            "question": query,
            "answer": match.get('answer'),
            "component": match.get('component'),
            "confidence": score,
            "source": "RAG"
        }
    else:
        return {
            "question": query,
            "answer": "No matching example found. Try being more specific.",
            "component": None,
            "confidence": 0,
            "source": "fallback"
        }


# ============================================================================
# STEP 6: Example Usage
# ============================================================================

def main():
    """Demonstrate RAG system with factory-generated training data"""
    
    print("🤖 Factory-Powered RAG System Demo\n")
    print("=" * 60)
    
    # Generate and save training data
    print("\n📚 Step 1: Generate training data...")
    examples = create_training_dataset()
    training_file = save_training_data(examples)
    
    # Test queries
    test_queries = [
        "How do I create a primary button?",
        "Make a danger button",
        "Create an email input field",
        "Show me a line chart",
        "Build a 3-column grid",
        "How to make a table?",
    ]
    
    print("\n🔍 Step 2: Test RAG system with queries...\n")
    
    for query in test_queries:
        print(f"\n{'='*60}")
        print(f"❓ Query: {query}")
        
        result = answer_question(query, training_file)
        
        print(f"✅ Confidence: {result['confidence']:.2%}")
        print(f"💡 Answer: {result['answer']}")
        
        if result['component']:
            print(f"🔧 Component Type: {result['component'].get('type')}")
            print(f"📦 Component JSON:")
            print(json.dumps(result['component'], indent=2))
    
    print(f"\n{'='*60}")
    print("\n✨ RAG System Demo Complete!")
    
    # Show statistics
    print(f"\n📊 Training Dataset Statistics:")
    print(f"  - Total examples: {len(examples)}")
    
    component_types = {}
    for ex in examples:
        comp_type = ex['component'].get('type', 'unknown')
        component_types[comp_type] = component_types.get(comp_type, 0) + 1
    
    print(f"  - Component types:")
    for comp_type, count in component_types.items():
        print(f"    • {comp_type}: {count}")


# ============================================================================
# STEP 7: Production Integration
# ============================================================================

def integrate_with_api():
    """
    Example: How to integrate with FastAPI endpoint
    
    In your design_system_agent/api/main.py:
    """
    
    code_example = '''
from fastapi import FastAPI
from design_system_agent.core.component_factory import ComponentFactory
import json

app = FastAPI()

# Load training data on startup
with open('design_system_agent/dataset/factory_usage.jsonl', 'r') as f:
    TRAINING_EXAMPLES = [json.loads(line) for line in f]

@app.post("/api/generate-component")
async def generate_component(query: str):
    """Generate component from natural language query"""
    
    # Find matching example using RAG
    match, score = find_matching_example(query, TRAINING_EXAMPLES)
    
    if match and score > 0.5:
        return {
            "success": True,
            "component": match['component'],
            "factory_method": match['answer'],
            "confidence": score
        }
    
    # Fallback: Try to infer component type from query
    if 'button' in query.lower():
        component = ComponentFactory.create_button(text='Click Me', variant='primary')
        return {"success": True, "component": component}
    
    return {"success": False, "error": "Could not generate component"}
    '''
    
    return code_example


if __name__ == '__main__':
    main()
    
    print("\n\n📝 Integration Example:")
    print(integrate_with_api())
