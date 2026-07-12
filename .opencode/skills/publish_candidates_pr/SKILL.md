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
1. **Locate & Read Files:** Scan the project folder at `/tmp/automation-hub/generate_nursing_candidates/` (including all specialty subdirectories) and use bash to locate all PDF files.
2. **Clone Repository and Create Branch (Using Git for Binary Files):** 
    - Clone the repository: `git clone https://github.com/agent-runtime-labs/talent-knowledge-base.git /tmp/talent-kb-temp`
    - Create and checkout a new branch with timestamp: `git checkout -b feat/add-nursing-profiles-binary-$(date +%s)`
    - **IMPORTANT:** Use git push for binary files instead of API encoding. Git handles PDFs natively without corruption.
3. **Copy Files to Repository Structure:** 
    - Create the target directory structure: `mkdir -p docs/profiles/<specialty>/`
    - Copy all PDF files from `/tmp/automation-hub/generate_nursing_candidates/<specialty>/` to `docs/profiles/<specialty>/`
    - Map the files so the target path inside the repository is: `docs/profiles/<specialty>/<filename>.pdf`.
4. **Commit and Push (Using Git):** 
    - Stage all files: `git add docs/profiles/`
    - Commit with a clear message: `git commit -m "docs: add synthetic nursing candidate profiles"`
    - Push to remote: `git push origin HEAD`
    - This approach ensures PDFs remain intact as binary files.
5. **Raise Pull Request (`create_pull_request`):** 
    - Use the `github_create_pull_request` tool to open a PR.
    - Set `head` to the newly created branch (e.g., `feat/add-nursing-profiles-binary-<timestamp>`)
    - Set `base` to `main`
    - Title the PR: "Add New Synthetic Candidate Profiles".
    - In the PR body, list the names or IDs of the candidates being added so reviewers know exactly what is included.

## Output Formatting
- Provide a brief confirmation that the files were read locally.
- Show the exact filenames and their target paths in the repository.
- Provide the exact name of the newly created branch.
- Output the direct URL to the created Pull Request so the user can easily click and review it.
- **Verification tip:** After the PR is created, suggest the user verify by checking one of the PDFs can be opened in the PR diff preview on GitHub.

## Example Interaction
**User:** Can you raise a PR with all the candidates present under the tmp-output folder?
**Assistant:** Sure, I am on it.

*(Scans local folder, creates branch, pushes files, and creates PR)*

I have successfully committed the candidate profiles and raised the Pull Request. 
- **Repository:** agent-runtime-labs/talent-knowledge-base
- **Branch:** feat/add-nursing-profiles-16890234
- **PR Link:** https://github.com/agent-runtime-labs/talent-knowledge-base/pull/42

The files have been uploaded to the `docs/profiles/` folder in the repository. Let me know if you need any updates to the PR description!

## Troubleshooting Binary File Issues

If PDFs do not push correctly to GitHub:

1. **Verify local PDF integrity:** `file /tmp/automation-hub/generate_nursing_candidates/ICU_Nurse/*.pdf` should show "PDF document"
2. **Verify git push succeeded:** Check that `git push origin HEAD` completes without errors
3. **Check GitHub credentials:** Ensure git is configured with valid GitHub credentials or SSH keys: `git config --list | grep github`
4. **Verify branch was created:** Confirm the remote branch exists: `git branch -r | grep feat/add-nursing-profiles`
5. **Inspect file on GitHub:** After PR creation, navigate to the PR and click on the Files Changed tab to verify the PDF is listed and can be previewed