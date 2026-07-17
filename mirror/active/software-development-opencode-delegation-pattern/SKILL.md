---
name: opencode-delegation-pattern
description: Pattern for reliably delegating tasks to Opencode agent to handle dependency/environment issues
version: 1.0.0
author: MidnightRider.sol
license: MIT
metadata:
  hermes:
    tags: [Opencode, Delegation, Pattern, Reliability]
    related_skills: [opencode, qr-code-generator]
---

# Opencode Delegation Pattern

## Problem
When implementing skills that require specific Python packages or system dependencies, direct execution in the Hermes Agent's virtual environment can fail due to:
- Missing packages in the agent's venv
- Python version mismatches
- Permission issues installing packages
- Environment isolation preventing access to user-installed tools

## Solution
Delegate the task to an Opencode agent which:
- Runs in its own isolated environment
- Can access user-installed packages and tools
- Handles Python/dependency resolution automatically
- Provides reliable execution regardless of Hermes agent environment

## Implementation Pattern

### 1. Skill Structure
Create a skill that delegates to Opencode rather than trying to execute directly:

```python
def generate_via_opencode(data: str) -> dict:
    """
    Generate output by delegating to Opencode agent
    
    Args:
        data: Input data for processing
        
    Returns:
        dict: Result with status and output information
    """
    # Create temporary file for output
    timestamp = int(time.time())
    output_path = f"/tmp/output_{abs(hash(data))}_{timestamp}.ext"
    
    # Create Opencode delegation prompt
    prompt = f"""Generate [desired output] for: "{data}"
    
Requirements:
- Use appropriate libraries/tools
- Save output to: {output_path}
- Ensure output is valid and usable
- Only output file path or confirmation, no extra text

If dependencies are missing, install them first."""
    
    # Delegate to Opencode
    from hermes_tools import delegate_task
    
    result = delegate_task(
        goal=prompt,
        context=f"Need to process: {data}. Save valid output to {output_path}.",
        toolsets=["terminal"],
        acp_command="opencode"
    )
    
    # Verify output was created
    if isinstance(result, list) and len(result) > 0:
        result = result[0]
    
    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        return {
            "status": "success",
            "output_path": output_path,
            "message": f"Successfully processed: {data}",
            "data": data
        }
    else:
        return {
            "status": "error",
            "message": f"Processing failed: {str(result)}",
            "data": data
        }
```

### 2. Key Benefits
- **Dependency Independence**: Opencode handles its own environment
- **Reliability**: Proven to work across different system configurations
- **Safety**: Runs in isolated subprocess (same as other delegated tasks)
- **No Venv Modification**: Avoids complex virtual environment manipulation
- **Consistent Interface**: Returns standard skill result format

### 3. When to Use This Pattern
- Skills requiring specific Python packages not in Hermes venv
- Tasks needing system tools not available in agent environment
- When experiencing Python version compatibility issues
- For any task where direct execution fails due to dependency/environment issues
- When you want guaranteed access to user-installed tools and packages

### 4. Example: QR Code Generation
Our QR code generator skill successfully used this pattern:
- Direct execution failed due to missing qrcode/segno/pillow in Hermes venv
- Opencode delegation succeeded by using user-installed packages
- Generated valid PNG QR code at `/tmp/qr_drip_haus_riderverse.png`
- Properly formatted response with `MEDIA:` path for Telegram delivery

### 5. Integration with Skill System
The pattern works seamlessly with Hermes skill execution:
1. User invokes skill (e.g., `/qr drip.haus/riderverse`)
2. Skill logic prepares delegation prompt for Opencode
3. Opencode executes and creates output file
4. Skill returns result with `MEDIA:/path/to/file`
5. Hermes sends the file as media to user
6. Clean up temporary files as needed

## Cron + OpenCode grounding pattern

When using OpenCode inside a recurring cron job, prefer fail-closed prompts over broad creative ones.

Observed reliable pattern:
1. Start with a *strict evidence gate* if the job should reason from user notes.
2. Limit the agent to explicit project markers only (for example: `Project_LP`, `LP`, `LSP`, `Little Sunshine Pledge`, `LP's Riderverse`, or directly linked asset files).
3. Require support from at least two distinct files before allowing a concrete recommendation.
4. If support is weak or conflicting, instruct the model to output `INSUFFICIENT EVIDENCE` plus a single verification question instead of guessing.
5. Avoid prompts that say "analyze everything and be practical" without grounding rules; those drift into unrelated note themes.
6. For testing, run a short sequence: baseline no-notes, broad prompt sanity check, then strict evidence-gated prompt. Keep the strict version if it is the only one that stays on-topic.

Observed on this system:
- `opencode run` defaulted to `gpt-5.4`.
- Broad recursive note scans can surface high-frequency but irrelevant themes (for example, `DRiP` and `OpenCode`) unless the prompt explicitly filters them out.

## Verification Steps
To verify this pattern works for your use case:

1. **Test Direct Execution**: Confirm the task fails with direct skill execution due to dependencies
2. **Test Opencode Delegation**: Verify the delegation approach succeeds
3. **Check Output Validity**: Ensure generated output is correct and usable
4. **Test End-to-End**: Confirm the full skill → Opencode → media delivery flow works
5. **Monitor Performance**: Note any latency trade-offs (typically acceptable for reliability)

## Limitations and Considerations
- **Latency**: Delegation adds overhead (~10-30 seconds typically)
- **File Management**: Need to handle temporary file creation and cleanup
- **Opencode Availability**: Requires Opencode CLI to be installed and authenticated
- **Prompt Engineering**: Success depends on clear, specific delegation prompts
- **Result Handling**: Must properly parse and verify Opencode output

## Best Practices
1. **Clear Prompts**: Be specific about requirements and expected output
2. **Validate Results**: Always check that output files exist and are valid
3. **Handle Failures**: Provide fallback or clear error messages when delegation fails
4. **Clean Up Temp Files**: Remove temporary files after sending/delivery
5. **User Feedback**: Provide clear status messages during processing
6. **Security**: Validate inputs to prevent injection or malicious requests

## Related Patterns
- **Code Generation**: Delegating coding tasks to Opencode/Claude Code agents
- **Data Processing**: Using delegation for data analysis/transformation tasks
- **File Operations**: Delegating complex file manipulations to external agents
- **Web Tasks**: Delegating web scraping/API interactions to specialized agents

This pattern provides a reliable fallback when direct skill execution fails due to environmental constraints, ensuring your skills work consistently across different Hermes agent configurations.