# Examples

This directory contains example scripts demonstrating how to use the Design System Agent API.

## Available Examples

### 1. Dataset API Demo (`dataset_api_demo.py`)

Interactive demonstration of the dataset generation and search APIs.

**Features:**
- ✅ Health check to verify API is running
- 📊 Get dataset information and statistics
- 🚀 Generate new dataset with all 16 patterns
- 🔍 Search layouts using Vector RAG
- 💬 Process natural language queries

**Usage:**

1. **Start the API server first:**
   ```powershell
   # In project root
   .\start-dev.ps1
   ```

2. **Run the demo:**
   ```powershell
   # In project root
   python examples\dataset_api_demo.py
   ```

3. **Or run individual functions in Python:**
   ```python
   from examples.dataset_api_demo import *
   
   # Check dataset info
   get_dataset_info()
   
   # Generate dataset
   generate_dataset(total_records=2000, force_regenerate=False)
   
   # Search for layouts
   search_layouts("show lead dashboard", object_type="lead")
   
   # Process a query
   process_query("display case details with alerts")
   ```

## API Endpoints Demonstrated

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Check API health |
| `/api/v1/dataset/info` | GET | Get dataset statistics |
| `/api/v1/dataset/generate` | POST | Generate new dataset |
| `/api/v1/rag/search` | POST | Search similar layouts |
| `/api/v1/query` | POST | Process natural language query |

## Prerequisites

- API server must be running on `localhost:8000`
- Python packages: `requests`

Install dependencies:
```powershell
pip install requests
```

## Expected Output

The demo script will:

1. ✅ Verify API is running
2. 📊 Display current dataset statistics (if exists)
3. 🚀 Offer to generate dataset if missing
4. 🔍 Demonstrate RAG searches for different queries
5. 💬 Process example queries and show results

## API Documentation

For complete API documentation, see:
- [API_DOCUMENTATION.md](../API_DOCUMENTATION.md) - Complete endpoint reference
- http://localhost:8000/docs - Interactive Swagger UI
- http://localhost:8000/redoc - ReDoc documentation

## Troubleshooting

**Connection Error:**
```
❌ Cannot connect to API. Make sure the server is running.
```
**Solution:** Start the server with `.\start-dev.ps1`

**Dataset Not Found:**
```
ℹ️  Dataset does not exist yet
```
**Solution:** Run the demo script and choose 'y' when prompted to generate dataset

**Module Not Found:**
```
ModuleNotFoundError: No module named 'requests'
```
**Solution:** Install required packages: `pip install requests`

## Next Steps

After running the demo:

1. Explore the generated dataset in `dataset/crm_layouts.json`
2. Try the interactive API docs at http://localhost:8000/docs
3. Build your own client using the patterns in the demo script
4. Read [API_DOCUMENTATION.md](../API_DOCUMENTATION.md) for more endpoint details
