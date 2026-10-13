[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Plugin Data Keys Pattern

Store sync state on the collection so it persists across users:

```typescript
const PLUGIN_KEYS = {
    SOURCE_ID: "pluginSourceId",
    SLUG_FIELD_ID: "pluginSlugFieldId",
    LAST_SYNCED: "pluginLastSynced",
    TABLE_NAME: "pluginTableName",
} as const

// Write after sync:
await collection.setPluginData(PLUGIN_KEYS.SOURCE_ID, sourceId)
await collection.setPluginData(PLUGIN_KEYS.LAST_SYNCED, new Date().toISOString())

// Read at startup:
const previousSourceId = await collection.getPluginData(PLUGIN_KEYS.SOURCE_ID)
```

---


<!-- END SOURCE CONTENT -->
