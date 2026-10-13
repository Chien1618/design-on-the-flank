[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Cleanup Pattern

```typescript
useEffect(() => {
    let animationId

    // Setup...

    function render() {
        // Draw...
        animationId = requestAnimationFrame(render)
    }
    render()

    return () => {
        if (animationId) {
            cancelAnimationFrame(animationId)
        }
        // Additional cleanup: delete shaders, programs, buffers
    }
}, [])
```


<!-- END SOURCE CONTENT -->
