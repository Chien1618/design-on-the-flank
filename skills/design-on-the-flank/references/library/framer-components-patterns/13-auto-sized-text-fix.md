[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Auto-Sized Text Fix

When using auto-sized components (`@framerSupportedLayoutWidth auto`) with text, apply `minWidth: max-content` to prevent unexpected collapse or wrapping:

```typescript
<span style={{
    minWidth: "max-content",
    ...props.font,
}}>
    {props.label}
</span>
```

See [Auto-sized text fix](https://github.com/fredm00n/framerlabs/blob/main/hacks/Auto-sized%20text%20fix.md) for detailed explanation.


<!-- END SOURCE CONTENT -->
