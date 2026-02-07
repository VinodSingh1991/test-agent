# Setup Guide - LLM-Only System

## ⚠️ IMPORTANT: API Key Required

This system now **requires** `OPENAI_API_KEY` to function. All keyword-based fallbacks have been removed per your request.

## Quick Setup

### Windows PowerShell

```powershell
# Set for current session
$env:OPENAI_API_KEY = 'sk-your-api-key-here'

# Set permanently (User level)
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-your-api-key-here', 'User')

# Verify it's set
$env:OPENAI_API_KEY
```

### Linux/Mac Bash

```bash
# Set for current session
export OPENAI_API_KEY='sk-your-api-key-here'

# Set permanently (add to ~/.bashrc or ~/.zshrc)
echo "export OPENAI_API_KEY='sk-your-api-key-here'" >> ~/.bashrc
source ~/.bashrc

# Verify it's set
echo $OPENAI_API_KEY
```

### Using .env file

Create `.env` file in project root:
```env
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4o-mini  # Optional: override default model
```

Install python-dotenv:
```bash
pip install python-dotenv
```

Load in your code:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Obtaining an API Key

1. **Go to** https://platform.openai.com/api-keys
2. **Sign in** or create an OpenAI account
3. **Click** "Create new secret key"
4. **Copy** the key (starts with `sk-`)
5. **Store it safely** - you won't see it again!

## Verify Setup

Run the diagnostic test:

```bash
python test_llm_only.py
```

**If API key is correct:**
```
✓ TEST COMPLETED - System uses LLM-only approach
```

**If API key is missing:**
```
⚠️  OPENAI_API_KEY NOT SET
This system now requires OPENAI_API_KEY for all operations.
```

**If API key is invalid:**
```
✗ FAILED: Incorrect API key provided
```

## Model Selection

Default model: `gpt-4o-mini` (fastest, most cost-effective)

To use a different model:

```powershell
$env:OPENAI_MODEL = 'gpt-4o'  # Most capable (slower, expensive)
```

Available models:
- `gpt-3.5-turbo` - Fastest, cheapest (good for simple queries)
- `gpt-4o-mini` - **Default** - Best balance
- `gpt-4-turbo` - Legacy high-performance
- `gpt-4o` - Most capable (for complex queries)

## Cost Estimation

Approximate costs per 1000 API calls:

| Component | Tokens/Call | Cost (gpt-4o-mini) |
|-----------|-------------|-------------------|
| QueryAnalyzer | ~500 | $0.01 |
| LayoutSelectorAgent | ~2000 | $0.03 |
| DataFillingAgent | ~1500 | $0.02 |
| **Total per query** | ~4000 | **$0.06** |

**Monthly estimate** (1000 queries):
- Development: ~$60/month
- Production (10K queries): ~$600/month

💡 **Tip:** Use caching and query deduplication to reduce costs

## Troubleshooting

### Error: "OPENAI_API_KEY not set"

**Solution:**
```powershell
$env:OPENAI_API_KEY = 'sk-...'
```

### Error: "Rate limit exceeded"

**Solution:**
- Wait 60 seconds
- Implement request throttling
- Upgrade to higher tier plan

### Error: "API quota exceeded"

**Solution:**
- Check billing at https://platform.openai.com/account/billing
- Add payment method or increase quota
- Use cheaper model (gpt-5-nano)

### Error: "'AIMessage' object has no attribute 'normalized_query'"

This means the mock LLM is being used (no API key).

**Solution:**
- Set OPENAI_API_KEY properly
- Restart your Python process/API server

### Query works but returns empty data

**Check:**
1. Is `crm_sample_data.json` present?
   ```bash
   ls design_system_agent/dataset/crm_sample_data.json
   ```

2. Does it have data for your object type?
   - Lead: `lead_list_example`, `lead_detail_example`
   - Case: `case_list_example`, `case_detail_example`
   - etc.

## API Server Startup

```bash
# Make sure API key is set
$env:OPENAI_API_KEY = 'sk-...'

# Start server
python -m uvicorn design_system_agent.api.main:app --reload --port 8000

# Test endpoint
curl http://localhost:8000/health
```

## Development vs Production

### Development
```powershell
# Use cheaper model
$env:OPENAI_MODEL = 'gpt-3.5-turbo'

# Enable debug logging
$env:LOG_LEVEL = 'DEBUG'

# Start dev server
python -m uvicorn design_system_agent.api.main:app --reload
```

### Production
```powershell
# Use balanced model
$env:OPENAI_MODEL = 'gpt-4o-mini'

# Disable reload
python -m uvicorn design_system_agent.api.main:app --host 0.0.0.0 --port 8000

# Or use Docker
docker-compose up -d
```

## Security Best Practices

### ✅ DO:
- Store API key in environment variables
- Use `.env` file (add to `.gitignore`)
- Rotate keys regularly
- Use separate keys for dev/prod
- Monitor usage at https://platform.openai.com/usage

### ❌ DON'T:
- Commit API keys to git
- Share keys in Slack/email
- Use same key across multiple projects
- Expose keys in client-side code
- Log API keys in application logs

## Getting Help

If you're still having issues:

1. **Check logs:**
   ```bash
   tail -f logs/app.log
   ```

2. **Run diagnostics:**
   ```bash
   python setup_diagnostic.py
   ```

3. **Test individual components:**
   ```bash
   python test_llm_only.py
   ```

4. **OpenAI Status:**
   - https://status.openai.com/

5. **System requirements:**
   - Python 3.14+
   - OpenAI API access
   - 500MB free memory
   - Internet connection

## Support

For issues:
- Check [LLM_ONLY_UPDATE.md](LLM_ONLY_UPDATE.md) for recent changes
- Review [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API details
- Check OpenAI documentation: https://platform.openai.com/docs

---

**Last Updated:** 2026-02-07
**System Version:** LLM-Only (no keyword fallbacks)
