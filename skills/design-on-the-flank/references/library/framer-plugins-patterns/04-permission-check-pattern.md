[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Permission Check Pattern

```typescript
import { framer, type ProtectedMethod } from "framer-plugin"

export const SYNC_METHODS = [
    "ManagedCollection.setFields",
    "ManagedCollection.addItems",
    "ManagedCollection.removeItems",
    "ManagedCollection.setPluginData",
] as const satisfies ProtectedMethod[]

// At sync start (imperative):
if (!framer.isAllowedTo(...SYNC_METHODS)) {
    framer.closePlugin("Insufficient permissions", { variant: "error" })
}

// In React components (reactive):
import { useIsAllowedTo } from "framer-plugin"
const canSync = useIsAllowedTo(...SYNC_METHODS)
<button disabled={!canSync} onClick={handleSync}>Sync</button>
```

---


<!-- END SOURCE CONTENT -->
