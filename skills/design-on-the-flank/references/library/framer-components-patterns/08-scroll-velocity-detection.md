[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Scroll Velocity Detection

```typescript
export function withScrollBlur(Component): ComponentType {
    return (props) => {
        const [blur, setBlur] = useState(0)
        const lastScrollY = useRef(0)
        const lastTime = useRef(Date.now())

        useEffect(() => {
            let animationId

            const handleScroll = () => {
                const now = Date.now()
                const deltaTime = now - lastTime.current
                const deltaScroll = Math.abs(window.scrollY - lastScrollY.current)

                if (deltaTime > 0) {
                    const velocity = deltaScroll / deltaTime
                    setBlur(Math.min(velocity * 10, 20))
                }

                lastScrollY.current = window.scrollY
                lastTime.current = now
            }

            const decay = () => {
                setBlur(prev => {
                    const next = prev * 0.9
                    return next < 0.1 ? 0 : next
                })
                animationId = requestAnimationFrame(decay)
            }

            window.addEventListener("scroll", handleScroll, { passive: true })
            animationId = requestAnimationFrame(decay)

            return () => {
                window.removeEventListener("scroll", handleScroll)
                cancelAnimationFrame(animationId)
            }
        }, [])

        return (
            <Component
                {...props}
                style={{
                    ...props.style,
                    backdropFilter: `blur(${blur}px)`,
                    WebkitBackdropFilter: `blur(${blur}px)`,
                }}
            />
        )
    }
}
```


<!-- END SOURCE CONTENT -->
