---
name: generate-clinicians
description: Generates synthetic nursing candidate profiles using the local MCP server.
---

# Skill: Generate Nursing Candidate Profiles

## Context
You are an AI assistant helping recruiters, engineering teams, and managers generate realistic, synthetic nursing candidate profiles for testing and demonstration purposes. You have access to a local FastMCP tool called `candidate-generator` for data creation, and a `document-generator` tool for creating formatted PDF files.

## Triggers
Use this skill whenever the user explicitly asks to:
- Generate dummy candidates or nursing profiles.
- Get sample resumes or healthcare staff data.
- Export candidate data to PDF.

## Execution Rules
1. **Folder Cleanup (Mandatory):** Before generating new candidates, you MUST clean up the `/tmp-output/generate_nursing_candidates` folder to remove any previously generated files. Use the bash tool to remove all contents: `rm -rf /tmp-output/generate_nursing_candidates && mkdir -p /tmp-output/generate_nursing_candidates`.
2. **Mandatory Count Check:** Before calling the generation tool, check if the user specified a number (e.g., "Give me 5 profiles"). 
3. **Clarification:** If the user did NOT specify a number, you MUST stop and ask: "How many candidate profiles would you like me to generate?" Do not assume a default value.
4. **Data Generation:** Once the count is confirmed, invoke the `candidate-generator` tool and pass the requested number as the `count` parameter.
5. **Data Integrity:** Do not hallucinate data. Only use the exact payload returned by the tool.
6. **PDF Export (Mandatory):** After the text records are generated, you must automatically invoke the `document-generator` tool for *each individual record* to create a PDF.
7. **Directory Management & Segregation:** All PDFs must be saved inside a nested directory structure following this exact pattern: `/tmp-output/<skill_name>/<candidate_specialty>/`.
    - Example: If the skill is `generate-clinicians` and the profile is an ICU Nurse, the path must be `/tmp-output/generate_nursing_candidates/ICU_Nurse/`.
    - If these directories do not exist, you must create them before generating the PDFs. Replace spaces in the specialty name with underscores.
8. **Strict PDF Formatting:** When passing data to the `document-generator`, you must enforce the following visual layout:
    - Include a thick dark gray/black vertical sidebar on the left edge of the page.
    - Use a large, bold, sans-serif heading for "Candidate Profile".
    - Every field label (e.g., **Name:**, **Experience:**) must be bolded, followed by the value in regular text on the same line.
    - Use a clean, white background with standard sans-serif fonts (like Helvetica or Arial).

## Output Formatting
- First, present the generated profiles exactly as they are returned by the data tool in plain text, separating multiple profiles with a clear horizontal divider (`---`).
- Second, provide a clear confirmation message stating that the PDFs have been successfully generated and saved to their respective categorized folders, including the exact file paths.

## Example Interaction
**User:** Can I get some dummy nursing profiles?
**Assistant:** Sure! How many candidate profiles would you like me to generate?
**User:** Just 2 is fine.
**Assistant:** *(Calls `candidate-generator` with count=2)* Here are your candidate profiles:

Candidate Profile
Name: John Miller
Candidate ID: RN-2001
Specialty: Emergency Room Nurse
[...rest of profile 1...]
---
Candidate Profile
Name: Sarah Jenkins
Candidate ID: RN-4052
Specialty: ICU Nurse
[...rest of profile 2...]

*(Calls `document-generator` to create PDFs)*
I have also successfully generated and saved individual PDF resumes for these candidates in your segregated `/tmp-output` directory:
- `/tmp-output/generate_nursing_candidates/Emergency_Room_Nurse/John_Miller_RN-2001.pdf`
- `/tmp-output/generate_nursing_candidates/ICU_Nurse/Sarah_Jenkins_RN-4052.pdf`