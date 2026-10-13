[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Sync Algorithm (Universal)

All official CMS plugins use the "unsynced items" pattern for full-replace sync:

```typescript
async function syncCollection(collection: ManagedCollection, items: ItemData[]) {
    const unsyncedItems = new Set(await collection.getItemIds())

    const collectionItems = items.map(item => {
        unsyncedItems.delete(item.id)  // Mark as still present
        return {
            id: item.id,
            slug: slugify(item.title),
            draft: false,
            fieldData: {
                title: { type: "string", value: item.title },
                // ... more fields
            },
        }
    })

    await collection.setFields(fields)
    await collection.removeItems(Array.from(unsyncedItems))  // Remove stale items
    await collection.addItems(collectionItems)                // Upsert current items
    await collection.setPluginData("sourceId", sourceId)
}
```

**Order**: `setFields` → `removeItems` (stale) → `addItems` (all current)

Since `addItems` is upsert, unchanged items just get updated in place.

---


<!-- END SOURCE CONTENT -->
