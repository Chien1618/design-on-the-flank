[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Collection (Non-Managed)

For collections not owned by the plugin (user-editable collections):

```typescript
interface Collection {
    id: string
    name: string
    managedBy: "user" | string     // "user" for unmanaged, plugin ID for managed
    addFields(fields: CollectionFieldInput[]): Promise<void>
    addItems(items: CollectionItemInput[]): Promise<void>
    // ... other methods
}
```

Use `framer.getActiveCollection()` for the `collection` mode.

---


<!-- END SOURCE CONTENT -->
