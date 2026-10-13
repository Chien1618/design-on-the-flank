[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Quick Start

```javascript
import * as THREE from "three";

// Built-in geometry
const box = new THREE.BoxGeometry(1, 1, 1);
const sphere = new THREE.SphereGeometry(0.5, 32, 32);
const plane = new THREE.PlaneGeometry(10, 10);

// Create mesh
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const mesh = new THREE.Mesh(box, material);
scene.add(mesh);
```


<!-- END SOURCE CONTENT -->
