[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Common vars

- **duration** — seconds (default 0.5).
- **delay** — seconds before start.
- **ease** — string or function. Prefer built-in: `"power1.out"` (default), `"power3.inOut"`, `"back.out(1.7)"`, `"elastic.out(1, 0.3)"`, `"none"`.
- **stagger** — number (seconds between) like `0.1` or object: `{ amount: 0.3, from: "center" }`, `{ each: 0.1, from: "random" }`.
- **overwrite** — `false` (default), `true` (immediately kill all active tweens of the same targets), or `"auto"` (when the tween renders for the first time, only kill individual overlapping properties in other **active** tweens of the same targets).
- **repeat** — number or `-1` for infinite.
- **yoyo** — boolean; with repeat, alternates direction.
- **onComplete**, **onStart**, **onUpdate** — callbacks; scoped to the Animation instance itself (Tween or Timeline).
- **immediateRender** — When `true` (default for **from()** and **fromTo()**), the tween’s start state is applied as soon as the tween is created (avoids flash of unstyled content and works well with staggered timelines). When **multiple from() or fromTo() tweens** target the same property of the same element, set **immediateRender: false** on the later one(s) so the first tween’s end state is not overwritten before it runs; otherwise the second animation may not be visible.


<!-- END SOURCE CONTENT -->
