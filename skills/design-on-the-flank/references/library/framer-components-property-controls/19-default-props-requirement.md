[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Default Props Requirement

Property Controls only affect canvas. Always define `defaultProps` for:
- Preventing runtime errors
- Components instantiated from code
- Initial render before controls apply

```typescript
MyComponent.defaultProps = {
    text: "Default",
    color: "#000",
    font: {
        fontFamily: "Inter",
        fontWeight: 500,
        fontSize: 16,
    },
}
```


<!-- END SOURCE CONTENT -->
