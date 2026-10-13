[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Canvas Positioning for Effects

For effects that need to extend beyond component bounds:

```typescript
const safetyMargin = 100

// Canvas larger than container
const canvasWidth = containerWidth + safetyMargin * 2
const canvasHeight = containerHeight + safetyMargin * 2

// Position with negative offset
<canvas
    style={{
        position: "absolute",
        top: -safetyMargin,
        left: -safetyMargin,
        width: canvasWidth,
        height: canvasHeight,
        pointerEvents: "none",
    }}
/>
```

Container needs `overflow: visible` for this pattern.

<!-- END SOURCE CONTENT -->
