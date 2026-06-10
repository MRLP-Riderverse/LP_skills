---
name: find-nearby
description: Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, cities, zip codes, or Telegram location pins. No API keys needed.
version: 1.0.0
metadata:
  hermes:
    tags: [location, maps, nearby, places, restaurants, local]
    related_skills: []
---

# Find Nearby — Local Place Discovery

Find restaurants, cafes, bars, pharmacies, and other places near any location. Uses OpenStreetMap (free, no API keys). Works with:

- **Coordinates** from Telegram location pins (latitude/longitude in conversation)
- **Addresses** ("near 123 Main St, Springfield")
- **Cities** ("restaurants in downtown Austin")
- **Zip codes** ("pharmacies near 90210")
- **Landmarks** ("cafes near Times Square")

## Quick Reference

```bash
# By coordinates (from Telegram location pin or user-provided)
python3 SKILL_DIR/scripts/find_nearby.py --lat <LAT> --lon <LON> --type restaurant --radius 1500

# By address, city, or landmark (auto-geocoded)
python3 SKILL_DIR/scripts/find_nearby.py --near "Times Square, New York" --type cafe

# Multiple place types
python3 SKILL_DIR/scripts/find_nearby.py --near "downtown austin" --type restaurant --type bar --limit 10

# JSON output
python3 SKILL_DIR/scripts/find_nearby.py --near "90210" --type pharmacy --json
```

### Parameters

| Flag | Description | Default |
|------|-------------|---------|
| `--lat`, `--lon` | Exact coordinates | — |
| `--near` | Address, city, zip, or landmark (geocoded) | — |
| `--type` | Place type (repeatable for multiple) | restaurant |
| `--radius` | Search radius in meters | 1500 |
| `--limit` | Max results | 15 |
| `--json` | Machine-readable JSON output | off |

### Common Place Types

`restaurant`, `cafe`, `bar`, `pub`, `fast_food`, `pharmacy`, `hospital`, `bank`, `atm`, `fuel`, `parking`, `supermarket`, `convenience`, `hotel`

## Workflow

1. **Get the location.** Look for coordinates (`latitude: ... / longitude: ...`) from a Telegram pin, or ask the user for an address/city/zip.

2. **Ask for preferences** only if needed: place type, max distance, budget, "open now", accessibility, tent/RV preference, etc.

3. **Run the script** with appropriate flags. Use `--json` if you need to process results programmatically.

4. **For lodging / camping / venue matching**, verify the amenity on the source site when possible:
   - confirm tent sites, RV-only rules, cabin options, or age restrictions from the campground site
   - if the site is JS-heavy or returns weak snippets, use search snippets plus the page HTML text rather than assuming from the title alone
   - when comparing options near an event or transit hub, gather candidate venues first, then estimate drive time / distance to the user’s target using routing

5. **Present results** with names, distance, and a short reason why each matches the request. If the user asked about hours or "open now," check the `hours` field in results — if missing or unclear, verify with `web_search`.

6. **For directions**, use the `directions_url` from results, or construct: `https://www.google.com/maps/dir/?api=1&origin=<LAT>,<LON>&destination=<LAT>,<LON>`

## Tips

- If results are sparse, widen the radius (1500 → 3000m)
- For "open now" requests: check the `hours` field in results, cross-reference with `web_search` for accuracy since OSM hours aren't always complete
- Zip codes alone can be ambiguous globally — prompt the user for country/state if results look wrong
- The script uses OpenStreetMap data which is community-maintained; coverage varies by region
- If a geocoder is blocked or rate-limited, try an alternate free geocoder before giving up; in one successful workflow, Photon returned usable results after Nominatim was blocked
- For travel-time estimates, OSRM is a good no-key fallback when you only need approximate driving distance/time between a candidate place and a landmark or transit station
