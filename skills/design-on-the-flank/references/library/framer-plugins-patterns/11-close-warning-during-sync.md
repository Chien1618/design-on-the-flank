[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Close Warning During Sync

Prevent accidental close during long operations (from Notion plugin):

```typescript
async function syncWithWarning(collection: ManagedCollection) {
    try {
        await framer.setCloseWarning("Sync in progress. Closing will cancel the sync.")
        await performSync(collection)
        framer.closePlugin("Sync complete", { variant: "success" })
    } catch (error) {
        if (error instanceof FramerPluginClosedError) return
        throw error
    } finally {
        await framer.setCloseWarning(false)
    }
}
```

---


<!-- END SOURCE CONTENT -->
