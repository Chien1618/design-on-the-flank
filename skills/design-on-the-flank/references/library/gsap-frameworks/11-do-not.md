[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Do Not

- ❌ Create tweens or ScrollTriggers before the component is mounted (e.g. in setup without onMounted); the DOM nodes may not exist yet.
- ❌ Use selector strings without a **scope** (pass the container to gsap.context() as the second argument) so selectors don’t match elements outside the component.
- ❌ Skip cleanup; always call **ctx.revert()** in onUnmounted / onMount’s return so animations and ScrollTriggers are killed when the component is destroyed.
- ❌ Register plugins inside a component body that runs every render (it doesn't hurt anything, it's just wasteful); register once at app level.

### Learn More

- **gsap-react** skill for React-specific patterns (useGSAP, contextSafe).

<!-- END SOURCE CONTENT -->
