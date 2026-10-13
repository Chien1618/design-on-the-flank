[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Principles (All Frameworks)

- **Create** tweens and ScrollTriggers **after** the component’s DOM is available (e.g. onMounted, onMount).
- **Kill or revert** them in the **unmount** (or equivalent) cleanup so nothing runs on detached nodes and there are no leaks.
- **Scope selectors** to the component root so `.box` and similar only match elements inside that component, not the rest of the page.


<!-- END SOURCE CONTENT -->
