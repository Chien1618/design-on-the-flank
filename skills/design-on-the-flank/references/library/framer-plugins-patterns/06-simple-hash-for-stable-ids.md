[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Simple Hash for Stable IDs

When the data source doesn't have stable IDs (e.g., RSS feeds), generate them:

```typescript
function simpleHash(input: string): string {
    let hash = 0
    for (let i = 0; i < input.length; i++) {
        const char = input.charCodeAt(i)
        hash = (hash << 5) - hash + char
        hash = hash & hash
    }
    return Math.abs(hash).toString(16).padStart(8, "0")
}
```

---


<!-- END SOURCE CONTENT -->
