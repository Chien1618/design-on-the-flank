[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Critical: Wrap State Updates in startTransition

All React state updates in Framer must be wrapped in `startTransition()`:

```typescript
import { startTransition } from "react"

// ❌ WRONG - May cause issues in Framer's rendering pipeline
setCount(count + 1)

// ✅ CORRECT - Always wrap state updates
startTransition(() => {
    setCount(count + 1)
})
```

This is Framer-specific and prevents performance issues with concurrent rendering.


<!-- END SOURCE CONTENT -->
