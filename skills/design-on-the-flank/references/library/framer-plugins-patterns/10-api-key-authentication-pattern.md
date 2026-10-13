[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## API Key Authentication Pattern

Simpler alternative (not explicitly in official examples, but used by community plugins):

```typescript
// Validate before persisting
async function validateApiKey(key: string): Promise<boolean> {
    try {
        const res = await fetch(`https://api.example.com/test?key=${key}`)
        return res.ok
    } catch {
        return false
    }
}

// Store in localStorage (per-user, sandboxed)
function saveCredentials(apiKey: string, sourceId: string) {
    localStorage.setItem("apiKey", apiKey)
    localStorage.setItem("sourceId", sourceId)
}
```

---


<!-- END SOURCE CONTENT -->
