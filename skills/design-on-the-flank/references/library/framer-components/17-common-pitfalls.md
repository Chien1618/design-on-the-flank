[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Common Pitfalls

| Issue | Cause | Fix |
|-------|-------|-----|
| Font styles not applying | Accessing font props individually | Spread entire font object: `...props.font` |
| Hydration mismatch | Browser API in render | Use `isClient` state pattern |
| Override props undefined | Expecting property controls | Overrides don't support `addPropertyControls` |
| Scroll animation broken | `overflow: scroll` on container | Use IntersectionObserver on viewport |
| Shader attach error | Null shader from compilation failure | Check `createShader()` return before `attachShader()` |
| Component display name | Need custom name in Framer UI | `Component.displayName = "Name"` |
| TypeScript `Timeout` errors | Using `NodeJS.Timeout` type | Use `number` instead — browser environment |
| Overlay stuck under content | Stacking context from parent | Use React Portal to render at `document.body` level |
| Easing feels same for all curves | Not tracking initial distance | Track `initialDiff` when target changes for progress calculation |


<!-- END SOURCE CONTENT -->
