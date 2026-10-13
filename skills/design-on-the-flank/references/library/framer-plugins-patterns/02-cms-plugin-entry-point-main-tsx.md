[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## CMS Plugin Entry Point (main.tsx)

The canonical pattern for CMS plugins. Every official CMS plugin follows this structure:

```typescript
import { framer } from "framer-plugin"
import "framer-plugin/framer.css"

const collection = await framer.getActiveManagedCollection()
const previousSourceId = await collection.getPluginData("sourceId")
const previousSlugFieldId = await collection.getPluginData("slugFieldId")

// Attempt silent sync first (syncManagedCollection mode)
if (framer.mode === "syncManagedCollection" && previousSourceId && previousSlugFieldId) {
    if (!framer.isAllowedTo(...SYNC_METHODS)) {
        framer.closePlugin("Insufficient permissions", { variant: "error" })
    }
    await framer.hideUI()
    await syncCollection(collection, previousSourceId, previousSlugFieldId)
    framer.closePlugin("Sync complete", { variant: "success" })
}

// Fall through to configuration UI
const root = document.getElementById("root")!
createRoot(root).render(<App collection={collection} />)
```

**Key insight**: `syncManagedCollection` mode should attempt silent sync and close. Only show UI if sync fails or no config exists. This is the most important CMS plugin pattern.

---


<!-- END SOURCE CONTENT -->
