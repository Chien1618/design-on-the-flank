[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Transparency Support

Four requirements for transparent shaders:

### 1. Alpha-enabled Context
```typescript
const gl = canvas.getContext("webgl", { alpha: true })
```

### 2. Blending Configuration
```typescript
gl.enable(gl.BLEND)
gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA)
```

### 3. Transparent Clear Color
```typescript
gl.clearColor(0.0, 0.0, 0.0, 0.0)
gl.clear(gl.COLOR_BUFFER_BIT)
```

### 4. Fragment Shader Alpha Handling
```glsl
// Accumulate alpha in fragment shader
cl.a += smoothstep(2.5, 0.0, rz) * 0.1;

// Limit maximum opacity
color.a = min(color.a, 0.7);
```


<!-- END SOURCE CONTENT -->
