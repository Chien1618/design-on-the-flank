[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Shader Compilation Safety

**Always check shader compilation before attaching:**

```typescript
function createShader(gl, type, source) {
    const shader = gl.createShader(type)
    gl.shaderSource(shader, source)
    gl.compileShader(shader)

    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error("Shader compilation failed:", gl.getShaderInfoLog(shader))
        gl.deleteShader(shader)
        return null
    }
    return shader
}

function createProgram(gl, vertexShader, fragmentShader) {
    // Guard against null shaders
    if (!vertexShader || !fragmentShader) return null

    const program = gl.createProgram()
    gl.attachShader(program, vertexShader)
    gl.attachShader(program, fragmentShader)
    gl.linkProgram(program)

    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
        console.error("Program linking failed:", gl.getProgramInfoLog(program))
        gl.deleteProgram(program)
        return null
    }
    return program
}

// Usage with null checks
const vertexShader = createShader(gl, gl.VERTEX_SHADER, vertexSource)
if (!vertexShader) return

const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragmentSource)
if (!fragmentShader) return

const program = createProgram(gl, vertexShader, fragmentShader)
if (!program) return
```


<!-- END SOURCE CONTENT -->
