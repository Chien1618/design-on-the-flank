[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Error Handling

```typescript
import { FramerPluginClosedError } from "framer-plugin"

try {
    await syncCollection(collection)
    framer.closePlugin("Sync complete", { variant: "success" })
} catch (error) {
    if (error instanceof FramerPluginClosedError) return  // User closed plugin, ignore
    framer.notify(error.message, { variant: "error" })
}
```

The SDK auto-suppresses unhandled `FramerPluginClosedError` rejections. If you have a catch block that handles errors generically, explicitly check for and ignore this class.

---


<!-- END SOURCE CONTENT -->
