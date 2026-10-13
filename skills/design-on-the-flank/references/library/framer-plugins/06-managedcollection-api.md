[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ManagedCollection API

```typescript
interface ManagedCollection {
    id: string
    getItemIds(): Promise<string[]>
    setItemOrder(ids: string[]): Promise<void>
    getFields(): Promise<ManagedCollectionField[]>
    setFields(fields: ManagedCollectionFieldInput[]): Promise<void>
    addItems(items: ManagedCollectionItemInput[]): Promise<void>   // upsert!
    removeItems(ids: string[]): Promise<void>
    setPluginData(key: string, value: string | null): Promise<void>
    getPluginData(key: string): Promise<string | null>
}
```

**Critical**: `addItems()` is an **upsert** — it adds new items and updates existing ones matched by `id`.

### Field Types

```
"boolean" | "color" | "number" | "string" | "formattedText" |
"image" | "file" | "link" | "date" | "enum" |
"collectionReference" | "multiCollectionReference" | "array"
```

### Field Definition

```typescript
interface ManagedCollectionFieldInput {
    id: string
    name: string
    type: CollectionFieldType
    userEditable?: boolean        // default false for managed
    cases?: { id, name }[]       // for "enum"
    collectionId?: string         // for collection references
    fields?: ManagedCollectionFieldInput[]  // for "array" (gallery)
}
```

### Item Structure

```typescript
interface ManagedCollectionItemInput {
    id: string
    slug: string
    draft: boolean
    fieldData: Record<string, FieldDataEntryInput>
}
```

### Field Data Values — MUST specify type explicitly

```typescript
{ type: "string", value: "hello" }
{ type: "number", value: 42 }
{ type: "boolean", value: true }
{ type: "date", value: "2024-01-01T00:00:00Z" }   // ISO 8601
{ type: "link", value: "https://example.com" }
{ type: "image", value: "https://img.url" | null }
{ type: "file", value: "https://file.url" | null }
{ type: "color", value: "#FF0000" | null }
{ type: "formattedText", value: "<p>hello</p>", contentType: "html" }
{ type: "enum", value: "case-id" }
{ type: "collectionReference", value: "item-id" }
{ type: "multiCollectionReference", value: ["id1", "id2"] }
{ type: "array", value: [{ id: "1", fieldData: { ... } }] }
```


<!-- END SOURCE CONTENT -->
