[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Safari SVG Fix

Force GPU acceleration for smooth SVG animations:
```typescript
style={{
    willChange: "transform",
    transform: "translateZ(0)",
    backfaceVisibility: "hidden",
}}
```


<!-- END SOURCE CONTENT -->
