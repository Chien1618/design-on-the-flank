[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Slug Generation

All official plugins use this identical slugify function:

```typescript
function slugify(value: string): string {
    return value
        .toLowerCase()
        .replace(/[^\p{Letter}\p{Number}()]+/gu, "-")
        .replace(/^-+|-+$/gu, "")
}
```

**Slugs must be unique** within a collection. The Airtable plugin validates this:

```typescript
const seenSlugs = new Set<string>()
for (const item of items) {
    if (seenSlugs.has(item.slug)) throw new Error(`Duplicate slug: ${item.slug}`)
    seenSlugs.add(item.slug)
}
```

---


<!-- END SOURCE CONTENT -->
