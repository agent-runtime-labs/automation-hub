---
name: search-talent-kb
description: Search talent-kb for required candidates using the configured talent-kb MCP server; use when the user asks to find, lookup, shortlist, or search candidates in the talent database.
---

# Skill: Search Talent Knowledge Base

## Context
You are an AI assistant helping recruiters and hiring teams find matching candidate profiles from the organization's talent knowledge base. The project config already defines a remote MCP server named `talent-kb`. You MUST explicitly use the configured `talent-kb` MCP server/tool for candidate database searches and treat it as the only source of truth for candidate search results.

This skill now integrates with persistent memory blocks to cache and retrieve previous search results and candidate shortlists, allowing faster access to frequently needed profiles.

## Triggers
Use this skill whenever the user explicitly asks to:
- Search for candidates in the talent DB, talent KB, or talent knowledge base.
- Find candidates by role, specialty, skills, location, experience, certification, availability, candidate ID, or name.
- Shortlist candidates for a job requirement.
- Verify whether a specific candidate exists in the database.

## Required Inputs
Before searching, identify the user's search criteria. Useful criteria include:
- Role or specialty, such as ICU Nurse, Labor and Delivery Nurse, or Emergency Room Nurse.
- Required skills, certifications, licenses, location, years of experience, employment type, availability, or candidate ID.
- Ranking preference, such as most experienced, closest location match, exact certification match, or top N results.

## Clarification Rules
If the request does not include enough detail to perform a meaningful search, stop and ask one concise clarifying question. Ask only for the missing criteria needed to search.

Examples:
- "What role, specialty, or skill should I search for in the talent DB?"
- "Do you want an exact candidate lookup by ID/name, or a shortlist by role and requirements?"

Do not invent candidate criteria. Do not fabricate candidate data.

## Memory Integration
The skill now uses persistent memory to cache search results and shortlists:

**Memory Blocks Used:**
- `talent-kb-searches` (project scope) - Cached recent candidate searches with criteria and results
- `talent-kb-shortlists` (project scope) - Named shortlists for recurring job requirements

**Memory Workflow:**
1. Before executing a real-time search, ALWAYS ask the user to choose:
   - **Option A: Check Memory First** - Search cached results from previous talent-kb searches
   - **Option B: Real-Time Search** - Query the live talent-kb MCP server for fresh results
   - **Option C: Both** - Check memory first, then supplement with real-time results if needed

2. If user chooses memory search, use `memory_list` to check available blocks, then `memory_replace` or direct markdown editing to retrieve cached results.
3. If user chooses real-time, proceed with standard talent-kb search and optionally cache results with `memory_set`.
4. If user chooses both, start with memory cache, then supplement with live search for any gaps.

## Execution Rules
1. **ALWAYS ask the user first** whether they prefer cached memory results or real-time search before executing.
2. Explicitly use the configured `talent-kb` MCP server/tool for real-time candidate database searches.
3. Do not use GitHub, local files, generated candidate data, web search, or any other MCP server as a substitute for candidate DB search results.
4. If the available `talent-kb` tool names are not obvious in the active session, inspect available MCP tools/resources first, then choose the most specific search, query, retrieval, or lookup operation exposed by `talent-kb`.
5. Pass the user's criteria to the `talent-kb` MCP search/query operation as directly as possible. Preserve exact values for role names, certifications, IDs, and locations.
6. If the MCP server returns ranked scores, snippets, document references, or metadata, preserve those values in the output.
7. If the MCP server returns no matches, say so clearly and suggest one narrower or broader follow-up query.
8. If the `talent-kb` MCP server is unavailable, authentication fails, or required environment variables are missing, report the blocker clearly and do not substitute local guesses.
9. Keep any raw MCP output out of the final response unless it is necessary for debugging. Summarize candidate matches in a recruiter-friendly way.

## Output Formatting
Always format search results as a Markdown table.

For candidate matches, use this table shape when the data is available:

| Rank | Candidate | Candidate ID | Role/Specialty | Location | Experience | Key Matches | Confidence/Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Candidate name | ID | Role | Location | Years | Matching skills/certs | Score |

If exact fields are not returned by the MCP server, keep the table concise and use `Not provided` for missing values.

After the table, include a short `Notes` section only when useful. Keep it brief and include:
- Search criteria used.
- Any assumptions made.
- Any follow-up filter that would improve the result.

## Example Interaction - With Memory Integration

**User:** Search our DB for ICU nurses with 5+ years of experience and ACLS certification.

**Assistant:** Before I search, would you like me to:
- **A) Check Memory First** - Look for previously cached results for similar searches
- **B) Real-Time Search** - Query the live talent-kb database for fresh results
- **C) Both** - Check cache first, then supplement with real-time results

*User chooses "C) Both"*

**Assistant:** *(Checks memory cache for previous ICU nurse searches, then queries talent-kb MCP for real-time results)*

| Rank | Candidate | Candidate ID | Role/Specialty | Location | Experience | Key Matches | Confidence/Score |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Jane Miller | RN-1024 | ICU Nurse | Dallas, TX | 7 years | ICU, ACLS, ventilator care | 0.93 |
| 2 | Sam Patel | RN-2210 | ICU Nurse | Austin, TX | 6 years | ICU, ACLS, CCRN | 0.89 |

Notes:
- Search criteria used: ICU Nurse, 5+ years, ACLS certification.
- Result retrieved from: 1 cached + 1 real-time result.
- Add location or availability constraints to narrow the shortlist.
