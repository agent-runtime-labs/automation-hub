# Automation Hub

A collection of AI-powered tools and workflows that you can use to automate tasks in OpenCode.

## What is this?

This is a library of reusable **skills** and **commands** that extend OpenCode's capabilities. Think of it as a toolkit where you can:
- Create and manage automation workflows
- Run common tasks with simple commands
- Build enterprise automation solutions

## Quick Start

### Available Commands

Use these slash commands in OpenCode:

- `/grill-me` - Stress-test a plan or design
- `/search-talent-kb` - Search candidates in the talent knowledge base
- `/publish-candidates-workflow` - Generate candidate PDFs and publish them via GitHub PR

### How to Use

1. Start OpenCode
2. Type a slash command (e.g., `/publish-candidates-workflow`)
3. Follow the prompts to complete the workflow



## Architecture

```mermaid
flowchart TD
    user["User"] --> opencode["OpenCode"]
    config["opencode.json\nLoads skills + MCP servers"] --> opencode

    opencode --> cmd_grill["/grill-me"]
    opencode --> cmd_search["/search-talent-kb"]
    opencode --> cmd_publish["/publish-candidates-workflow"]

    cmd_grill --> skill_grill["grill-me skill\nStress-test plans"]
    cmd_search --> skill_search["search-talent-kb skill\nSearch candidates"]
    cmd_publish --> skill_generate["generate-clinicians skill\nGenerate profiles"]
    cmd_publish --> skill_publish["publish_candidates_pr skill\nCreate GitHub PR"]

    skill_search --> mcp_talent["talent-kb MCP\nCandidate database"]
    skill_generate --> mcp_candidate["candidate-generator MCP\nSynthetic profile data"]
    skill_generate --> mcp_document["document-generator MCP\nPDF generation"]
    skill_publish --> mcp_github["github MCP\nBranch, commit, PR"]

    mcp_candidate --> script["scripts/fake_candidate_profile.py"]
    mcp_document --> pdfs["Generated PDFs"]
    mcp_github --> repo["talent-knowledge-base repo"]

    opencode -. optional tools .-> mcp_playwright["playwright MCP\nBrowser automation"]
    opencode -. optional tools .-> mcp_grep["grep_app MCP\nPublic code search"]

    classDef entry fill:#dbeafe,stroke:#2563eb,color:#1e3a8a;
    classDef command fill:#fef3c7,stroke:#d97706,color:#78350f;
    classDef skill fill:#dcfce7,stroke:#16a34a,color:#14532d;
    classDef mcp fill:#fce7f3,stroke:#db2777,color:#831843;
    classDef output fill:#ede9fe,stroke:#7c3aed,color:#3b0764;

    class user,opencode,config entry;
    class cmd_grill,cmd_search,cmd_publish command;
    class skill_grill,skill_search,skill_generate,skill_publish skill;
    class mcp_talent,mcp_candidate,mcp_document,mcp_github,mcp_playwright,mcp_grep mcp;
    class script,pdfs,repo output;
```


## Skills (Automation Workflows)

This repo includes several skills that power the commands:

- **grill-me** - Tests your plans with rigorous questioning before you build
- **generate-clinicians** - Creates synthetic healthcare candidate profiles
- **publish_candidates_pr** - Commits candidates to Git and creates pull requests

## Setup

After you add or update skills and commands, **restart OpenCode** so it loads your changes.

## Need Help?

- Check `.opencode/skills/` to see how skills are built
- Look at `.opencode/commands/` to see how commands are structured
- See `AGENTS.md` for detailed development guidelines

---

Built with OpenCode. Learn more at [opencode.ai](https://opencode.ai)
