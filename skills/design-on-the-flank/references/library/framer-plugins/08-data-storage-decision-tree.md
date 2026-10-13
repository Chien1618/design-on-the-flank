[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Data Storage Decision Tree

| Need | Use | Why |
|------|-----|-----|
| API keys, auth tokens | `localStorage` | Per-user, no size warnings, not shared |
| User preferences | `localStorage` | Per-user, synchronous |
| Data source ID, last sync time | `collection.setPluginData()` | Shared across collaborators, tied to collection |
| Project-level config | `framer.setPluginData()` | Shared, but 4kB total limit |

- `pluginData`: 2kB per entry, 4kB total. Strings only. Pass `null` to delete.
- `localStorage`: Sandboxed per-plugin origin. No size warnings.
- `setPluginData()` triggers "Invoking protected message type" toast (SDK bug).


<!-- END SOURCE CONTENT -->
