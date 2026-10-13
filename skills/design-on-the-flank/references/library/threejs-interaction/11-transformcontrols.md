[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## TransformControls

Gizmo for moving/rotating/scaling objects.

```javascript
import { TransformControls } from "three/addons/controls/TransformControls.js";

const transformControls = new TransformControls(camera, renderer.domElement);
scene.add(transformControls);

// Attach to object
transformControls.attach(selectedMesh);

// Switch modes
transformControls.setMode("translate"); // 'translate', 'rotate', 'scale'

// Change space
transformControls.setSpace("local"); // 'local', 'world'

// Size
transformControls.setSize(1);

// Events
transformControls.addEventListener("dragging-changed", (event) => {
  // Disable orbit controls while dragging
  orbitControls.enabled = !event.value;
});

transformControls.addEventListener("change", () => {
  renderer.render(scene, camera);
});

// Keyboard shortcuts
window.addEventListener("keydown", (event) => {
  switch (event.key) {
    case "g":
      transformControls.setMode("translate");
      break;
    case "r":
      transformControls.setMode("rotate");
      break;
    case "s":
      transformControls.setMode("scale");
      break;
    case "Escape":
      transformControls.detach();
      break;
  }
});
```


<!-- END SOURCE CONTENT -->
