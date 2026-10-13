[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Permissions

```typescript
import { framer, useIsAllowedTo, type ProtectedMethod } from "framer-plugin"

// Imperative check
framer.isAllowedTo("ManagedCollection.addItems", "ManagedCollection.removeItems")

// React hook (reactive)
const canSync = useIsAllowedTo("ManagedCollection.addItems", "ManagedCollection.removeItems")

// Standard CMS sync permissions
const SYNC_METHODS = [
    "ManagedCollection.setFields",
    "ManagedCollection.addItems",
    "ManagedCollection.removeItems",
    "ManagedCollection.setPluginData",
] as const satisfies ProtectedMethod[]
```


<!-- END SOURCE CONTENT -->
