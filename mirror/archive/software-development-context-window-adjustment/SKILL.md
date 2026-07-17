---
name: context-window-adjustment
description: Adjust context window length in Hermes Agent for custom or non-standard models. Provides systematic approach to identify, override, and verify context limits.
version: 1.0.0
author: MidnightRider.sol
license: MIT
platforms: [linux, macos]
prerequisites:
  commands: [hermes]
metadata:
  hermes:
    tags: [context, window, tokens, configuration, model-limits]
    homepage: https://github.com/NousResearch/hermes-agent
---

# Context Window Adjustment in Hermes Agent

This skill provides a systematic approach to adjust the context window length when using custom, non-standard, or newly released models that may not have accurate context length information in the model registries.

## When to Use This Skill

- You're using a custom model (like NVIDIA NIM, local models, or enterprise endpoints)
- The context window percentage seems incorrect or too restrictive
- You need to increase context limits for long conversations, code analysis, or document processing
- Models.dev or OpenRouter don't have accurate context information for your model
- You want to verify and override context limits systematically

## How Hermes Determines Context Windows

Hermes uses this fallback chain to determine context window size:

1. **models.dev registry** (primary source)
2. **OpenRouter API** (fallback for known models)
3. **Hardcoded defaults** in `agent/model_metadata.py`
4. **Context probing** (adaptive fallback that tests decreasing sizes)

## Step-by-Step Procedure

### 1. Identify Current Configuration

First, check your current model setup:

```bash
cat ~/.hermes/config.yaml | grep -A 5 "model:"
```

Look for:
- `default`: model identifier
- `provider`: provider name (custom, openrouter, etc.)
- `base_url`: API endpoint
- `api_key`: authentication token

### 2. Check What Models.dev Says

For standard models, verify what the registries report:

```bash
# Check context from models.dev
hermes execute-code --code "
import sys
sys.path.insert(0, '~/.hermes/hermes-agent')
from agent.models_dev import lookup_models_dev_context
ctx = lookup_models_dev_context('PROVIDER', 'MODEL_NAME')
print(f'Context from models.dev: {ctx}')
"
```

Replace `PROVIDER` and `MODEL_NAME` with your values (e.g., `nvidia` and `nemotron-3-super-120b-a12b`).

### 3. Apply Context Window Override (Recommended for Custom Models)

For custom models or when registries have incorrect data, add an explicit override to your config:

```yaml
# In ~/.hermes/config.yaml under the model section:
model:
  default: your/model-name
  provider: custom  # or your actual provider
  base_url: https://your-api-endpoint/v1
  api_key: your-api-key-here
  context_window: 262144  # 256K in tokens
```

**Important**: The value must be in tokens. Common values:
- 32K = 32768
- 64K = 65536  
- 128K = 131072
- 256K = 262144
- 1M = 1048576

### 4. Verify the Change

After saving your config, the context percentage shown in the interface should now be based on your new limit.

You can also verify programmatically:

```bash
hermes execute-code --code "
import sys
sys.path.insert(0, '~/.hermes/hermes-agent')
from agent.model_metadata import get_context_window_length
# This would need the actual model resolution - for verification,
# check that your config value is being used
print('Check context percentage in chat interface')
"
```

### 5. Alternative: Update Hardcoded Defaults (Advanced)

If you want this to persist across config changes for a specific model family, you can edit the hardcoded defaults:

```bash
# Edit the default context lengths
nano ~/.hermes/hermes-agent/agent/model_metadata.py

# Find the DEFAULT_CONTEXT_LENGTHS dictionary and add/edit:
DEFAULT_CONTEXT_LENGTHS = {
    # ... existing entries
    "your-model-pattern": 262144,  # 256K
    # ... 
}
```

**Note**: This approach is less recommended as it may be overwritten during updates.

## Verification and Testing

### Quick Verification
After making changes:
1. Send a message in chat
2. Look for the context percentage display (usually in status bar or model info)
3. The percentage should reflect your new limit

Example: If you previously saw "65%" with 128K limit, with 256K limit you should see approximately "32%" for the same conversation length.

### Testing with Long Content
To test that your increased limit works:
1. Use a tool that can generate long content (like `execute_code` to create a large text file)
2. Try to fit that content in context
3. Verify you don't get "context window exceeded" errors

## Common Context Window Values

| Description | Tokens | Approx. Words |
|-------------|--------|---------------|
| Standard | 32768 | ~24,000 |
| Extended | 65536 | ~48,000 |
| Large | 131072 | ~96,000 |
| Very Large | 262144 | ~192,000 |
| Extremely Large | 1048576 | ~768,000 |

## Troubleshooting

### "Context window exceeded" errors persist
1. Double-check your config.yaml indentation (YAML is space-sensitive)
2. Ensure you restarted Hermes or started a new conversation after config change
3. Verify the exact model name matches what's in config
4. Check if another fallback source is overriding your setting

### Changes don't take effect
1. Run `hermes config reload` if available
2. Start a completely new conversation session
3. Check logs for any configuration loading errors
4. Ensure you're editing the correct config file (`~/.hermes/config.yaml`)

### Need to verify actual model capabilities
Remember: setting a high context window in Hermes doesn't magically give your model more context - it only tells Hermes how much to send. If the actual model doesn't support the context length you've set, you'll get API errors. Always verify your model's actual capabilities with the provider.

## Related Skills

- `hermes-agent`: Broad guide to Hermes configuration and usage
- `plan`: For creating implementation plans when doing complex configuration
- `systematic-debugging`: If you encounter issues after making changes

## Example: NVIDIA Nemotron Model

For the specific case discussed in the origin session:
```yaml
model:
  default: nvidia/nemotron-3-super-120b-a12b
  provider: custom
  base_url: https://integrate.api.nvidia.com/v1
  api_key: nvapi-your-key-here
  context_window: 262144  # Increased from likely 128K default
```

This skill was created based on practical experience adjusting context limits for custom NVIDIA models in Hermes Agent.