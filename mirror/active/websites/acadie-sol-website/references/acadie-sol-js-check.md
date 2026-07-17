# Acadie.sol JS Verification Script

The following one‑liner can be run from the project root to catch syntax errors in all HTML‑embedded script tags:

```bash
for html in *.html; do
  node -e \"const fs=require('fs'); const c=fs.readFileSync('$html','utf8'); 
  const scripts=c.match(/<script>[\\s\\S]*?<\\/script>/g); 
  if(scripts) scripts.forEach((s,i)=>{try{new Function(s.replace(/<\\/?script>/g,''))}catch(e){console.error('$html script'+i+':',e.message)};})\"; 
done
```

It loops over each `.html` file, extracts the contents of each `<script>` block, strips the script tags, and attempts to create a Function from the body. Any `SyntaxError` is printed with the file and script index.

**Usage**: Save as `scripts/check-js.sh` (make executable) or paste directly into a terminal. A clean run prints nothing; errors appear as shown above.

**Why this works**: It avoids loading the page in a browser, giving a fast syntax gate before you even start the local server.