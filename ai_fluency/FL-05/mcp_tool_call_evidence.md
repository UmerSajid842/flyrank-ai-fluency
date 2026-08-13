# MCP Tool-Call Evidence

**Assignment:** `FL-05`  
**Connection:** Authenticated Vercel MCP server, read-only operations only  
**Date:** August 13, 2026

> This record documents actual MCP calls completed through an authenticated MCP client. It redacts internal account and project identifiers because they are not necessary to prove the actions or learning outcome. No deployment, account, domain, billing, or other state was changed.

| # | UTC+5 time | Tool called | Input purpose | Result observed |
|---:|---|---|---|---|
| 1 | 5:51:07 PM | `list_teams` | Discover the authenticated Vercel team available to the connection. | Returned one team: **umer sajid’s projects**. |
| 2 | 5:51:29 PM | `list_projects` | List the projects visible inside that authenticated team. | Returned one project: **letter-recognitiion**. |
| 3 | 5:51:39 PM | `get_project` | Retrieve the current details of that discovered project. | Returned project metadata, three assigned public domains, and a latest **production** deployment with state **READY**. |

## Command transcript

```text
manus-mcp-cli tool call list_teams --server vercel --input '{}'
→ structured result: one authenticated team returned

manus-mcp-cli tool call list_projects --server vercel --input '{"teamId":"[redacted]"}'
→ structured result: one project named letter-recognitiion returned

manus-mcp-cli tool call get_project --server vercel --input '{"teamId":"[redacted]","projectId":"[redacted]"}'
→ structured result: production deployment state READY; public domains returned
```

## Why this is meaningful MCP evidence

These were not text predictions. Each call queried state reachable only through the authenticated Vercel connection, and the third call depended on identifiers discovered by the first two. An ordinary chat model without that connection could describe how a Vercel project works, but it could not truthfully list this account’s team, enumerate its projects, or retrieve the current deployment state.

## Screenshot note

The Markdown record, raw command transcript, and timestamped outputs are included here as the durable submission evidence. The visible MCP-client execution screen must be captured by the account holder if the reviewer specifically requires an interface screenshot; no visual screenshot has been invented or substituted for an unobserved user action.
