[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Official GSAP best practices

- ✅ Use **property names in camelCase** in vars (e.g. `backgroundColor`, `rotationX`).
- ✅ Prefer **transform aliases** (`x`, `y`, `scale`, `rotation`, `xPercent`, `yPercent`, etc.) over animating the raw `transform` string; use **autoAlpha** instead of `opacity` for fade in/out when elements should be hidden and non-interactive at 0.
- ✅ Use documented built-in eases; use CustomEase only when a custom curve is needed.
- ✅ Store the tween/timeline return value when controlling playback (pause, play, reverse, kill).
- ✅ Prefer timelines instead of chaining animations using `delay`.
- ✅ Use **gsap.matchMedia()** for responsive breakpoints and **prefers-reduced-motion** so animations can be reduced or disabled for accessibility.


<!-- END SOURCE CONTENT -->
