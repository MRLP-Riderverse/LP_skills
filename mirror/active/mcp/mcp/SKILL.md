---
name: mcp
description: "MCP (Model Context Protocol) — connect servers, register tools, call endpoints via CLI and native client."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP, Model-Context-Protocol, tools, servers, CLI, stdio, HTTP]
    related_skills: [hermes-agent]
    absorbed_skills: [mcporter, native-mcp]
---

# MCP — Model Context Protocol Client Guide

Class-level skill for working with MCP servers in Hermes. Two access paths: **mcporter CLI** (ad-hoc server interaction) and **native MCP client** (config-driven auto-discovery).

## When to Use

- Need to call an external tool provided by an MCP server
- Want to configure a new MCP server for persistent use
- Ad-hoc: use mcporter CLI for quick one-off calls
- Persistent: add server to config.yaml for auto-discovery

---

## mcporter CLI — Ad-Hoc Server Interaction

### List Available Servers

```bash
mcporter list
```

### Configure a Server

```bash
# Add a stdio-based server
mcporter config add my-server --transport stdio --command "npx" --args "-y,my-mcp-server"

# Add an HTTP-based server
mcporter config add my-api --transport http --url http://localhost:8080/mcp
```

### Authenticate

```bash
mcporter auth login my-server
mcporter auth status my-server
```

### Call Tools

```bash
# List tools on a server
mcporter tools list my-server

# Call a tool
mcporter tools call my-server tool-name --input '{"key": "value"}'
```

### Generate Types

```bash
# Generate TypeScript types from a server's schema
mcporter types generate my-server --output types.ts
```

---

## Native MCP Client — Config-Driven Auto-Discovery

Servers configured in `~/.hermes/config.yaml` under the `mcp` section are auto-discovered and their tools registered at startup.

### Config Format

```yaml
mcp:
  servers:
    my-stdio-server:
      transport: stdio
      command: npx
      args: ["-y", "my-mcp-server"]
    
    my-http-server:
      transport: http
      url: http://localhost:8080/mcp
      headers:
        Authorization: "Bearer ${MY_API_KEY}"
```

### Auto-Discovered Tools

When a server is configured, all its tools become available as regular Hermes tools. No manual call needed — just use the tool name directly.

### Adding a New Server

1. Edit `~/.hermes/config.yaml` to add the server entry
2. Restart Hermes or run `hermes mcp reload`
3. New tools appear in the tool list automatically

---

## Server Types

| Transport | Use case | Connection |
|-----------|----------|------------|
| **stdio** | Local CLI tools, language servers | Process spawn via command |
| **HTTP** | Remote services, APIs | HTTP POST to URL |
| **SSE** | Streaming services | Server-Sent Events |

---

## Pitfalls

- **Server startup** — stdio servers may take time to start; first call may be slow
- **Process cleanup** — stdio servers need proper cleanup on exit
- **Auth tokens** — HTTP servers may need API keys in headers
- **Tool name collisions** — two servers may expose the same tool name; namespace with server prefix
- **Config reload** — adding a server to config requires restart or explicit reload
