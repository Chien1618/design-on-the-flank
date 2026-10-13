[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## UI Sizing Per Screen State

Official plugins change window size based on the current screen:

```typescript
// Separate functions for each UI state
async function showLoginUI() {
    await framer.showUI({ width: 320, height: 340, resizable: false })
}

async function showConfigUI() {
    await framer.showUI({ width: 360, height: 425, minWidth: 360, minHeight: 425, resizable: true })
}

// Or in useLayoutEffect based on state:
useLayoutEffect(() => {
    framer.showUI({
        width: hasConfig ? 360 : 260,
        height: hasConfig ? 425 : 340,
        resizable: hasConfig,
    })
}, [hasConfig])
```

---


<!-- END SOURCE CONTENT -->
