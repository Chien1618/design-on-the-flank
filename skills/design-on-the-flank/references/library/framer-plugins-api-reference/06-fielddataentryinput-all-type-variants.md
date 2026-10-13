[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## FieldDataEntryInput — All Type Variants

Every field value must explicitly declare its type. Never pass raw values.

```typescript
// Primitives
{ type: "string", value: string }
{ type: "number", value: number }
{ type: "boolean", value: boolean }

// Date — ISO 8601 string
{ type: "date", value: string | null }
// Example: "2024-06-15T10:30:00Z"

// Link — full URL
{ type: "link", value: string | null }

// Image — URL string or null
{ type: "image", value: string | null }

// File — URL string or null
{ type: "file", value: string | null }

// Color — hex string or null
{ type: "color", value: string | null }

// Formatted Text — HTML content
{ type: "formattedText", value: string, contentType?: "html" }

// Enum — value is the case ID (not display name)
{ type: "enum", value: string }

// Collection Reference — value is an item ID or slug from the referenced collection
{ type: "collectionReference", value: string }

// Multi Collection Reference — array of item IDs/slugs
{ type: "multiCollectionReference", value: string[] }

// Array (Gallery) — nested items with their own fieldData
{ type: "array", value: ArrayItemInput[] }
```

### ArrayItemInput (for gallery/array fields)

```typescript
interface ArrayItemInput {
    id: string
    fieldData: Record<string, FieldDataEntryInput>
}
```

### Default Values for Missing Fields

When a source item has no data for a field, use type-appropriate defaults:

| Type | Default |
|------|---------|
| `string`, `formattedText` | `""` |
| `boolean` | `false` |
| `number` | `0` |
| `image`, `file`, `link`, `date`, `color` | `null` |
| `collectionReference` | `null` |
| `multiCollectionReference` | `[]` |
| `array` | `[]` |
| `enum` | First case ID |

---


<!-- END SOURCE CONTENT -->
