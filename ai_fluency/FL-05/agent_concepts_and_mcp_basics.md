# Agent Concepts and MCP Basics

**Assignment:** `FL-05`  
**Author:** Umer Sajid  
**Evidence date:** August 13, 2026

## Workflow versus agent

I think of a **workflow** as a fixed route: the same steps happen in the same order every time. Someone decides the sequence in advance, specifies what enters and leaves each step, and checks the result at the defined review points. A workflow can still use AI inside one of its steps, but that does not make the whole process an agent. Its strength is repeatability. Its weakness is that it does not decide for itself when to change its plan.

An **agent** has a goal and can choose among available actions while it works toward that goal. It may inspect a result, select a tool, ask for more information, or revise the next step. That makes it useful when the correct path depends on what the agent finds, but it also means its permissions and stopping rules need careful control. I would not describe every prompt chain as an agent. If I hand it five sources and require it to summarize, critique, and format them in a fixed order, that is still a workflow. If it can decide which sources to seek, which chart to inspect, whether evidence is insufficient, and when to stop, it is behaving more like an agent.

My Week 4 research-and-writing pipeline is currently a **workflow, not an agent**. It has a fixed three-plus-step route: prepare a public-safe source packet, extract structured study notes, draft a case-study paragraph, perform a claim audit, and have a human decide whether it can be published. I chose this because the job is evidence discipline, not autonomous browsing. The human review point is intentional: no AI-generated wording is allowed to upgrade a planned result into a verified result.

## What MCP adds

Model Context Protocol (MCP) is a standard connection between an AI client and an external server. It matters because the client can discover and use capabilities exposed by that server instead of relying only on text in a chat window. The official introduction describes MCP as an open protocol supported by multiple clients and servers. [1]

The three basic MCP primitives are **tools, resources, and prompts**. A tool is an operation the model or client can invoke with structured arguments. MCP tools are listed by a server and called through a dedicated tool-call operation; their definitions include an input schema. [2] A resource is information the server exposes for a client to read or include as context, such as a file, record, or web-backed object. Resources have a URI and can be listed or read by the client. [3] A prompt is a reusable, server-defined message template that the user explicitly selects, often with arguments. [4]

For this assignment, I connected to the authenticated **Vercel MCP server** through an MCP client. I used a read-only scope; I did not create, edit, deploy, purchase, or delete anything. This connection enabled three account-specific tasks that plain chat could not truthfully perform:

| Task | Actual result | Why ordinary chat could not do it |
|---|---|---|
| List the authenticated Vercel teams | Returned the signed-in team named “umer sajid’s projects.” | Chat has no authenticated view of my Vercel account. |
| List projects in that team | Returned one existing project, `letter-recognitiion`. | Project inventory is account-specific and changes over time. |
| Retrieve that project’s details | Returned its production deployment status as `READY` and its public domains. | Chat cannot verify the current deployment state of a private account connection. |

The accompanying execution record preserves the commands, timestamps, and redacted outputs for these three completed calls. It deliberately omits account and project IDs that are not needed to demonstrate the learning objective.

## A realistic upgrade path

I would upgrade the Week 4 workflow to an agent only after its fixed version has been tested. The agent’s goal could be: “Prepare an evidence-safe update to the portfolio case study.” Its allowed tools would be limited to reading a specified public source folder, checking repository status, and opening a deployment URL. It could decide which missing proof to flag, but it could not publish, alter source data, or make claims without a human approval step. This keeps the useful part of agent behavior—choosing what evidence needs attention—while protecting accuracy, privacy, and final publishing decisions.

## References

[1]: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro "Model Context Protocol — Introduction"
[2]: https://modelcontextprotocol.io/specification/2026-07-28/server/tools "Model Context Protocol Specification — Tools"
[3]: https://modelcontextprotocol.io/specification/2026-07-28/server/resources "Model Context Protocol Specification — Resources"
[4]: https://modelcontextprotocol.io/specification/2026-07-28/server/prompts "Model Context Protocol Specification — Prompts"
