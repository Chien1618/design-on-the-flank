[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Multi-Column Text Layout

```typescript
export function withColumns(Component): ComponentType {
    return (props) => {
        return (
            <div style={{
                columns: "300px auto",
                columnGap: "50px",
                maxWidth: "100%",
            }}>
                <Component {...props} style={{ ...props.style, margin: 0 }} />
            </div>
        )
    }
}
```


<!-- END SOURCE CONTENT -->
