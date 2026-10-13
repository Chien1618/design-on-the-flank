[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Do Not

- ❌ Chain animations with **delay** when a **timeline** can sequence them; prefer `gsap.timeline()` and the position parameter for multi-step animation.
- ❌ Forget to pass **defaults** (e.g. `defaults: { duration: 0.5, ease: "power2.out" }`) when many child tweens share the same duration or ease.
- ❌ Forget that **duration** on the timeline constructor is not the same as tween duration; timeline “duration” is determined by its children.
- ❌ Nest animations that contain a ScrollTrigger; ScrollTriggers should only be on top-level Tweens/Timelines.

<!-- END SOURCE CONTENT -->
