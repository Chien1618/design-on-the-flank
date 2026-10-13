[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Basic Setup

```typescript
import { useEffect, useRef } from "react"

export default function ShaderComponent(props) {
    const canvasRef = useRef(null)

    useEffect(() => {
        const canvas = canvasRef.current
        const gl = canvas.getContext("webgl", { alpha: true })

        if (!gl) {
            console.error("WebGL not supported")
            return
        }

        // Setup and render loop here

        return () => {
            // Cleanup
        }
    }, [])

    return (
        <canvas
            ref={canvasRef}
            style={{
                width: "100%",
                height: "100%",
                display: "block",
            }}
        />
    )
}
```


<!-- END SOURCE CONTENT -->
