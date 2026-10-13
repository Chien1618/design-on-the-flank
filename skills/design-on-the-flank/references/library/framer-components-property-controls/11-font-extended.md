[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
### Font (Extended)
```typescript
font: {
    type: ControlType.Font,
    title: "Font",
    controls: "extended",
    defaultValue: {
        fontFamily: "Inter",
        fontWeight: 500,
        fontSize: 16,
        lineHeight: "1.5em",
    },
}
```

**Critical**: Always spread the entire font object in styles: `...props.font`

#### Variant-to-FontWeight Mapping

Framer uses `variant` names that map to CSS `font-weight` and `font-style`:

| Variant | font-weight | font-style |
|---------|-------------|------------|
| Thin | 100 | normal |
| Extra Light | 200 | normal |
| Light | 300 | normal |
| Regular | 400 | normal |
| Medium | 500 | normal |
| Semibold | 600 | normal |
| Bold | 700 | normal |
| Extra Bold | 800 | normal |
| Black | 900 | normal |
| Thin Italic | 100 | italic |
| Extra Light Italic | 200 | italic |
| Light Italic | 300 | italic |
| Italic / Regular Italic | 400 | italic |
| Medium Italic | 500 | italic |
| Semibold Italic | 600 | italic |
| Bold Italic | 700 | italic |
| Extra Bold Italic | 800 | italic |
| Black Italic | 900 | italic |

Use these variant names in `defaultValue.variant` when setting up Font controls.


<!-- END SOURCE CONTENT -->
