# Design System Agent API Documentation

## Overview
The Design System Agent API provides endpoints for generating UI layouts, searching patterns using RAG, and managing datasets for CRM applications.

**Base URL:** `http://localhost:8000`

---

## Endpoints

### 1. Process Query
**POST** `/query`

Processes a natural language query and generates a layout using the agent.

**Request Body:**
```json
{
  "query": "show lead details",
  "context": "optional context",
  "format": "json"
}
```

**Response:**
```json
{
  "layout": { /* Generated layout structure */ },
  "query": "show lead details",
  "object_type": "lead",
  "layout_type": "detail"
}
```

---

### 2. RAG Search
**POST** `/rag/search`

Search for similar CRM layouts using Vector RAG with reranking.

**Request Body:**
```json
{
  "query": "show lead dashboard",
  "object_type": "lead",
  "layout_type": "dashboard",
  "top_k": 10,
  "rerank": true,
  "final_k": 3
}
```

**Response:**
```json
{
  "query": "show lead dashboard",
  "results": [
    {
      "query": "show lead metrics",
      "object_type": "lead",
      "layout_type": "dashboard",
      "patterns_used": ["pattern0"],
      "layout": { /* Layout structure */ },
      "score": 0.95
    }
  ],
  "total_results": 3
}
```

---

### 3. RAG Statistics
**GET** `/rag/stats`

Get statistics about the RAG index.

**Response:**
```json
{
  "total_indexed_layouts": 1500,
  "index_path": "vector_index/crm_layouts.faiss",
  "metadata_path": "vector_index/crm_layouts_metadata.pkl",
  "embedding_model": "all-MiniLM-L6-v2",
  "embedding_dimension": 384,
  "reranker_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"
}
```

---

### 4. Rebuild RAG Index
**POST** `/rag/rebuild`

Rebuild the RAG index from scratch. This deletes existing index and creates a new one.

**Response:**
```json
{
  "status": "success",
  "message": "RAG index rebuilt successfully",
  "total_layouts_indexed": 1500,
  "index_path": "vector_index/crm_layouts.faiss"
}
```

---

### 5. Generate Dataset ⭐ NEW
**POST** `/dataset/generate`

Generate comprehensive CRM layouts dataset with all 16 patterns.

**Request Body:**
```json
{
  "total_records": 2000,
  "force_regenerate": false
}
```

**Parameters:**
- `total_records` (optional, default: 2000): Target number of records to generate
- `force_regenerate` (optional, default: false): Force regeneration even if dataset exists

**Response:**
```json
{
  "status": "success",
  "message": "Dataset generated successfully",
  "total_records": 1856,
  "jsonl_path": "dataset/crm_layouts.jsonl",
  "json_path": "dataset/crm_layouts.json",
  "patterns_used": [
    "pattern0", "pattern1", "pattern2", "pattern3", "pattern4",
    "pattern5", "pattern6", "pattern7", "pattern8", "pattern9",
    "pattern10", "pattern11", "pattern12", "pattern13", "pattern14", "pattern15"
  ],
  "object_types": [
    "account", "case", "contact", "lead", "opportunity"
  ]
}
```

**Status Values:**
- `success`: Dataset generated successfully
- `exists`: Dataset already exists (use `force_regenerate: true` to override)

---

### 6. Get Dataset Info ⭐ NEW
**GET** `/dataset/info`

Get detailed information about the current dataset.

**Response:**
```json
{
  "status": "success",
  "exists": true,
  "total_records": 1856,
  "patterns": [
    "pattern0", "pattern1", "pattern2", "pattern3", "pattern4",
    "pattern5", "pattern6", "pattern7", "pattern8", "pattern9",
    "pattern10", "pattern11", "pattern12", "pattern13", "pattern14", "pattern15"
  ],
  "pattern_counts": {
    "pattern0": 120,
    "pattern1": 115,
    "pattern2": 118,
    ...
  },
  "object_types": [
    "account", "case", "contact", "lead", "opportunity"
  ],
  "object_type_counts": {
    "lead": 425,
    "account": 380,
    "contact": 390,
    "case": 335,
    "opportunity": 326
  },
  "layout_types": [
    "dashboard", "detail", "list", "summary"
  ],
  "files": {
    "json": {
      "path": "dataset/crm_layouts.json",
      "size_bytes": 2458624,
      "size_mb": 2.34
    },
    "jsonl": {
      "path": "dataset/crm_layouts.jsonl",
      "size_bytes": 2156789,
      "size_mb": 2.06
    }
  }
}
```

---

## Usage Examples

### Example 1: Generate Dataset
```bash
curl -X POST "http://localhost:8000/dataset/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "total_records": 2000,
    "force_regenerate": false
  }'
```

### Example 2: Check Dataset Info
```bash
curl -X GET "http://localhost:8000/dataset/info"
```

### Example 3: Process a Query
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "show lead metrics dashboard",
    "format": "json"
  }'
```

### Example 4: Search Similar Layouts
```bash
curl -X POST "http://localhost:8000/rag/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "display case status with alerts",
    "object_type": "case",
    "top_k": 5,
    "rerank": true,
    "final_k": 3
  }'
```

---

## Pattern Information

The system uses 16 patterns for layout generation:

| Pattern ID | Pattern Name | Description |
|-----------|--------------|-------------|
| pattern0 | Dashboard Metrics (3 Dashlets) | Dashboard view with 3 metric cards |
| pattern1 | Title + Description | Simple heading with descriptive text |
| pattern2 | Title + Description + List | Heading, description, and list |
| pattern3 | Description Only | Minimal text-only response |
| pattern4 | Title + List | Heading with bulleted list |
| pattern5 | Title + Description + List + Card | Rich detailed view combining list and card |
| pattern6 | Title + Description + Table + Summary | Tabular data view with context |
| pattern7 | Dashlet 4 Columns | Full-width dashboard with 4 metric cards |
| pattern8 | Title + Badges + Description | Status-focused view with badges |
| pattern9 | Metrics Row (3 Metrics) | KPI metrics with trend indicators |
| pattern10 | Card Grid (2 Cards) | Side-by-side card layout |
| pattern11 | Title + Table | Table view with heading |
| pattern12 | Alert + Title + Description | Attention-grabbing layout with alert |
| pattern13 | List with Cards | Activity list with detailed card |
| pattern14 | Metrics + Table (Analytics) | Analytics dashboard with metrics and table |
| pattern15 | Detailed Field View | Complete field breakdown |

---

## Object Types

The system supports the following CRM object types:
- **Lead**: Potential customers
- **Account**: Organizations/companies
- **Contact**: Individual people
- **Case**: Support cases/tickets
- **Opportunity**: Sales opportunities

---

## Error Handling

All endpoints return standard HTTP status codes:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid request parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Error response format:
```json
{
  "detail": "Error message description"
}
```

---

## Development

### Starting the Server
```bash
# Using the provided scripts
.\start-dev.ps1        # Development mode (Windows)
.\start-prod.ps1       # Production mode (Windows)

# Or manually
uvicorn design_system_agent.api.main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation
Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## Notes

- Dataset generation can take several minutes depending on `total_records`
- RAG index is automatically built on first search if it doesn't exist
- Use `force_regenerate: true` carefully as it will overwrite existing datasets
- All patterns use comprehensive LLM guidance for intelligent layout selection
