[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
### OrbitControls

```javascript
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const controls = new OrbitControls(camera, renderer.domElement);

// Damping (smooth movement)
controls.enableDamping = true;
controls.dampingFactor = 0.05;

// Rotation limits
controls.minPolarAngle = 0; // Top
controls.maxPolarAngle = Math.PI / 2; // Horizon
controls.minAzimuthAngle = -Math.PI / 4; // Left
controls.maxAzimuthAngle = Math.PI / 4; // Right

// Zoom limits
controls.minDistance = 2;
controls.maxDistance = 50;

// Enable/disable features
controls.enableRotate = true;
controls.enableZoom = true;
controls.enablePan = true;

// Auto-rotate
controls.autoRotate = true;
controls.autoRotateSpeed = 2.0;

// Target (orbit point)
controls.target.set(0, 1, 0);

// Update in animation loop
function animate() {
  controls.update(); // Required for damping and auto-rotate
  renderer.render(scene, camera);
}
```


<!-- END SOURCE CONTENT -->
