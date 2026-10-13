[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## When to Create vs Kill

| Lifecycle             | Action                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Mounted**           | Create tweens and ScrollTriggers inside **gsap.context(scope)**.                                                  |
| **Unmount / Destroy** | Call **ctx.revert()** so all animations and ScrollTriggers in that context are killed and inline styles reverted. |

Do not create GSAP animations in the component’s setup or in a synchronous top-level script that runs before the root element exists. Wait for **onMounted** / **onMount** (or equivalent) so the container ref is in the DOM.


<!-- END SOURCE CONTENT -->
