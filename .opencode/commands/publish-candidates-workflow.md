---
name: publish-candidates-workflow
description: End-to-end workflow to generate synthetic nursing candidate profiles and publish them to GitHub via Pull Request.
argument-hint: "<number of profiles>"
---

# Generate and Publish Candidate Profiles Workflow

This is a step-by-step workflow that:
1. **Step 1:** Generates synthetic nursing candidate profiles using the `generate-clinicians` skill
2. **Step 2:** Once generated, publishes those profiles to GitHub using the `publish_candidates_pr` skill

## Execution

The number of profiles to generate is: {{args}}

First, I'll load the `generate-clinicians` skill to create the profiles.

Then, I'll load the `publish_candidates_pr` skill to commit and raise a PR with those profiles.
