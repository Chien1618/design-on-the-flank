[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Data Storage

### pluginData size limits
- `framer.setPluginData()`: 2kB per entry, 4kB total across all keys (project-level)
- `collection.setPluginData()`: 2kB per entry, 4kB per collection
- Values must be strings. Pass `null` to delete a key.

### localStorage is sandboxed
`localStorage` is sandboxed per-plugin origin and per-user. It's safe for API keys and tokens. It's synchronous (no async needed) and has no Framer-imposed size limits.

### When to use which storage

| Data | Storage | Reason |
|------|---------|--------|
| API keys, auth tokens | `localStorage` | Per-user, not shared, no size warnings |
| User preferences | `localStorage` | Per-user, synchronous |
| Data source ID, slug field | `collection.setPluginData()` | Shared across collaborators |
| Last sync timestamp | `collection.setPluginData()` | Shared state for the collection |
| Project-level config | `framer.setPluginData()` | Shared, but tiny (4kB total) |

Per Framer's own docs: `pluginData` should NOT store sensitive data like API keys.

---


<!-- END SOURCE CONTENT -->
