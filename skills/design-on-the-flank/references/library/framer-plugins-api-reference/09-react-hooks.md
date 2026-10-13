[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## React Hooks

```typescript
import { useIsAllowedTo } from "framer-plugin"

// Reactive permission check — re-renders when permissions change
const canSync: boolean = useIsAllowedTo(
    "ManagedCollection.addItems",
    "ManagedCollection.removeItems"
)
```

---


<!-- END SOURCE CONTENT -->
