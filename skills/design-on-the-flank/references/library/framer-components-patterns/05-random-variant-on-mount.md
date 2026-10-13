[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Random Variant on Mount

```typescript
export function withRandomVariant(Component): ComponentType {
    return (props) => {
        const [variant, setVariant] = useState("variant-1")

        useEffect(() => {
            const num = Math.floor(Math.random() * 4) + 1
            setVariant(`variant-${num}`)
        }, [])

        return <Component {...props} variant={variant} />
    }
}
```


<!-- END SOURCE CONTENT -->
