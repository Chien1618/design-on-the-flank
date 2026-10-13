[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ManagedCollection

```typescript
interface ManagedCollection {
    id: string
    name: string

    // Items
    getItemIds(): Promise<string[]>
    addItems(items: ManagedCollectionItemInput[]): Promise<void>
    // Upsert: adds new items, updates existing items matched by id.
    removeItems(ids: string[]): Promise<void>
    setItemOrder(ids: string[]): Promise<void>

    // Fields
    getFields(): Promise<ManagedCollectionField[]>
    setFields(fields: ManagedCollectionFieldInput[]): Promise<void>
    // Replaces the entire field schema. Existing data for removed fields is lost.

    // Plugin Data (per-collection)
    setPluginData(key: string, value: string | null): Promise<void>
    getPluginData(key: string): Promise<string | null>
    // 2kB per entry, 4kB per collection. Strings only.

    // Activation
    setAsActive(): Promise<void>  // SDK 2.2.0+
}
```

---


<!-- END SOURCE CONTENT -->
