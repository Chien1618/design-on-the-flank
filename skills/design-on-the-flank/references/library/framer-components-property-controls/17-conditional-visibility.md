[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Conditional Visibility

Hide controls based on other prop values:

```typescript
advancedMode: {
    type: ControlType.Boolean,
    defaultValue: false,
},
advancedSetting: {
    type: ControlType.Number,
    hidden: (props) => !props.advancedMode,
},
```


<!-- END SOURCE CONTENT -->
