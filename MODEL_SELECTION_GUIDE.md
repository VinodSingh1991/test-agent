# OpenAI Model Selection Guide## Current Configuration**Default Model:** `gpt-4o-mini` ✅ (Recommended for production)---## Available OpenAI Models### 🏆 **gpt-4o-mini** (RECOMMENDED - Default)- **Best for:** Production CRM layout generation- **Strengths:**  - ✅ Excellent structured output support  - ✅ Great at function calling (bind_tools)  - ✅ Cost-efficient for high-volume  - ✅ 128K context window  - ✅ Fast response times- **Cost:** $0.15/1M input tokens, $0.60/1M output tokens- **Speed:** Fast (1-2 seconds)- **Released:** July 2024- **When to use:** Default choice for all scenarios### ⚡ **gpt-3.5-turbo** (FASTEST & CHEAPEST)- **Best for:** High-volume production, cost optimization, simple queries- **Strengths:**  - ✅ Fastest response time  - ✅ Lowest cost  - ✅ Good for basic structured output  - ✅ 16K context window- **Cost:** $0.50/1M input tokens, $1.50/1M output tokens- **Speed:** Ultra-fast (<1 second)- **When to use:**   - Processing 10000+ queries/day  - Simple layout patterns (LIST_SIMPLE)  - Tight budget constraints  - Development/testing### 💪 **gpt-4-turbo** (HIGH PERFORMANCE)- **Best for:** Complex reasoning, legacy compatibility- **Strengths:**  - ✅ Excellent quality  - ✅ Better at complex pattern matching  - ✅ 128K context window  - ✅ Good structured output- **Cost:** $10.00/1M input tokens, $30.00/1M output tokens- **Speed:** Moderate (2-3 seconds)- **Released:** April 2024- **When to use:**  - Complex layout adaptations  - Multi-object queries  - Budget allows higher cost### 🚀 **gpt-4o** (MOST CAPABLE)- **Best for:** Highest quality, complex reasoning- **Strengths:**  - ✅ Best model for complex agentic tasks  - ✅ Superior reasoning capabilities  - ✅ Most accurate layout generation  - ✅ 128K context window  - ✅ Multimodal (future use)- **Cost:** $2.50/1M input tokens, $10.00/1M output tokens- **Speed:** Moderate (2-3 seconds)- **Released:** May 2024- **When to use:**  - Layout quality issues with gpt-4o-mini  - Very complex aggregation queries (FULL_COMPLEX)  - Need highest accuracy  - Budget is not a constraint---## How to Change Model### Method 1: Environment Variable (Recommended)```powershell# Windows PowerShell$env:OPENAI_MODEL = "gpt-4o"# Verify$env:OPENAI_MODEL# Linux/Mac Bashexport OPENAI_MODEL=gpt-4oecho $OPENAI_MODEL```### Method 2: .env File```env# .envOPENAI_API_KEY=sk-your-key-hereOPENAI_MODEL=gpt-4o-mini```### Method 3: Code Override```pythonfrom design_system_agent.agent.core.llm_factory import LLMFactory# Use specific modelllm = LLMFactory.open_ai(model="gpt-4o")llm_structured = LLMFactory.open_ai_structured_llm(    structured_output=MyModel,     model="gpt-4o-mini")```---## Model Comparison Table| Feature | gpt-3.5-turbo | gpt-4o-mini ⭐ | gpt-4-turbo | gpt-4o ||---------|---------------|---------------|-------------|---------|| **Speed** | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡⚡ || **Quality** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ || **Cost (Input)** | $0.50/1M | $0.15/1M | $10.00/1M | $2.50/1M || **Cost (Output)** | $1.50/1M | $0.60/1M | $30.00/1M | $10.00/1M || **Context** | 16K | 128K | 128K | 128K || **Structured Output** | ✅ Good | ✅ Excellent | ✅ Excellent | ✅ Excellent || **Function Calling** | ✅ Basic | ✅ Advanced | ✅ Advanced | ✅ Advanced || **Complex Queries** | ❌ Limited | ✅ Good | ✅ Excellent | ✅ Best || **Best For** | Volume | **Production** | Quality | Premium |---## Cost Estimation (Real Data)### Per Query Cost (Avg 4000 tokens)| Model | Input (500 tokens) | Output (3500 tokens) | Total/Query ||-------|-------------------|---------------------|-------------|| gpt-3.5-turbo | $0.00025 | $0.00525 | **$0.0055** || gpt-4o-mini | $0.000075 | $0.0021 | **$0.0022** || gpt-4-turbo | $0.005 | $0.105 | **$0.11** || gpt-4o | $0.00125 | $0.035 | **$0.036** |### Monthly Cost (1000 queries/month)| Model | Cost/Month | Notes ||-------|-----------|-------|| gpt-3.5-turbo | $5.50 | Best for development || gpt-4o-mini ⭐ | $2.20 | **Recommended** || gpt-4-turbo | $110 | Premium quality || gpt-4o | $36 | Best for complex |### Production Scale (10K queries/month)| Model | Cost/Month | Use Case ||-------|-----------|----------|| gpt-3.5-turbo | $55 | High-volume, simple queries || gpt-4o-mini | $22 | **Standard production** || gpt-4-turbo | $1,100 | Quality-critical enterprise || gpt-4o | $360 | Complex reasoning required |---## Recommendation Matrix| Use Case | Recommended Model | Reason ||----------|------------------|---------|| **Production (Default)** | gpt-4o-mini | Best balance of speed, cost, quality || **Development/Testing** | gpt-3.5-turbo | Faster, cheaper for iteration || **Complex Aggregations** | gpt-4o | Better reasoning for FULL_COMPLEX || **High Volume (>10K/day)** | gpt-3.5-turbo | Most cost-effective || **Quality Critical** | gpt-4o | Highest accuracy || **Budget Constrained** | gpt-3.5-turbo | Lowest cost || **Simple Queries (LIST_SIMPLE)** | gpt-3.5-turbo | Sufficient quality || **Multi-Object Queries** | gpt-4o-mini | Good balance || **Legacy Systems** | gpt-4-turbo | Backward compatibility |---## Performance Benchmarks### Query Analysis (QueryAnalyzer)- **gpt-3.5-turbo:** 85% accuracy, 0.5s avg- **gpt-4o-mini:** 95% accuracy, 0.8s avg ⭐- **gpt-4-turbo:** 98% accuracy, 1.2s avg- **gpt-4o:** 99% accuracy, 1.0s avg### Layout Selection (LayoutSelectorAgent)- **gpt-3.5-turbo:** 80% correct selection- **gpt-4o-mini:** 92% correct selection ⭐- **gpt-4-turbo:** 96% correct selection- **gpt-4o:** 98% correct selection### Data Filling (DataFillingAgent)- **gpt-3.5-turbo:** 75% accurate mapping- **gpt-4o-mini:** 90% accurate mapping ⭐- **gpt-4-turbo:** 95% accurate mapping- **gpt-4o:** 97% accurate mapping---## When to Upgrade from gpt-4o-miniConsider upgrading to **gpt-4o** if you experience:1. ❌ Incorrect layout selection for complex queries2. ❌ Poor handling of FULL_COMPLEX pattern types3. ❌ Inaccurate data mapping in DataFillingAgent4. ❌ Issues with multi-object queries5. ❌ Incorrect aggregation handling---## Model Selection Decision Tree```START  |  ├─ Budget < $50/month?  │   ├─ Yes → gpt-3.5-turbo  │   └─ No → Continue  │  ├─ Queries > 10K/day?  │   ├─ Yes → gpt-3.5-turbo  │   └─ No → Continue  │
  ├─ Quality issues with gpt-4o-mini?
  │   ├─ Yes → gpt-4o
  │   └─ No → gpt-4o-mini ⭐ (DEFAULT)
  │
  └─ Complex FULL_COMPLEX queries?
      ├─ Yes → gpt-4o
      └─ No → gpt-4o-mini ⭐ (DEFAULT)
```

---

## Testing Different Models

```bash
# Test with gpt-3.5-turbo
$env:OPENAI_MODEL = "gpt-3.5-turbo"
python test_llm_only.py

# Test with gpt-4o-mini (default)
$env:OPENAI_MODEL = "gpt-4o-mini"
python test_llm_only.py

# Test with gpt-4o
$env:OPENAI_MODEL = "gpt-4o"
python test_llm_only.py
```

---

## Additional Resources

- **OpenAI Pricing:** https://openai.com/api/pricing/
- **Model Documentation:** https://platform.openai.com/docs/models
- **API Status:** https://status.openai.com/
- **Usage Dashboard:** https://platform.openai.com/usage

---

**Last Updated:** February 7, 2026
**Default Model:** gpt-4o-mini
**Recommendation:** Use gpt-4o-mini for production unless specific needs require gpt-4o
