[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## NPM Package Imports

Standard import (preferred):
```typescript
import { Component } from "package-name"
```

Force specific version via CDN when Framer cache is stuck:
```typescript
import { Component } from "https://esm.sh/package-name@1.2.3?external=react,react-dom"
```

Always include `?external=react,react-dom` for React components.

**Critical for Three.js in Framer:**
Framer's SSR environment **does not support** Node.js `require()` for Three.js addon modules (like `EffectComposer` or `GLTFLoader`). You must import them via `esm.sh` and set `?external=three` to prevent duplicate Three.js instances:

```typescript
// ❌ FAILS IN FRAMER:
// const EffectComposer = require("three/examples/jsm/postprocessing/EffectComposer.js")

// ✅ CORRECT:
import { EffectComposer } from "https://esm.sh/three@0.160.0/examples/jsm/postprocessing/EffectComposer.js?external=three"
import { RenderPass } from "https://esm.sh/three@0.160.0/examples/jsm/postprocessing/RenderPass.js?external=three"
```


<!-- END SOURCE CONTENT -->
