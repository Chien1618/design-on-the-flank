[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## UI & Styling

### Framer overrides `<button>` styles
Framer's built-in CSS has high specificity on `<button>` elements. Custom backgrounds and text colors get silently overridden, especially in light mode.

**Workarounds:**
- Use `<div role="button" tabIndex={0}>` for custom-styled interactive elements
- If you must use `<button>`, apply `!important` on `background` and `color`
- Use high-specificity selectors: `.parent .child.active { background: red !important; }`

### framer.css conflicts
Importing `"framer-plugin/framer.css"` provides Framer's base styles (fonts, colors, input styling), but can conflict with custom CSS. The import is optional but recommended for a native look.

### showUI flicker
Calling `framer.showUI()` in a `useEffect` causes a visible resize flicker. Always use `useLayoutEffect`:

```typescript
useLayoutEffect(() => {
    framer.showUI({ width: 320, height: hasConfig ? 380 : 340 })
}, [hasConfig])
```

### SVG icon centering
Icons in `framer.json` must use a 30×30 viewBox. Paths drawn at absolute coordinates can end up outside the visible area. Use `<g transform="translate(15 15)">` with centered path coordinates.

---


<!-- END SOURCE CONTENT -->
