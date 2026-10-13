[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## ScrollTrigger.batch()

**ScrollTrigger.batch(triggers, vars)** creates one ScrollTrigger per target and **batches** their callbacks (onEnter, onLeave, etc.) within a short interval. Use it to coordinate an animation (e.g. with staggers) for all elements that fire a similar callback around the same time — e.g. animate every element that just entered the viewport in one go. Good alternative to IntersectionObserver. Returns an Array of ScrollTrigger instances.

- **triggers**: selector text (e.g. `".box"`) or Array of elements.
- **vars**: standard ScrollTrigger config (start, end, once, callbacks, etc.). Do **not** pass `trigger` (targets are the triggers) or animation-related options: `animation`, `invalidateOnRefresh`, `onSnapComplete`, `onScrubComplete`, `scrub`, `snap`, `toggleActions`.

**Callback signature:** Batched callbacks receive **two** parameters (unlike normal ScrollTrigger callbacks, which receive the instance):
1. **targets** — Array of trigger elements that fired this callback within the interval.
2. **scrollTriggers** — Array of the ScrollTrigger instances that fired. Use for progress, direction, or `kill()`.

**Batch options in vars:**
- **interval** (Number) — Max time in seconds to collect each batch. Default is roughly one requestAnimationFrame. When the first callback of a type fires, the timer starts; the batch is delivered when the interval elapses or when **batchMax** is reached.
- **batchMax** (Number | Function) — Max elements per batch. When full, the callback fires and the next batch starts. Use a **function** that returns a number for responsive layouts; it runs on refresh (resize, tab focus, etc.).

```javascript
ScrollTrigger.batch(".box", {
  onEnter: (elements, triggers) => {
    gsap.to(elements, { opacity: 1, y: 0, stagger: 0.15 });
  },
  onLeave: (elements, triggers) => {
    gsap.to(elements, { opacity: 0, y: 100 });
  },
  start: "top 80%",
  end: "bottom 20%"
});
```

With **batchMax** and **interval** for finer control:

```javascript
ScrollTrigger.batch(".card", {
  interval: 0.1,
  batchMax: 4,
  onEnter: (batch) => gsap.to(batch, { opacity: 1, y: 0, stagger: 0.1, overwrite: true }),
  onLeaveBack: (batch) => gsap.set(batch, { opacity: 0, y: 50, overwrite: true })
});
```

See [ScrollTrigger.batch()](https://gsap.com/docs/v3/Plugins/ScrollTrigger/static.batch/) in the GSAP docs.


<!-- END SOURCE CONTENT -->
