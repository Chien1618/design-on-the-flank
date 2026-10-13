[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Error Resilience with Promise.allSettled

Don't let one failed item abort the entire sync:

```typescript
const results = await Promise.allSettled(promises)
const items: CollectionItem[] = []
const errors: SyncError[] = []

results.forEach((result, index) => {
    if (result.status === "fulfilled" && result.value !== null) {
        items.push(result.value)
    } else if (result.status === "rejected") {
        errors.push({ index, error: result.reason })
    }
})

// Sync whatever succeeded, report errors
await collection.addItems(items)
if (errors.length > 0) {
    framer.notify(`Synced with ${errors.length} errors`, { variant: "warning" })
}
```

---


<!-- END SOURCE CONTENT -->
