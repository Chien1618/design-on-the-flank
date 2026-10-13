[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Do Not

- ❌ Target by **selector without a scope**; always pass **scope** (ref or element) in useGSAP or gsap.context() so selectors like `.box` are limited to that root and do not match elements outside the component.
- ❌ Animate using selector strings that can match elements outside the current component unless a `scope` is defined in useGSAP or gsap.context() so only elements inside the component are affected.
- ❌ Skip cleanup; always revert context or kill tweens/ScrollTriggers in the effect return to avoid leaks and updates on unmounted nodes.
- ❌ Run GSAP or ScrollTrigger during SSR; keep all usage inside client-only lifecycle (e.g. useGSAP).


### Learn More

https://gsap.com/resources/React

<!-- END SOURCE CONTENT -->
