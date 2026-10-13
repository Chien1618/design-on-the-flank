[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Debugging Tips

- **Toast debugging**: If you see "Invoking protected message type" toasts, it's the SDK — not your code. For settings, switch to `localStorage`.
- **Invisible button text**: If button text disappears in light mode, Framer is overriding your color. Add `color: #fff !important` or use `<div role="button">`.
- **Plugin won't load**: Check `framer.json` for valid mode names and icon paths. Icons must exist in `public/`.
- **Sync runs but nothing appears**: Check that `fieldData` values have the `{ type, value }` wrapper. Raw values are silently ignored.
- **Items disappear after sync**: If you call `removeItems` with all IDs before `addItems`, there's a race condition window. Use the unsynced-items pattern instead.
- **"setPluginData" quota exceeded**: You hit the 4kB limit. Use fewer keys or store structured data as a single JSON string.

<!-- END SOURCE CONTENT -->
