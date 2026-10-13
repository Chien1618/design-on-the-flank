[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Common Mistakes

### Not attempting silent sync
The most common mistake in CMS plugins: always showing UI in `syncManagedCollection` mode. The correct pattern is to try syncing silently first and close the plugin on success. Only fall through to UI if sync fails or no config exists.

### Forgetting field data type wrapper
Field values must include explicit type:
```typescript
// WRONG
fieldData: { title: "Hello" }

// CORRECT
fieldData: { title: { type: "string", value: "Hello" } }
```

### Using setPluginData for API keys
API keys should go in `localStorage`, not `pluginData`. `pluginData` is shared across all project collaborators and triggers toast warnings.

### Not handling FramerPluginClosedError
If you have try/catch around async operations that end with `closePlugin()`, you must explicitly ignore `FramerPluginClosedError` or your error handling will catch it.

### Hardcoding UI dimensions
Plugin UI should resize based on the current screen state. Use `useLayoutEffect` to call `showUI` with appropriate dimensions when the state changes.

### Not checking permissions before sync
Always call `framer.isAllowedTo()` at the start of sync operations. Without it, users see unhelpful "Insufficient permissions" toasts mid-sync.

---


<!-- END SOURCE CONTENT -->
