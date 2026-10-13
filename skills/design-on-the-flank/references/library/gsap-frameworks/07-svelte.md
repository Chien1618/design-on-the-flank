[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Svelte

Use **onMount** to run GSAP after the DOM is ready. Use the **returned cleanup function** from onMount (or track the context and clean up in a reactive block / component destroy) to revert. Svelte 5 uses a different lifecycle; the same principle applies: create in “mounted” and revert in “destroyed.”

```javascript
<script>
  import { onMount } from "svelte";
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";

  let container;

  onMount(() => {
    if (!container) return;
    const ctx = gsap.context(() => {
      gsap.to(".box", { x: 100 });
      gsap.from(".item", { autoAlpha: 0, stagger: 0.1 });
    }, container);
    return () => ctx.revert();
  });
</script>

<div bind:this={container}>
  <div class="box">Box</div>
  <div class="item">Item</div>
</div>
```

- ✅ **bind:this={container}** — get a reference to the root element so you can pass it to **gsap.context(scope)**.
- ✅ **return () => ctx.revert()** — Svelte’s onMount can return a cleanup function; call **ctx.revert()** there so cleanup runs when the component is destroyed.


<!-- END SOURCE CONTENT -->
