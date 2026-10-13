[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Key Rules

1. Always check the project's `CLAUDE.md` for project-specific overrides and decisions
2. CMS plugins should attempt silent sync in `syncManagedCollection` mode before showing UI
3. `addItems()` is upsert — no need to check for existing items before adding
4. Field data values MUST include explicit `type` property: `{ type: "string", value: "..." }`
5. Use `localStorage` for sensitive/user-specific data, `pluginData` for shared sync state
6. Import `"framer-plugin/framer.css"` for standard Framer plugin styling
7. Use `<div role="button">` instead of `<button>` to avoid Framer's CSS overrides
8. Handle `FramerPluginClosedError` in catch blocks — ignore it silently
9. Call `showUI` in `useLayoutEffect` to avoid flicker when resizing
10. Always check permissions with `framer.isAllowedTo()` before sync operations

<!-- END SOURCE CONTENT -->
