---
name: publish_candidates_pr
description: Commits generated candidate profiles to the talent-knowledge-base repo and raises a Pull Request using the GitHub MCP server.
---

# Skill: Publish Candidate Profiles via PR

## Context
You are an AI assistant helping engineering and recruitment teams automate the ingestion of synthetic candidate data. Your job is to take locally generated PDF profiles and publish them to a central GitHub repository via a Pull Request.

## Triggers
Use this skill whenever the user explicitly asks to:
- Raise a PR for the generated candidates.
- Publish the candidate profiles to GitHub.
- Upload the PDFs to the talent knowledge base.

## Execution Rules
1. **Locate & Read Files:** Scan the project folder at `/tmp-output/generate_nursing_candidates/` (including all specialty subdirectories) and use the local file reader to get the contents of the newly generated PDF candidate profiles.
2. **Branch Creation (`create_branch`):** - Owner: `agent-runtime-labs`
   - Repo: `talent-knowledge-base`
   - Create a new, unique branch off the `main` branch. Use a naming convention like `feat/add-nursing-profiles-<timestamp>`.
3. **Commit Files (`push_files`):** - Push the PDF files to the newly created branch.
   - Map the files so the target path inside the repository is: `docs/profiles/<specialty>/<filename>.pdf`.
   - Use a clear commit message like: "docs: add synthetic nursing candidate profiles".
4. **Raise Pull Request (`create_pull_request`):** - Open a Pull Request from your new branch (`head`) against the `main` branch (`base`).
   - Title the PR: "Add New Synthetic Candidate Profiles".
   - In the PR body, list the names or IDs of the candidates being added so reviewers know exactly what is included.

## Output Formatting
- Provide a brief confirmation that the files were read locally.
- Provide the exact name of the newly created branch.
- Output the direct URL to the created Pull Request so the user can easily click and review it.

## Example Interaction
**User:** Can you raise a PR with all the candidates present under the tmp-output folder?
**Assistant:** Sure, I am on it.

*(Scans local folder, creates branch, pushes files, and creates PR)*

I have successfully committed the candidate profiles and raised the Pull Request. 
- **Repository:** agent-runtime-labs/talent-knowledge-base
- **Branch:** feat/add-nursing-profiles-16890234
- **PR Link:** https://github.com/agent-runtime-labs/talent-knowledge-base/pull/42

The files have been uploaded to the `docs/profiles/` folder in the repository. Let me know if you need any updates to the PR description!