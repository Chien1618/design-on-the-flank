[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Framer Environment

### Cmd+Z / Ctrl+Z captures globally
Framer captures undo globally. Users may accidentally undo the plugin instantiation when they expect to undo text input within the plugin. This is NOT interceptable from within the plugin iframe.

### Console logs
`console.log` output appears in the browser devtools, not the terminal. To see logs:
1. Right-click the plugin iframe in Framer
2. "Inspect Element"
3. Switch to Console tab

The `npm run dev` terminal only shows Vite build/HMR output.

### Plugins run in an iframe
All plugins execute inside a sandboxed iframe. This means:
- CORS restrictions apply to external API calls
- `window.parent` access is limited
- Storage is sandboxed per-origin

### Permission errors
When a plugin attempts a protected operation without permission, the SDK throws `FramerPluginError` and shows a toast: "Insufficient permissions." Always check with `framer.isAllowedTo()` before attempting protected operations.

---


<!-- END SOURCE CONTENT -->
