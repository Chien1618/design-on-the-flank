[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Accessibility and responsive (gsap.matchMedia())

**gsap.matchMedia()** (GSAP 3.11+) runs setup code only when a media query matches; when it stops matching, all animations and ScrollTriggers created in that run are **reverted automatically**. Use it for responsive breakpoints (e.g. desktop vs mobile) and for **prefers-reduced-motion** so users who prefer reduced motion get minimal or no animation.

- **Create:** `let mm = gsap.matchMedia();`
- **Add a query:** `mm.add("(min-width: 800px)", () => { gsap.to(...); return () => { /* optional custom cleanup */ }; });`
- **Revert all:** `mm.revert();` (e.g. on component unmount).
- **Scope (optional):** Pass a third argument (element or ref) so selector text inside the handler is scoped to that root: `mm.add("(min-width: 800px)", () => { ... }, containerRef);`

**Conditions syntax** — Use an object to pass multiple named queries and avoid duplicate code; the handler receives a context with `context.conditions` (booleans per condition):

```javascript
mm.add(
  {
    isDesktop: "(min-width: 800px)",
    isMobile: "(max-width: 799px)",
    reduceMotion: "(prefers-reduced-motion: reduce)"
  },
  (context) => {
    const { isDesktop, reduceMotion } = context.conditions;
    gsap.to(".box", {
      rotation: isDesktop ? 360 : 180,
      duration: reduceMotion ? 0 : 2  // skip animation when user prefers reduced motion
    });
    return () => { /* optional cleanup when no condition matches */ };
  }
);
```

Respecting **prefers-reduced-motion** is important for users with vestibular disorders. Use `duration: 0` or skip the animation when `reduceMotion` is true. Do not nest **gsap.context()** inside matchMedia — matchMedia creates a context internally; use **mm.revert()** only.

Full docs: [gsap.matchMedia()](https://gsap.com/docs/v3/GSAP/gsap.matchMedia/). For immediate re-run of all matching handlers (e.g. after toggling a reduced-motion control), use **gsap.matchMediaRefresh()**.


<!-- END SOURCE CONTENT -->
