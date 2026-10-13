[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Magnetic Hover Effect

```typescript
import { motion, useSpring } from "framer-motion"

const SPRING_CONFIG = { damping: 100, stiffness: 1000 }

export function withMagnet(Component): ComponentType {
    return (props) => {
        const springX = useSpring(0, SPRING_CONFIG)
        const springY = useSpring(0, SPRING_CONFIG)

        const handleMove = (e) => {
            const rect = e.currentTarget.getBoundingClientRect()
            const centerX = rect.left + rect.width / 2
            const centerY = rect.top + rect.height / 2

            springX.set((e.clientX - centerX) * 0.3)
            springY.set((e.clientY - centerY) * 0.3)
        }

        const handleLeave = () => {
            springX.set(0)
            springY.set(0)
        }

        return (
            <motion.div
                onPointerMove={handleMove}
                onPointerLeave={handleLeave}
                style={{
                    x: springX,
                    y: springY,
                    willChange: "transform",
                    transform: "translateZ(0)",
                    backfaceVisibility: "hidden",
                }}
            >
                <Component {...props} />
            </motion.div>
        )
    }
}
```


<!-- END SOURCE CONTENT -->
