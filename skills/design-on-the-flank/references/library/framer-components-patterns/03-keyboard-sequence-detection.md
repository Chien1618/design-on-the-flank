[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Keyboard Sequence Detection

```typescript
const targetSequence = ["d", "r", "u", "t", "o"]

export function withCodeword(Component): ComponentType {
    return (props) => {
        const [keySequence, setKeySequence] = useState([])
        const [triggered, setTriggered] = useState(false)

        useEffect(() => {
            const handler = (event) => {
                const newSequence = [...keySequence, event.key]
                if (newSequence.length > targetSequence.length) {
                    newSequence.shift()
                }

                const isMatch = targetSequence.every(
                    (key, i) => key === newSequence[i]
                )

                if (isMatch) {
                    setTriggered(true)
                    setKeySequence([])
                } else {
                    setKeySequence(newSequence)
                }
            }

            window.addEventListener("keydown", handler)
            return () => window.removeEventListener("keydown", handler)
        }, [keySequence])

        return <Component {...props} variant={triggered ? "secret" : "default"} />
    }
}
```


<!-- END SOURCE CONTENT -->
