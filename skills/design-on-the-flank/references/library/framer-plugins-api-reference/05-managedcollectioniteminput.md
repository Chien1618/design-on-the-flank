[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ManagedCollectionItemInput

```typescript
interface ManagedCollectionItemInput {
    id: string                                      // Unique item identifier (used for upsert matching)
    slug: string                                    // URL slug, must be unique across collection
    draft: boolean                                  // true = draft, false = published
    fieldData: Record<string, FieldDataEntryInput>  // Keys are field IDs
}
```

---


<!-- END SOURCE CONTENT -->
