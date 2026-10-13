[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Default Media Placeholder URLs

Working placeholder URLs for components with media controls:

```typescript
const placeholders = {
    image: "https://framerusercontent.com/images/GfGkADagM4KEibNcIiRUWlfrR0.jpg",
    video: "https://framerusercontent.com/assets/MLWPbW1dUQawJLhhun3dBwpgJak.mp4",
    audio: "https://framerusercontent.com/assets/8w3IUatLX9a5JVJ6XPCVuHi94.mp3",
}
```

Use these when setting default values via parameter destructuring (since `ControlType.ResponsiveImage` and `ControlType.File` don't support `defaultValue`).

<!-- END SOURCE CONTENT -->
