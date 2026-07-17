---
name: ghostty-theme-creation
description: Create custom color themes for Ghostty terminal emulator with proper file structure and palette syntax.
category: devops
---

# Ghostty Theme Creation Skill

## When to Use This Skill

Use this skill when you need to:
- Create custom color themes for Ghostty terminal emulator
- Convert color palettes from other terminals to Ghostty format
- Fix theme loading errors in Ghostty
- Create multiple theme variants for a branding system

## Critical Format Requirements

### ✅ CORRECT: Ghostty Theme File Format

Ghostty themes must use **individual palette lines**, NOT array syntax:

```ini
# Theme file: ~/.config/ghostty/themes/my-theme
background = #0c0818
foreground = #c4b4d4
cursor-color = #7acc54
cursor-text = #0c0818
selection-background = #6444a0
selection-foreground = #ffffff

# 16-color palette (CORRECT format)
palette = 0=#0c0818
palette = 1=#7acc54
palette = 2=#6444a0
palette = 3=#c4b4d4
palette = 4=#4a90e2
palette = 5=#f5c54c
palette = 6=#160030
palette = 7=#c4b4d4
palette = 8=#1a1230
palette = 9=#7acc54
palette = 10=#6444a0
palette = 11=#c4b4d4
palette = 12=#4a90e2
palette = 13=#f5c54c
palette = 14=#160030
palette = 15=#ffffff
```

### ❌ WRONG: Array Syntax (Will Fail)

```ini
# DO NOT USE - This causes "config error - couldn't load"
palette = [
  #0c0818, #7acc54, #6444a0, ...
]
```

## File Structure

Themes must be placed in the correct directory:

```
~/.config/ghostty/
├── config              # Main config with: theme = "my-theme"
└── themes/
    ├── my-theme        # Theme file (no .conf extension)
    ├── my-theme-dark
    └── my-theme-light
```

## Step-by-Step Workflow

### 1. Create Theme File

```bash
# Create themes directory if it doesn't exist
mkdir -p ~/.config/ghostty/themes

# Create theme file
cat > ~/.config/ghostty/themes/lp64-atomic-purple << 'EOF'
background = #0c0818
foreground = #c4b4d4
cursor-color = #7acc54
cursor-text = #0c0818

palette = 0=#0c0818
palette = 1=#7acc54
palette = 2=#6444a0
palette = 3=#c4b4d4
palette = 4=#4a90e2
palette = 5=#f5c54c
palette = 6=#160030
palette = 7=#c4b4d4
palette = 8=#1a1230
palette = 9=#7acc54
palette = 10=#6444a0
palette = 11=#c4b4d4
palette = 12=#4a90e2
palette = 13=#f5c54c
palette = 14=#160030
palette = 15=#ffffff
EOF
```

### 2. Update Main Config

Add to `~/.config/ghostty/config`:

```ini
theme = "lp64-atomic-purple"
```

### 3. Reload Ghostty

- Press `Ctrl+Shift+,` (comma) in Ghostty, OR
- Close and reopen Ghostty

## Common Pitfalls

### 1. Array Syntax Error
**Problem:** Using `palette = [...]` causes "config error - couldn't load"  
**Solution:** Use individual `palette = N=#color` lines

### 2. Wrong Directory
**Problem:** Theme files in `~/.config/ghostty/` root instead of `themes/` subdirectory  
**Solution:** Place theme files in `~/.config/ghostty/themes/`

### 3. Theme Name Mismatch
**Problem:** Config says `theme = "my-theme"` but file is `mytheme` (no dash)  
**Solution:** Ensure theme name in config matches filename exactly

### 4. Missing Required Colors
**Problem:** Theme loads but colors look wrong  
**Solution:** Define all 16 palette colors (0-15) plus background/foreground

## Color Palette Reference

Standard 16-color ANSI palette mapping:

| Index | Name          | Typical Use        |
|-------|---------------|--------------------|
| 0     | black         | Background         |
| 1     | red           | Errors/strings     |
| 2     | green         | Success/prompts    |
| 3     | yellow        | Warnings           |
| 4     | blue          | Paths/keywords     |
| 5     | magenta       | Types/classes      |
| 6     | cyan          | Variables          |
| 7     | white         | Text               |
| 8-15  | bright variants | Bold/highlighted |

## Verification Steps

1. **Check file exists:**
   ```bash
   ls -la ~/.config/ghostty/themes/
   ```

2. **Verify format (no array syntax):**
   ```bash
   grep -E "^palette = \[" ~/.config/ghostty/themes/* && echo "ERROR: Array syntax found"
   ```

3. **Test theme loads:**
   ```bash
   ghostty +show-config --theme=your-theme 2>&1 | grep -i error
   ```

4. **Check current theme in config:**
   ```bash
   grep "^theme" ~/.config/ghostty/config
   ```

## Example: Creating Multiple Theme Variants

```bash
# Create theme switcher script
cat > ~/.local/bin/ghostty-theme << 'EOF'
#!/usr/bin/env bash
THEME_NAME="$1"
THEMES_DIR="$HOME/.config/ghostty/themes"

if [ -z "$THEME_NAME" ]; then
    echo "Usage: ghostty-theme <name>"
    echo "Available: $(ls $THEMES_DIR)"
    exit 1
fi

if [ ! -f "$THEMES_DIR/$THEME_NAME" ]; then
    echo "Theme not found: $THEME_NAME"
    exit 1
fi

sed -i "s/^theme = .*/theme = \"$THEME_NAME\"/" ~/.config/ghostty/config
echo "Switched to theme: $THEME_NAME"
echo "Reload Ghostty config (Ctrl+Shift+,) to apply"
EOF

chmod +x ~/.local/bin/ghostty-theme
```

## Related Skills

- `lp64-terminal-design` - LP64 aesthetic specifications
- `terminal-color-schemes` - General terminal color theory
- `ghostty-configuration` - Broader Ghostty configuration patterns

## Resources

- Ghostty Config Docs: https://ghostty.org/docs/config
- Theme Examples: https://github.com/ghostty-org/ghostty/tree/main/config
- Color Palette Picker: https://ghostty.org/docs/config#theme
