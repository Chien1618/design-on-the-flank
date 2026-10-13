[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Shadertoy to WebGL Conversion

When adapting complex Shadertoy algorithms (GLSL) into Framer React Code Components using raw WebGL 1.0, you must handle several strict limitations:

### 1. WebGL 1.0 Syntax Limitations
**No `tanh()`**: WebGL 1.0 doesn't have a native hyperbolic tangent. Use an exponential approximation and clamp to prevent overflow/NaN (which causes black screens):
```glsl
vec4 tanh_approx(vec4 x) {
    vec4 x_clamped = clamp(x, -20.0, 20.0);
    vec4 exp2x = exp(2.0 * x_clamped);
    return (exp2x - 1.0) / (exp2x + 1.0);
}
```

**Strict Typing**: WebGL 1.0 does not auto-cast. You cannot mix floats and ints (e.g., `1` vs `1.0`).

**For-Loops**: WebGL 1.0 requires loop indices to be compared to a constant expression. You cannot mutate the iterator in complex ways inside the loop header (e.g., `for(o*=i; i++<1e2; ...)` will fail). Extract logic cleanly:
```glsl
// ❌ Shadertoy shortcut (Fails in WebGL 1.0)
for(o*=i; i++<1e2; p += cos(...)) { ... }

// ✅ WebGL 1.0 compliant
float i = 0.0;
for(int j = 0; j < 100; j++) {
    i += 1.0;
    float fi = float(j);
    // ... Math logic here ...
}
```

### 2. Framer Canvas vs Published (Performance Drop)
Shaders iterate per pixel. A loop of 100 iterations on a 4K retina screen (DPR 2.0) will instantly freeze Framer's editor because it executes millions of calculations per frame.

**Solution:** Clamp Device Pixel Ratio (`dpr`) to preserve framerate, and disable time-based animations on Canvas:
```typescript
// Inside render() function
// Downscale high-density screens for complex shaders (e.g., limit to 0.75 or 1.0)
const dpr = window.devicePixelRatio > 1.5 ? 1.0 : window.devicePixelRatio

if (canvas.width !== Math.floor(displayWidth * dpr)) {
    canvas.width = Math.floor(displayWidth * dpr)
    canvas.height = Math.floor(displayHeight * dpr)
}

// Stop heavy time calculations in Editor to keep Canvas snappy
const currentTime = isOnCanvas ? 0 : (performance.now() - startTime) * 0.001 * speed
```


<!-- END SOURCE CONTENT -->
