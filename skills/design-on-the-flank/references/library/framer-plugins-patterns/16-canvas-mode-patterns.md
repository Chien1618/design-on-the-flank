[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Canvas Mode Patterns

For plugins that insert assets onto the canvas:

```typescript
// Mode-dependent behavior
if (framer.mode === "canvas") {
    await framer.addImage({ image: url, name, altText })
} else {
    // "image" or "editImage" mode — set on selection
    await framer.setImage({ image: url, name, altText })
    framer.closePlugin()
}

// Drag-and-drop support
import { Draggable } from "framer-plugin"
<Draggable data={{ type: "image", image: fullUrl, previewImage: thumbUrl, name, altText }}>
    <div className="image-card">...</div>
</Draggable>
```

---


<!-- END SOURCE CONTENT -->
