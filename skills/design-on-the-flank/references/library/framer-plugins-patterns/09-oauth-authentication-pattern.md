[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## OAuth Authentication Pattern

Used by Airtable, Google Sheets, Notion, HubSpot:

```typescript
class Auth {
    private TOKENS_KEY = "pluginTokens"

    async authorize(): Promise<Tokens> {
        // 1. Get auth URL from external worker
        const { authUrl, readKey } = await fetch("https://oauth.fetch.tools/my-plugin/authorize").then(r => r.json())
        // 2. Open browser for user to authorize
        window.open(authUrl)
        // 3. Poll for tokens
        return this.pollForTokens(readKey)
    }

    getTokens(): Tokens | null {
        const stored = localStorage.getItem(this.TOKENS_KEY)
        return stored ? JSON.parse(stored) : null
    }

    saveTokens(tokens: Tokens) {
        localStorage.setItem(this.TOKENS_KEY, JSON.stringify(tokens))
    }

    logout() {
        localStorage.removeItem(this.TOKENS_KEY)
        window.location.reload()
    }
}

export const auth = new Auth()
```

Tokens always go in `localStorage` (per-user, not shared).

---


<!-- END SOURCE CONTENT -->
