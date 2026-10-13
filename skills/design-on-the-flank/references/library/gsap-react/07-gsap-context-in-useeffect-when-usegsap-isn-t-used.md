[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## gsap.context() in useEffect (when useGSAP isn't used)

It's okay to use **gsap.context()** inside a regular **useEffect()** when @gsap/react is not used or when the effect's dependency/trigger behavior is needed. When doing so, **always** call **ctx.revert()** in the effect's cleanup function so animations and ScrollTriggers are killed and inline styles are reverted. Otherwise this causes leaks and updates on detached nodes.

```javascript
useEffect(() => {
  const ctx = gsap.context(() => {
    gsap.to(".box", { x: 100 });
    gsap.from(".item", { opacity: 0, stagger: 0.1 });
  }, containerRef);
  return () => ctx.revert();
}, []);
```

- ✅ Pass a **scope** (ref or element) as the second argument so selectors are scoped to that node.
- ✅ **Always** return a cleanup that calls **ctx.revert()**.


<!-- END SOURCE CONTENT -->
