---
name: python-user-packages
description: Handle Python user site-packages access in Hermes skills for dependency resolution
version: 1.0.0
author: MidnightRider.sol
license: MIT
metadata:
  hermes:
    tags: [Python, Dependencies, Site-Packages, Environment]
    related_skills: []
---

# Python User Packages Skill

## Description
Provides a reliable method for Hermes skills to access Python packages installed in the user's site-packages directory, which is often where packages are installed when the Hermes Agent's virtual environment doesn't have write access to its own site-packages.

## When to Use
- When a skill needs to import Python packages that are installed in the user's site-packages (e.g., via `pip install --user`)
- When the Hermes Agent's virtual environment doesn't have access to required dependencies
- For skills that need to work reliably across different Hermes installations and environments
- When encountering `ModuleNotFoundError` for packages that are actually installed

## Approach
1. Detect the user's site-packages directory
2. Add it to `sys.path` if not already present
3. Import required modules
4. Handle import errors gracefully

## Key Files
- Reference implementation: See `qr-code-generator` skill's `__init__.py`
- Pattern can be reused in any skill needing user site-packages access

## Constants to Customize
- `USER_SITE_PATH`: Typically `/home/{username}/.local/lib/python{X.Y}/site-packages`
- Adjust based on actual Python version and username

## Implementation Pattern
```python
import sys
import os

# Add user site-packages to Python path
USER_SITE = "/home/midnight/.local/lib/python3.10/site-packages"
if USER_SITE not in sys.path:
    sys.path.insert(0, USER_SITE)

# Now import your modules
import qrcode  # or whatever module you need
```

## Verification
- Test that the import works after adding the path
- Handle cases where the path doesn't exist or modules aren't available
- Provide clear error messages for troubleshooting

## Example Usage in Skills
This pattern is used in the `qr-code-generator` skill to reliably access the `qrcode`, `segno`, and `Pillow` packages installed in the user's site-packages directory.

## Author
MidnightRider.sol