---
name: verify-telegram-gateway
description: Verify that Hermes Agent's Telegram gateway is properly configured and functioning by checking service status, configuration, logs, and message flow.
version: 1.0.0
author: Hermes Agent
tags: [telegram, gateway, troubleshooting, messaging, verification]
---
# Verify Telegram Gateway Functionality

This skill provides a systematic approach to verify that your Hermes Agent Telegram gateway is properly configured and operational.

## When to Use This Skill

- After initial Telegram gateway setup
- When you suspect gateway issues
- After configuration changes
- As part of routine system health checks
- When troubleshooting message delivery problems

## Verification Steps

### 1. Check Gateway Service Status
```bash
hermes gateway status
```

Look for:
- Service loaded and active (running)
- Main PID showing the gateway process
- Recent startup timestamp

### 2. Verify Telegram Platform Connection
```bash
hermes gateway setup
```

Navigate through the setup menu to see:
- Telegram platform status (should show "configured")
- Other platform statuses for reference

### 3. Examine Configuration
Check for proper Telegram settings:
```bash
# View masked configuration
hermes config | grep -i telegram

# Check environment file for actual values (token may be masked)
cat ~/.hermes/.env | grep -i telegram
```

Expected findings:
- `Telegram: configured` in config output
- `TELEGRAM_BOT_TOKEN=` line in .env
- `TELEGRAM_ALLOWED_USERS=` with your user ID
- `TELEGRAM_HOME_CHANNEL=` set appropriately

### 4. Check Gateway Logs for Activity
The most reliable verification method is checking actual message flow:
```bash
# Watch live gateway activity
tail -f ~/.hermes/logs/gateway.log | grep -i telegram

# Or check recent entries
grep -i telegram ~/.hermes/logs/gateway.log | tail -20
```

Look for:
- `[Telegram] Connected to Telegram (polling mode)` or similar connection confirmation
- `inbound message: platform=telegram` showing your messages
- `Sending response` or `outbound message` showing replies to you
- Message flushing/batched processing notifications

### 5. Test Message Flow (Indirect)
Since direct API testing may be hindered by masked credentials:
1. Send a test message to Hermes via Telegram
2. Watch the logs for the inbound message
3. Observe that a response is generated and sent back
4. Verify you receive the response in your Telegram chat

### 6. Alternative: Check Active Processes
```bash
# Verify Hermes gateway is running
ps aux | grep hermes | grep gateway

# Should show something like:
# /home/user/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main gateway run --replace
```

## Troubleshooting Common Issues

### Gateway Not Running
If `hermes gateway status` shows inactive:
```bash
hermes gateway start
# or
hermes gateway install  # if not installed as service
hermes gateway start
```

### Telegram Not Connected
If logs show connection issues:
1. Verify bot token is correct in ~/.hermes/.env
2. Check that TELEGRAM_ALLOWED_USERS includes your user ID
3. Ensure the bot has been started with /start in Telegram
4. Restart gateway: `hermes gateway restart`

### Session Stuck vs Gateway Stuck
A key distinction:
- `/stop` is a Telegram command that stops the currently running agent/session and unlocks it.
- `/stop` does not restart the Telegram gateway service itself.
- If Telegram commands are still being handled but one task is hung, `/stop` is the right recovery action.
- If Telegram commands stop being processed entirely, use a real gateway restart from the server/PC (`hermes gateway restart` or systemd restart).

Useful recovery order:
1. Try `/status` to confirm Telegram command handling is alive.
2. Try `/stop` to clear a stuck session.
3. If the gateway still seems wedged, restart the service from the host.

### Codex / ChatGPT Auth Path
Hermes may be configured for the `openai-codex` provider while actually using ChatGPT-backed Codex auth (`base_url: https://chatgpt.com/backend-api/codex`, `auth_mode: chatgpt`). In that case:
- Usage may not appear in the OpenAI/Codex dashboard the way API-key billing does.
- Hermes config can still show `openai-codex` even though it is not using a normal OpenAI API key flow.
- If you see model/provider fallback warnings in logs, check `hermes config` and `hermes doctor` before assuming billing or usage reporting is the issue.

### Unexpected Pairing Request From Telegram
If you receive a new DM pairing request unexpectedly:
1. Check gateway logs for an unauthorized Telegram DM event.
2. Inspect `~/.hermes/pairing/telegram-pending.json` for the pending code and metadata.
3. Remember that the default unauthorized DM behavior is `pair`, so any unknown Telegram user can trigger a pairing code response.
4. Verify whether the incoming event had a real Telegram user identity; `user_id: null` usually indicates the gateway could not resolve the sender cleanly.
5. If needed, revoke or ignore the pending pairing request rather than approving it.

Useful commands:
```bash
journalctl --user -u hermes-gateway.service --since '1 hour ago' --no-pager | grep -i telegram
cat ~/.hermes/pairing/telegram-pending.json
```
### Masked Credentials Preventing Direct Testing
The bot token in .env may appear as `***` for security. This is normal - the gateway uses the actual value internally. Trust the log evidence over direct API tests when tokens are masked.

## Verification Success Indicators

You can consider the Telegram gateway verified when you observe:
- Gateway service active and running
- Telegram platform shows as configured
- Logs show successful connection to Telegram
- Logs show inbound messages from your user ID
- Logs show outbound responses being sent to your chat
- You actually receive responses in your Telegram conversation

## Maintenance Tips

- Periodically check gateway status with `hermes gateway status`
- Monitor log file size; old logs are rotated automatically
- After changing Telegram configuration, restart gateway: `hermes gateway restart`
- Keep your bot token secure; never share the actual value from .env
- If you regenerate your bot token, update ~/.hermes/.env and restart gateway

## Related Skills

- `webhook-subscriptions` - For setting up event-driven triggers
- `hermes-agent` - For general Hermes configuration and troubleshooting
- `mcp` - For extending Hermes with external tools via MCP servers

---
**Note**: This skill focuses on verification rather than initial setup. For initial Telegram gateway configuration, use `hermes gateway setup` and follow the interactive prompts.