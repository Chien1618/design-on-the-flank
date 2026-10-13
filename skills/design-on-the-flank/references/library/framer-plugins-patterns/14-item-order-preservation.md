[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Item Order Preservation

Google Sheets plugin preserves row order:

```typescript
await collection.addItems(collectionItems)
await collection.setItemOrder(collectionItems.map(item => item.id))
```

---


<!-- END SOURCE CONTENT -->
