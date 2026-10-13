[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Prefer the useGSAP() Hook

When **@gsap/react** is available, use the **useGSAP()** hook instead of `useEffect()` for GSAP setup. It handles cleanup automatically and provides a scope and **contextSafe** for callbacks.

```javascript
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(useGSAP); // register before running useGSAP or any GSAP code

const containerRef = useRef(null);

useGSAP(() => {
  gsap.to(".box", { x: 100 });
  gsap.from(".item", { opacity: 0, stagger: 0.1 });
}, { scope: containerRef });
```

- ✅ Pass a **scope** (ref or element) so selectors like `.box` are scoped to that root.
- ✅ Cleanup (reverting animations and ScrollTriggers) runs automatically on unmount.
- ✅ Use **contextSafe** from the hook's return value to wrap callbacks (e.g. onComplete) so they no-op after unmount and avoid React warnings.


<!-- END SOURCE CONTENT -->
