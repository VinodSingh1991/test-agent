"""
Example script demonstrating dataset generation API usage
"""
import requests
import json
from time import sleep

# API Base URL
BASE_URL = "http://localhost:8000/api/v1"


def check_health():
    """Check if API is running"""
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ API is running")
            return True
        else:
            print("❌ API is not responding correctly")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running.")
        print("   Start server with: .\\start-dev.ps1")
        return False


def get_dataset_info():
    """Get current dataset information"""
    print("\n" + "="*60)
    print("📊 Getting Dataset Info")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/dataset/info")
    
    if response.status_code == 200:
        data = response.json()
        
        if data["exists"]:
            print(f"✅ Dataset exists")
            print(f"   Total Records: {data['total_records']}")
            print(f"   Patterns: {len(data['patterns'])} patterns")
            print(f"   Object Types: {', '.join(data['object_types'])}")
            print(f"\n   Pattern Distribution:")
            for pattern, count in sorted(data['pattern_counts'].items()):
                print(f"      {pattern}: {count} records")
            print(f"\n   Object Type Distribution:")
            for obj_type, count in sorted(data['object_type_counts'].items()):
                print(f"      {obj_type}: {count} records")
            print(f"\n   File Sizes:")
            print(f"      JSON: {data['files']['json']['size_mb']} MB")
            print(f"      JSONL: {data['files']['jsonl']['size_mb']} MB")
        else:
            print("ℹ️  Dataset does not exist yet")
            print("   Generate it using the generate_dataset() function")
        
        return data
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"   {response.json()}")
        return None


def generate_dataset(total_records=2000, force_regenerate=False):
    """Generate new dataset"""
    print("\n" + "="*60)
    print("🚀 Generating Dataset")
    print("="*60)
    print(f"   Total Records: {total_records}")
    print(f"   Force Regenerate: {force_regenerate}")
    print("\n⏳ This may take a few minutes...")
    
    payload = {
        "total_records": total_records,
        "force_regenerate": force_regenerate
    }
    
    response = requests.post(
        f"{BASE_URL}/dataset/generate",
        json=payload
    )
    
    if response.status_code == 200:
        data = response.json()
        
        if data["status"] == "success":
            print(f"\n✅ Dataset generated successfully!")
            print(f"   Total Records: {data['total_records']}")
            print(f"   Patterns Used: {len(data['patterns_used'])} patterns")
            print(f"   Object Types: {', '.join(data['object_types'])}")
            print(f"\n   Files:")
            print(f"      JSON: {data['json_path']}")
            print(f"      JSONL: {data['jsonl_path']}")
        elif data["status"] == "exists":
            print(f"\nℹ️  {data['message']}")
            print(f"   Total Records: {data['total_records']}")
            print(f"   Use force_regenerate=True to regenerate")
        
        return data
    else:
        print(f"\n❌ Error: {response.status_code}")
        print(f"   {response.json()}")
        return None


def search_layouts(query, object_type=None, top_k=5):
    """Search for similar layouts using RAG"""
    print("\n" + "="*60)
    print("🔍 Searching Layouts")
    print("="*60)
    print(f"   Query: {query}")
    print(f"   Object Type: {object_type or 'Any'}")
    
    payload = {
        "query": query,
        "object_type": object_type,
        "top_k": top_k,
        "rerank": True,
        "final_k": 3
    }
    
    response = requests.post(
        f"{BASE_URL}/rag/search",
        json=payload
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ Found {data['total_results']} results:")
        
        for i, result in enumerate(data['results'], 1):
            print(f"\n   Result #{i}:")
            print(f"      Query: {result.get('query', 'N/A')}")
            print(f"      Object: {result.get('object_type', 'N/A')}")
            print(f"      Layout Type: {result.get('layout_type', 'N/A')}")
            print(f"      Pattern: {result.get('patterns_used', ['N/A'])[0]}")
            print(f"      Score: {result.get('score', 0):.4f}")
        
        return data
    else:
        print(f"\n❌ Error: {response.status_code}")
        print(f"   {response.json()}")
        return None


def process_query(query):
    """Process a natural language query"""
    print("\n" + "="*60)
    print("💬 Processing Query")
    print("="*60)
    print(f"   Query: {query}")
    
    payload = {
        "query": query,
        "format": "json"
    }
    
    response = requests.post(
        f"{BASE_URL}/query",
        json=payload
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ Query processed successfully!")
        print(f"   Object Type: {data.get('object_type', 'N/A')}")
        print(f"   Layout Type: {data.get('layout_type', 'N/A')}")
        print(f"   Layout has {len(data.get('layout', {}).get('rows', []))} rows")
        
        return data
    else:
        print(f"\n❌ Error: {response.status_code}")
        print(f"   {response.json()}")
        return None


def main():
    """Main demonstration flow"""
    print("\n" + "="*80)
    print(" "*20 + "🎨 Design System Agent - Dataset API Demo")
    print("="*80)
    
    # Check if API is running
    if not check_health():
        return
    
    # Get current dataset info
    info = get_dataset_info()
    
    # If dataset doesn't exist, generate it
    if info and not info.get("exists"):
        print("\n🔧 Dataset not found. Would you like to generate it?")
        print("   This will create ~2000 layout examples using all 16 patterns.")
        user_input = input("\n   Generate dataset? (y/n): ").strip().lower()
        
        if user_input == 'y':
            generate_dataset(total_records=2000, force_regenerate=False)
            print("\n⏳ Waiting for index to be rebuilt...")
            sleep(2)
            get_dataset_info()
    
    # Demonstrate RAG search
    if info and info.get("exists"):
        print("\n" + "="*80)
        print("🔍 Demonstrating RAG Search")
        print("="*80)
        
        search_examples = [
            ("show lead dashboard with metrics", "lead"),
            ("display case details", "case"),
            ("account list view", "account")
        ]
        
        for query, obj_type in search_examples:
            search_layouts(query, obj_type, top_k=3)
            sleep(1)
    
    # Demonstrate query processing
    print("\n" + "="*80)
    print("💬 Demonstrating Query Processing")
    print("="*80)
    
    query_examples = [
        "show my lead metrics",
        "display case with urgent alerts",
        "list all contacts"
    ]
    
    for query in query_examples:
        process_query(query)
        sleep(1)
    
    print("\n" + "="*80)
    print(" "*30 + "✅ Demo Complete!")
    print("="*80)
    print("\nFor more information, check API_DOCUMENTATION.md")
    print("API Docs: http://localhost:8000/docs")


if __name__ == "__main__":
    main()
