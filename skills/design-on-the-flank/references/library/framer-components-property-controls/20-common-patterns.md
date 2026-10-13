[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Common Patterns

### Mode-Dependent Controls
```typescript
addPropertyControls(Component, {
    mode: {
        type: ControlType.Enum,
        options: ["image", "video"],
        defaultValue: "image",
    },
    image: {
        type: ControlType.Image,
        hidden: (props) => props.mode !== "image",
    },
    video: {
        type: ControlType.File,
        allowedFileTypes: ["mp4"],
        hidden: (props) => props.mode !== "video",
    },
})
```

### Nested Object with Conditional
```typescript
progressOptions: {
    type: ControlType.Object,
    title: "Progress",
    controls: {
        showProgress: {
            type: ControlType.Boolean,
            defaultValue: false,
        },
        progressFont: {
            type: ControlType.Font,
            controls: "extended",
            hidden: (props) => !props.showProgress,
        },
    },
}
```

Note: In nested objects, `hidden` receives the parent object, not root props.

<!-- END SOURCE CONTENT -->
