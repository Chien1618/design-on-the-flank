[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Field Definitions — Static vs Dynamic

### Static (simple plugins like RSS):
```typescript
const FIELDS: ManagedCollectionFieldInput[] = [
    { type: "string", name: "Title", id: "title" },
    { type: "link", name: "Link", id: "link" },
    { type: "date", name: "Date", id: "date" },
    { type: "formattedText", name: "Content", id: "content" },
]
```

### Dynamic (complex plugins like Airtable):
Infer field types from the data source, let users customize the mapping in UI, then call `setFields()` with the result.

---


<!-- END SOURCE CONTENT -->
