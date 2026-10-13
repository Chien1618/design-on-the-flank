[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Screenshot Exclude Class

```typescript
export function withScreenshotExclude(Component): ComponentType {
    return (props) => {
        const className = (props.className || "") + " screenshot-exclude"
        return <Component {...props} className={className} />
    }
}
```


<!-- END SOURCE CONTENT -->
