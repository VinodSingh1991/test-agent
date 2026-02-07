"""
Quick test script for dataset generation API
Use this for quick validation or automated testing
"""
import requests
import sys


def test_dataset_generation():
    """Test dataset generation endpoint"""
    base_url = "http://localhost:8000/api/v1"
    
    print("Testing Dataset Generation API...")
    print("-" * 50)
    
    # Test 1: Get dataset info
    print("\n1. Testing GET /dataset/info")
    try:
        response = requests.get(f"{base_url}/dataset/info", timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Dataset exists: {data.get('exists', False)}")
            if data.get('exists'):
                print(f"   Total records: {data.get('total_records', 0)}")
        print("   ✅ PASS")
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    # Test 2: Generate dataset (without force)
    print("\n2. Testing POST /dataset/generate (no force)")
    try:
        payload = {"total_records": 100, "force_regenerate": False}
        response = requests.post(f"{base_url}/dataset/generate", json=payload, timeout=300)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Status: {data.get('status')}")
            print(f"   Message: {data.get('message')}")
            print(f"   Total records: {data.get('total_records')}")
        print("   ✅ PASS")
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    # Test 3: Verify dataset exists after generation
    print("\n3. Testing dataset exists after generation")
    try:
        response = requests.get(f"{base_url}/dataset/info", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('exists'):
                print(f"   Dataset exists: True")
                print(f"   Total records: {data.get('total_records')}")
                print(f"   Patterns: {len(data.get('patterns', []))}")
                print(f"   Object types: {len(data.get('object_types', []))}")
                print("   ✅ PASS")
            else:
                print("   ❌ FAIL: Dataset should exist after generation")
                return False
        else:
            print(f"   ❌ FAIL: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    return True


def test_rag_endpoints():
    """Test RAG-related endpoints"""
    base_url = "http://localhost:8000/api/v1"
    
    print("\n\nTesting RAG Endpoints...")
    print("-" * 50)
    
    # Test 1: RAG stats
    print("\n1. Testing GET /rag/stats")
    try:
        response = requests.get(f"{base_url}/rag/stats", timeout=30)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Total indexed: {data.get('total_indexed_layouts', 0)}")
            print(f"   Embedding model: {data.get('embedding_model')}")
        print("   ✅ PASS")
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    # Test 2: RAG search
    print("\n2. Testing POST /rag/search")
    try:
        payload = {
            "query": "show lead dashboard",
            "object_type": "lead",
            "top_k": 5,
            "rerank": True,
            "final_k": 3
        }
        response = requests.post(f"{base_url}/rag/search", json=payload, timeout=30)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Results found: {data.get('total_results', 0)}")
        print("   ✅ PASS")
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    return True


def test_query_endpoint():
    """Test query processing endpoint"""
    base_url = "http://localhost:8000/api/v1"
    
    print("\n\nTesting Query Processing...")
    print("-" * 50)
    
    print("\n1. Testing POST /query")
    try:
        payload = {
            "query": "show lead metrics",
            "format": "json"
        }
        response = requests.post(f"{base_url}/query", json=payload, timeout=30)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Object type: {data.get('object_type')}")
            print(f"   Layout type: {data.get('layout_type')}")
            print(f"   Layout rows: {len(data.get('layout', {}).get('rows', []))}")
        print("   ✅ PASS")
    except Exception as e:
        print(f"   ❌ FAIL: {e}")
        return False
    
    return True


def main():
    """Run all tests"""
    print("=" * 50)
    print("  Dataset Generation API Test Suite")
    print("=" * 50)
    
    # Check API health
    print("\nChecking API health...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ API is running\n")
        else:
            print("❌ API returned unexpected status")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Cannot connect to API: {e}")
        print("\nMake sure the server is running:")
        print("  .\\start-dev.ps1")
        sys.exit(1)
    
    # Run tests
    all_passed = True
    
    if not test_dataset_generation():
        all_passed = False
    
    if not test_rag_endpoints():
        all_passed = False
    
    if not test_query_endpoint():
        all_passed = False
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("  ✅ ALL TESTS PASSED")
    else:
        print("  ❌ SOME TESTS FAILED")
    print("=" * 50)
    
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
