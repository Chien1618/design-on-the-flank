[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Progress Tracking

For operations with many API calls (from Notion plugin):

```typescript
interface SyncProgress {
    current: number
    total: number
    hasFinishedLoading: boolean
}

// With concurrency limiting:
import pLimit from "p-limit"
const limit = pLimit(5)

const promises = items.map((item, i) =>
    limit(async () => {
        const result = await fetchItemDetails(item.id)
        onProgress({ current: i + 1, total: items.length, hasFinishedLoading: false })
        return result
    })
)
const results = await Promise.allSettled(promises)
```

---


<!-- END SOURCE CONTENT -->
