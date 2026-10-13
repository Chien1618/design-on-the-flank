[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## AmbientLight

Illuminates all objects equally. No direction, no shadows.

```javascript
// AmbientLight(color, intensity)
const ambient = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambient);

// Modify at runtime
ambient.color.set(0xffffcc);
ambient.intensity = 0.3;
```


<!-- END SOURCE CONTENT -->
