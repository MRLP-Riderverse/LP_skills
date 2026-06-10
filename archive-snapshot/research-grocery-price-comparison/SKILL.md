---
name: grocery-price-comparison
description: Compare grocery prices across local Canadian chains using Instacart store pages and dynamic page scraping. Use when the user asks which store has the best price for a specific item (e.g. eggs, milk, bread) and the stores have public online listings.
---

# Grocery Price Comparison via Instacart

Use this workflow when a user asks for the cheapest price across local grocery chains and you need current, store-specific pricing.

## Best use case
- Comparing prices for a specific item across multiple chains
- Local Canadian grocery stores that expose products through Instacart
- When the user wants a practical recommendation, not a generic guess

## Workflow

1. Identify the relevant store slugs.
   - Common Bathurst NB / Atlantic Canada slugs I’ve verified:
     - Walmart: `walmart-canada`
     - Sobeys: `sobeys`
     - Atlantic Superstore: `atlantic-superstore`
     - No Frills: `no-frills-can`
   - If the slug is unknown, search the web for `site:instacart.ca/store <store name> <item>`.

2. Load each store search page with a query for the item.
   - Example: `https://www.instacart.ca/store/walmart-canada/s?k=eggs`
   - Use a headless browser or Playwright, not just a static fetch, because the page content is rendered dynamically.

3. Wait for the page to render product cards.
   - `networkidle` can be too slow or never settle.
   - Prefer `domcontentloaded` plus a short wait (about 8–15 seconds) before reading the body text.

4. Extract current prices from visible text.
   - The page usually includes lines like `Current price: $4.13`.
   - Read the `body` text and pair `Current price` lines with the next product title/size lines.

5. Compare like-for-like products.
   - Prefer the cheapest standard carton, usually `12 ct` or `18 ct` depending on the user’s intent.
   - Exclude odd items unless the user explicitly wants all egg products.
   - Watch for misleading rows such as sponsored items, promo bundles, or `1 each` entries.

6. Report the result clearly.
   - Name the cheapest store/item combination found.
   - Also mention the cheapest “basic large eggs” option separately if the lowest overall item is a specialty egg.
   - If one or more stores do not have public listings, say so instead of guessing.

## Pitfalls
- Store slugs are not always obvious; `superstore` may 404, while `atlantic-superstore` works.
- `networkidle` can hang on Instacart pages; use a fixed wait after `domcontentloaded`.
- Some pages show prices in compact text (`$413`) right next to the readable version (`Current price: $4.13`). Use the readable one.
- Some stores may not have a usable public database for smaller local chains; don’t fabricate coverage.

## Output suggestion
- Best overall price: <store> — <item> — <price>
- Best basic carton: <store> — <item> — <price>
- Unverified stores: <store names>
