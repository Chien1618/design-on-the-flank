[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
### String
```typescript
text: {
    type: ControlType.String,
    title: "Text",
    defaultValue: "Hello",
    placeholder: "Enter text...",
    displayTextArea: true, // For multiline
    preventLocalization: true, // Prevents automatic translation
}
```

Use `preventLocalization: true` for technical content that shouldn't be translated (API keys, code snippets, etc.).


<!-- END SOURCE CONTENT -->
