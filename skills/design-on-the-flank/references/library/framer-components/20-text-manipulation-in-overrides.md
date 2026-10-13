[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Text Manipulation in Overrides

Framer text uses deeply nested structure. Process recursively:

```typescript
const processChildren = (children) => {
    if (typeof children === "string") {
        return processText(children)
    }
    if (isValidElement(children)) {
        return cloneElement(children, {
            ...children.props,
            children: processChildren(children.props.children)
        })
    }
    if (Array.isArray(children)) {
        return children.map(child => processChildren(child))
    }
    return children
}
```


<!-- END SOURCE CONTENT -->
