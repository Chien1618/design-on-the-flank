[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
### Object (Grouped Controls)
```typescript
settings: {
    type: ControlType.Object,
    title: "Settings",
    icon: "effect", // UI icon: "object" | "effect" | "color" | "interaction" | "boolean"
    controls: {
        opacity: { type: ControlType.Number, defaultValue: 1 },
        color: { type: ControlType.Color, defaultValue: "#fff" },
    },
}
```

The `icon` property changes how the control appears in Framer's property panel. Options: `"object"`, `"effect"`, `"color"`, `"interaction"`, `"boolean"`.


<!-- END SOURCE CONTENT -->
