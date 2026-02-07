"""
Setup Guide - Fix API Key and Data Issues

This script helps diagnose and fix common setup issues.
"""
import os
import sys

print("=" * 80)
print("DESIGN SYSTEM AGENT - SETUP DIAGNOSTIC")
print("=" * 80)

# Check 1: Python version
print("\n[CHECK 1] Python Version")
print("-" * 80)
python_version = sys.version.split()[0]
print(f"✓ Python version: {python_version}")
if python_version.startswith("3.14"):
    print("⚠️  WARNING: Python 3.14 has Pydantic v1 compatibility warnings (non-critical)")

# Check 2: OpenAI API Key
print("\n[CHECK 2] OpenAI API Key")
print("-" * 80)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    masked_key = api_key[:7] + "..." + api_key[-4:] if len(api_key) > 11 else "***"
    print(f"✅ OPENAI_API_KEY is set: {masked_key}")
else:
    print("❌ OPENAI_API_KEY is NOT set")
    print("\n💡 HOW TO FIX:")
    print("   1. Get your API key from: https://platform.openai.com/api-keys")
    print("   2. Set environment variable in PowerShell:")
    print("      $env:OPENAI_API_KEY = 'sk-proj-your-key-here'")
    print("   3. Verify it's set:")
    print("      echo $env:OPENAI_API_KEY")
    print("   4. Restart VS Code debug session")
    print("\n   Alternative: Create .env file in project root:")
    print("      OPENAI_API_KEY=sk-proj-your-key-here")

# Check 3: Model Selection
print("\n[CHECK 3] Model Selection")
print("-" * 80)
model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
print(f"✓ Using model: {model}")
if model == "gpt-4o-mini":
    print("⚠️  WARNING: gpt-4o-mini is deprecated. Upgrade to gpt-5-mini")
    print("   Set: $env:OPENAI_MODEL = 'gpt-5-mini'")
elif model in ["gpt-5-mini", "gpt-5-nano", "gpt-4.1-mini", "gpt-5.2"]:
    print(f"✅ Model '{model}' is up-to-date (2026)")
else:
    print(f"⚠️  Unknown model: {model}")
    print("   Recommended models: gpt-5-mini, gpt-5-nano, gpt-4.1-mini, gpt-5.2")

# Check 4: Test API Connection
print("\n[CHECK 4] Test API Connection")
print("-" * 80)
if api_key:
    try:
        from langchain_openai import ChatOpenAI
        
        print("Testing OpenAI API connection...")
        llm = ChatOpenAI(
            model=model,
            temperature=0,
            max_tokens=100,
            openai_api_key=api_key
        )
        
        response = llm.invoke("Say 'API works!'")
        print(f"✅ API connection successful!")
        print(f"   Response: {response.content[:50]}...")
        
    except Exception as e:
        print(f"❌ API connection failed: {str(e)}")
        print("\n💡 POSSIBLE CAUSES:")
        print("   - Invalid API key")
        print("   - Insufficient credits/quota")
        print("   - Network connectivity issues")
        print("   - Model not available on your plan")
else:
    print("⏭️  Skipped (no API key set)")

# Check 5: FAISS Vector Index
print("\n[CHECK 5] FAISS Vector Index")
print("-" * 80)
vector_index_path = "design_system_agent/vector_index/crm_layouts.faiss"
if os.path.exists(vector_index_path):
    print(f"✅ FAISS index found: {vector_index_path}")
else:
    print(f"⚠️  FAISS index not found: {vector_index_path}")
    print("   This is OK - system will create default layouts")

# Check 6: CRM Dataset
print("\n[CHECK 6] CRM Dataset")
print("-" * 80)
dataset_path = "design_system_agent/dataset/crm_layouts.json"
if os.path.exists(dataset_path):
    print(f"✅ CRM dataset found: {dataset_path}")
    import json
    with open(dataset_path, 'r') as f:
        data = json.load(f)
    print(f"   Layouts available: {len(data)}")
else:
    print(f"⚠️  CRM dataset not found: {dataset_path}")
    print("   This is OK - system will create default layouts")

# Summary and Next Steps
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

issues_found = []
if not api_key:
    issues_found.append("Missing OPENAI_API_KEY")
if model == "gpt-4o-mini":
    issues_found.append("Deprecated model (gpt-4o-mini)")

if issues_found:
    print(f"\n❌ {len(issues_found)} issue(s) found:")
    for i, issue in enumerate(issues_found, 1):
        print(f"   {i}. {issue}")
    
    print("\n📋 QUICK FIX (PowerShell):")
    print("=" * 80)
    if not api_key:
        print("# Set API key")
        print("$env:OPENAI_API_KEY = 'sk-proj-your-key-here'")
        print()
    if model == "gpt-4o-mini":
        print("# Upgrade to latest model")
        print("$env:OPENAI_MODEL = 'gpt-5-mini'")
        print()
    print("# Restart VS Code debug session")
    print("# Run query: 'show my top priority cases where status equal hot'")
else:
    print("\n✅ All checks passed! System is ready.")
    print("\n📋 NEXT STEPS:")
    print("=" * 80)
    print("1. Restart your debug session in VS Code")
    print("2. Run a test query:")
    print("   POST http://localhost:8000/generate-layout")
    print("   Body: {\"query\": \"show my top priority cases where status equal hot\"}")
    print("3. Check debug console for logs:")
    print("   - [LayoutSelectorAgent] ✓ Successfully received structured output")
    print("   - [LayoutSelectorAgent] ✓ Selected: <layout_id>, Confidence: 0.85+")
    print("4. Verify response contains valid layout JSON")

print("\n" + "=" * 80)
print("ADDITIONAL RESOURCES")
print("=" * 80)
print("- Model Guide: MODEL_SELECTION_GUIDE.md")
print("- API Docs: API_DOCUMENTATION.md")
print("- Design System Tools: DESIGN_SYSTEM_TOOLS_GUIDE.md")
print()
