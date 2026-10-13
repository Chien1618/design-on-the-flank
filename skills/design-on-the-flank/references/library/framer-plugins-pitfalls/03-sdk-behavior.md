[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## SDK Behavior

### "Invoking protected message type" toast warnings
`setPluginData()`, `addManagedCollectionItems()`, `setManagedCollectionFields()`, and other SDK methods trigger visible toast notifications saying "Invoking protected message type ... without checking permissions first."

**What it is**: A Framer SDK internal message-passing warning surfaced as a user-facing toast. NOT just a console warning — users see it.

**Workarounds:**
- For settings: use `localStorage` instead of `setPluginData()` to eliminate the toast entirely
- For collection operations (`addItems`, `setFields`): unavoidable — these are core sync APIs. Likely a Framer SDK bug that will be fixed.
- `console.warn` overrides do NOT suppress these toasts (they come from the SDK's internal layer, not `console`)

### closePlugin throws internally
`framer.closePlugin()` returns `never` and throws `FramerPluginClosedError`. Any code after it won't execute. The SDK auto-suppresses unhandled rejections of this class, but if you have a `catch` block:

```typescript
try {
    await syncCollection(collection)
    framer.closePlugin("Done", { variant: "success" })
} catch (error) {
    if (error instanceof FramerPluginClosedError) return  // Must ignore
    // Handle real errors
}
```

### addItems is upsert
`collection.addItems()` adds new items AND updates existing ones matched by `id`. You don't need to check whether an item already exists before adding it.

### Slug uniqueness is required
Items in a collection must have unique slugs. If two items share a slug, the sync may fail or produce unexpected results. Always validate before calling `addItems`.

---


<!-- END SOURCE CONTENT -->
