# Directory Card Lookup — Response Shapes

## Clear match

```text
Found draft card for: Eastside Deli
Path: /.../inbox/eastside-deli.md

# Draft: Eastside Deli
...
```

## Ambiguous match

```text
Possible cards found for: Big D
- [draft] Big D Drive-in — /.../inbox/big-d-drive-in.md
- [draft] Big Deal Market — /.../inbox/big-deal-market.md
```

## Deterministic command

```bash
python3 scripts/lookup_cards.py "<query>" --root /home/midnight/ExoCortex/websites/projects/acadie_sol_directory --format json
```
