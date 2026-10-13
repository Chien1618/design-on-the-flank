[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ManagedCollectionFieldInput

```typescript
interface ManagedCollectionFieldInput {
    id: string                              // Stable identifier, used in fieldData keys
    name: string                            // Display name in Framer CMS
    type: CollectionFieldType
    userEditable?: boolean                  // Default false for managed collections.
                                            // If true, user can edit this field in CMS UI
                                            // and sync won't overwrite it.

    // Type-specific properties:
    cases?: { id: string; name: string }[]  // Required for "enum"
    collectionId?: string                   // Required for "collectionReference" / "multiCollectionReference"
    allowedFileTypes?: string[]             // Optional for "file"
    fields?: ManagedCollectionFieldInput[]  // Required for "array" (gallery sub-fields)
}
```

### CollectionFieldType — All Values

```typescript
type CollectionFieldType =
    | "boolean"
    | "color"
    | "number"
    | "string"
    | "formattedText"
    | "image"
    | "file"
    | "link"
    | "date"
    | "enum"
    | "collectionReference"
    | "multiCollectionReference"
    | "array"
    | "divider"
    | "unsupported"
```

---


<!-- END SOURCE CONTENT -->
