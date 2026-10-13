[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Toggle on Keystroke

```typescript
export function withKeyToggle(Component): ComponentType {
    return (props) => {
        const [isActive, setIsActive] = useState(false)

        useEffect(() => {
            const handler = (event) => {
                if (event.key === "f" || event.key === "F") {
                    setIsActive(prev => !prev)
                }
            }

            window.addEventListener("keydown", handler)
            return () => window.removeEventListener("keydown", handler)
        }, [])

        return (
            <Component
                {...props}
                style={{ ...props.style, opacity: isActive ? 1 : 0 }}
            />
        )
    }
}
```


<!-- END SOURCE CONTENT -->
