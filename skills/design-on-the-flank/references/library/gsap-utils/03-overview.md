[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Overview

**gsap.utils** provides pure helpers; no need to register. Use in tween vars (e.g. function-based values), in ScrollTrigger or Observer callbacks, or in any JS that drives GSAP. All are on **gsap.utils** (e.g. `gsap.utils.clamp()`).

**Omitting the value: function form.** Many utils accept the value to transform as the **last** argument. If you omit that argument, the util returns a **function** that accepts the value later. Use the function form when you need to clamp, map, normalize, or snap many values with the same config (e.g. in a mousemove handler or tween callback). **Exception: random()** — pass **true** as the last argument to get a reusable function (do not omit the value); see [random()](https://gsap.com/docs/v3/GSAP/UtilityMethods/random()).

```javascript
// With value: returns the result
gsap.utils.clamp(0, 100, 150); // 100

// Without value: returns a function you call with the value later
let c = gsap.utils.clamp(0, 100);
c(150);  // 100
c(-10);  // 0
```


<!-- END SOURCE CONTENT -->
