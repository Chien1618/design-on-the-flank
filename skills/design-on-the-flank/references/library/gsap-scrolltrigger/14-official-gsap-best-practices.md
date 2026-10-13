[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Official GSAP best practices

- ✅ **gsap.registerPlugin(ScrollTrigger)** once before any ScrollTrigger usage.
- ✅ Call **ScrollTrigger.refresh()** after DOM/layout changes (new content, images, fonts) that affect trigger positions. Whenever the viewport is resized, `ScrollTrigger.refresh()` is automatically called (debounced 200ms)
- ✅ In React, use the `useGSAP()` hook to ensure that all ScrollTriggers and GSAP animations are reverted and cleaned up when necessary, or use a `gsap.context()` to do it manually in a useEffect/useLayoutEffect cleanup function. 
- ✅ Use **scrub** for scroll-linked progress or **toggleActions** for discrete play/reverse; do not use both on the same trigger.
- ✅ For fake horizontal scroll with **containerAnimation**, use **ease: "none"** on the horizontal tween/timeline so scroll and horizontal position stay in sync.
- ✅ Create ScrollTriggers in the order they appear on the page (top to bottom, scroll 0 → max). When they are created in a different order (e.g. dynamic or async), set **refreshPriority** on each so they are refreshed in that same top-to-bottom order (first section on page = lower number).


<!-- END SOURCE CONTENT -->
