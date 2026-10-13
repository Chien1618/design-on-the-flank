[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Do Not

- ❌ Put ScrollTrigger on a **child tween** when it's part of a timeline; put it on the **timeline** or a **top-level tween** only. Wrong: `gsap.timeline().to(".a", { scrollTrigger: {...} })`. Correct: `gsap.timeline({ scrollTrigger: {...} }).to(".a", { x: 100 })`.
- ❌ Forget to call **ScrollTrigger.refresh()** after DOM/layout changes (new content, images, fonts) that affect trigger positions; viewport resize is auto-handled, but dynamic content is not.
- ❌ Nest ScrollTriggered animations inside of a parent timeline. ScrollTriggers should only exist on top-level animations.
- ❌ Forget to **gsap.registerPlugin(ScrollTrigger)** before using ScrollTrigger.
- ❌ Use **scrub** and **toggleActions** together on the same ScrollTrigger; choose one behavior. If both exist, **scrub** wins.
- ❌ Use an ease other than **"none"** on the horizontal animation when using **containerAnimation** for fake horizontal scroll; it breaks the 1:1 scroll-to-position mapping.
- ❌ Create ScrollTriggers in random or async order without setting **refreshPriority**; refresh runs in creation order (or by refreshPriority), and wrong order can affect layout (e.g. pin spacing). Create them top-to-bottom or assign **refreshPriority** so they refresh in page order.
- ❌ Leave **markers: true** in production.
- ❌ Forget **refresh()** after layout changes (new content, images, fonts) that affect trigger positions; viewport resize is handled automatically.

### Learn More

https://gsap.com/docs/v3/Plugins/ScrollTrigger/

<!-- END SOURCE CONTENT -->
