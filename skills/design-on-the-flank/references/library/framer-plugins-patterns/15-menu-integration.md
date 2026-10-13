[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Menu Integration

Add context menu items to the plugin:

```typescript
framer.setMenu([
    {
        label: `View ${tableName} in Airtable`,
        visible: Boolean(dataSource),
        onAction: () => window.open(`https://airtable.com/${baseId}/${tableId}`),
    },
    { type: "separator" },
    { label: "Log Out", onAction: () => auth.logout() },
])
```

---


<!-- END SOURCE CONTENT -->
