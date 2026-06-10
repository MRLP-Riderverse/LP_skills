---
name: skill-directory-reorganization
description: Safely reorganize Hermes skill directories while preserving functionality and updating internal references. Use when skill directory names are confusing or when better categorization by context/use case is needed.
version: 1.0.0
author: MidnightRider.sol
license: MIT
metadata:
  hermes:
    tags: [Skill Management, Directory Organization, Refactoring, Hermes Agent]
    related_skills: []
---

# Hermes Skill Directory Reorganization

## Description
Safely reorganize Hermes skill directories while preserving functionality and updating internal references. This skill provides a systematic approach to renaming skill directories (e.g., for clearer naming conventions) while ensuring that all dependent systems (cron jobs, scripts, references) continue to function correctly.

## When to Use
- Skill directory names are unclear or don't adequately describe their context/use case
- You want to reorganize skills by context rather than just function (e.g., grouping by location, use case, or environment)
- Skill directory names cause confusion in workflows or documentation
- Preparing skills for better discoverability and organization
- You've renamed directories and need to update internal references

## Approach
1. **Planning**: Identify the directories to rename and their new names
2. **Verification**: Confirm source directories exist and destinations don't already exist
3. **Execution**: Perform directory renames using `mv` command
4. **Reference Updates**: Update internal references in skill files (SKILL.md) to point to new directory paths
5. **Validation**: Verify that dependent systems still work (cron jobs, scripts, Telegram delivery)
6. **Documentation**: Update any relevant documentation or notes

## Key Files Typically Affected
- Skill directories being renamed (and their contents)
- SKILL.md files within those directories (may contain path references)
- Cron jobs that reference scripts in those directories
- Any custom scripts or tools that reference the old paths
- The .hub directory in ~/.hermes/skills/ (contains metadata about installed skills)

## Step-by-Step Procedure

### 1. Plan the Renames
```bash
# List current directories to confirm what exists
ls -la ~/.hermes/skills/

# Define your rename mapping
# Example: weather-tool → weatherAPI-home
#          weather-one-shot → weatherAPI-not-home
```

### 2. Execute the Renames
```bash
# For each directory to rename:
OLD_PATH="~/.hermes/skills/old-name"
NEW_PATH="~/.hermes/skills/new-name"

# Verify source exists
if [ -d "$OLD_PATH" ]; then
  # Verify destination doesn't exist to avoid overwriting
  if [ ! -d "$NEW_PATH" ]; then
    mv "$OLD_PATH" "$NEW_PATH"
    echo "Renamed: $OLD_PATH → $NEW_PATH"
  else
    echo "Error: Destination $NEW_PATH already exists"
  fi
else
  echo "Error: Source $OLD_PATH does not exist"
fi
```

### 3. Update Internal References
After renaming directories, update any SKILL.md files that reference the old paths:

```bash
# Example: Update references in the moved skill file
SKILL_FILE="~/.hermes/skills/new-name/SKILL.md"

# Replace old path references with new ones
sed -i 's|~/.hermes/skills/old-name/|~/.hermes/skills/new-name/|g' "$SKILL_FILE"

# Verify the changes
grep "new-name" "$SKILL_FILE"
```

### 4. Validate System Integrity
```bash
# Check that cron jobs still list correctly
hermes cron list

# Test that key scripts still execute
python3 ~/.hermes/skills/weatherAPI-home/bathurst_weather.py  # Example

# Verify Telegram delivery still works (if applicable)
# Trigger a manual cron run and check output
hermes cron run <job-id>
```

## Constants to Modify for Your Use Case
- `OLD_PATH`: The current directory path to rename
- `NEW_PATH`: The new directory path
- `SKILL_FILE`: Path to the SKILL.md file that needs updating
- `OLD_REFERENCE`: The old path string to replace in files (e.g., `~/.hermes/skills/weather-tool/`)
- `NEW_REFERENCE`: The new path string to use as replacement (e.g., `~/.hermes/skills/weatherAPI-home/`)

## Performance Notes
- Directory renames are instantaneous filesystem operations
- The main time investment is in verification and updating references
- For skills with many internal references, consider using automated search/replace tools
- Always validate after changes to catch broken references early

## Example Usage
Reorganizing weather skills for clearer context separation:

```bash
# Rename directories
mv ~/.hermes/skills/weather-tool ~/.hermes/skills/weatherAPI-home
mv ~/.hermes/skills/weather-one-shot ~/.hermes/skills/weatherAPI-not-home

# Update skill file references
sed -i 's|~/.hermes/skills/weather-tool/|~/.hermes/skills/weatherAPI-home/|g' \
  ~/.hermes/skills/weatherAPI-not-home/SKILL.md

# Validate
hermes cron list  # Confirm weather job still appears
python3 ~/.hermes/skills/weatherAPI-home/bathurst_weather.py  # Confirm script works
```

## Notes
- Always back up or verify you can recover before making changes (though Hermes skills are generally recoverable)
- When updating references in SKILL.md files, be careful to only update path references, not the skill name/description
- The skill name (in SKILL.md frontmatter) should describe the function, while the directory name can describe context/use case
- After reorganization, consider updating any personal memory or notes that reference the old paths
- For complex reorganizations with multiple interdependent skills, plan the update order carefully

## Author
MidnightRider.sol