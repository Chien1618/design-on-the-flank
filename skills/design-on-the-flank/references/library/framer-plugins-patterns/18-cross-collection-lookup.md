[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Cross-Collection Lookup

Notion plugin scans all collections to find linked databases:

```typescript
async function getExistingDatabaseMap(): Promise<Map<string, string>> {
    const map = new Map<string, string>()
    for (const collection of await framer.getCollections()) {
        const dbId = await collection.getPluginData("databaseId")
        if (dbId) map.set(dbId, collection.id)
    }
    return map
}
```

<!-- END SOURCE CONTENT -->
