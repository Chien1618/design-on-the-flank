[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ProtectedMethod — Known Values

```typescript
type ProtectedMethod =
    // ManagedCollection
    | "ManagedCollection.addItems"
    | "ManagedCollection.removeItems"
    | "ManagedCollection.setFields"
    | "ManagedCollection.setPluginData"
    // Collection (non-managed)
    | "Collection.addItems"
    | "Collection.addFields"
    | "Collection.removeFields"
    // Nodes
    | "Node.setAttributes"
    // Canvas
    | "addImage"
    | "setImage"
    | "addText"
```

"Get" methods (getItemIds, getFields, getPluginData, etc.) do NOT require permission checks.

---


<!-- END SOURCE CONTENT -->
