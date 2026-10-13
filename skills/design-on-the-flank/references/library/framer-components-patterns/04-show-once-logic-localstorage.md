[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Show-Once Logic (localStorage)

```typescript
export function withShowOnce(Component): ComponentType {
    return (props) => {
        const [shouldShow, setShouldShow] = useState(() => {
            try {
                return !localStorage.getItem("hasShown")
            } catch {
                return true
            }
        })

        useEffect(() => {
            if (shouldShow) {
                localStorage.setItem("hasShown", "true")
            }
        }, [shouldShow])

        if (!shouldShow) return null

        return <Component {...props} />
    }
}
```


<!-- END SOURCE CONTENT -->
