[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Scroll Frame Sequence

```typescript
export default function ScrollSequence(props) {
    const { images, scrollSensitivity = 50 } = props
    const [frame, setFrame] = useState(0)
    const accumulator = useRef(0)
    const lastY = useRef(0)

    useEffect(() => {
        const handler = () => {
            const delta = window.scrollY - lastY.current
            lastY.current = window.scrollY

            accumulator.current += Math.abs(delta)

            if (accumulator.current >= scrollSensitivity) {
                const change = Math.floor(accumulator.current / scrollSensitivity)
                accumulator.current %= scrollSensitivity

                setFrame(prev => {
                    const next = delta > 0 ? prev + change : prev - change
                    return ((next % images.length) + images.length) % images.length
                })
            }
        }

        window.addEventListener("scroll", handler, { passive: true })
        return () => window.removeEventListener("scroll", handler)
    }, [images.length, scrollSensitivity])

    return <img src={images[frame]} style={{ width: "100%", height: "100%" }} />
}
```


<!-- END SOURCE CONTENT -->
