[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
### ResponsiveImage / File — No defaultValue Support

**Critical**: `ControlType.ResponsiveImage` and `ControlType.File` do NOT support `defaultValue` in property controls. You must use component parameter destructuring instead:

```typescript
// ❌ WRONG - defaultValue is ignored
addPropertyControls(MyComponent, {
    image: {
        type: ControlType.ResponsiveImage,
        defaultValue: { src: "...", alt: "..." }, // This does nothing!
    },
})

// ✅ CORRECT - Use parameter destructuring
function MyComponent(props) {
    const {
        image = {
            src: "https://framerusercontent.com/images/GfGkADagM4KEibNcIiRUWlfrR0.jpg",
            alt: "Default image"
        }
    } = props

    return <img {...image} />
}

addPropertyControls(MyComponent, {
    image: { type: ControlType.ResponsiveImage },
})
```

Same pattern applies to `ControlType.File`:
```typescript
function MyComponent(props) {
    const {
        videoFile = "https://framerusercontent.com/assets/MLWPbW1dUQawJLhhun3dBwpgJak.mp4"
    } = props

    return <video src={videoFile} />
}
```


<!-- END SOURCE CONTENT -->
