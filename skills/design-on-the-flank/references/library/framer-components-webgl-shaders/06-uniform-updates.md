[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Uniform Updates

```typescript
const resolutionLocation = gl.getUniformLocation(program, "resolution")
const timeLocation = gl.getUniformLocation(program, "time")

let startTime = performance.now()

function render() {
    gl.useProgram(program)
    gl.uniform2f(resolutionLocation, gl.canvas.width, gl.canvas.height)
    gl.uniform1f(timeLocation, (performance.now() - startTime) * 0.001)

    // Draw...
    requestAnimationFrame(render)
}
```


<!-- END SOURCE CONTENT -->
