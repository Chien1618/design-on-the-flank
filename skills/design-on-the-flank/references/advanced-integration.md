# Three.js and GSAP inside Framer

Read alongside the Framer contract. The upstream library contains standalone web examples and setup instructions. These rules govern adapting them into one Framer TSX file; do not copy their HTML shell, npm commands or app scaffold into the user's workflow.

## Dependencies

Verify the current official API and an import pattern that works in Framer before choosing a library version. Keep Three.js core and addons on the same version and avoid duplicate React or Three.js instances. Keep GSAP core and plugins compatible. Register the plugins actually used. Name external network and asset dependencies in the handoff. Do not assume an import succeeded because syntax parsing passed.

For browser-dependent libraries, choose a Framer-supported loading pattern safe during server rendering. Guard async loading against unmount and stale props. An inaccessible CDN or model needs an error/empty state, not a permanently blank component.

## Three.js lifecycle

- Mount the renderer in an instance-owned element using a ref, never `document.body`. Read its dimensions, not the whole window. Resize from the container and update camera projection, renderer and any composer together; handle zero-sized containers.
- Create the scene in an effect. Keep stable objects in refs. Apply color, speed, lighting, camera and shader-uniform prop changes to those objects. Rebuild geometry or renderer only when necessary; release replaced resources.
- Drive animation from elapsed time or delta time. Bound device pixel ratio and particle counts. Pause or reduce work when hidden and use a suitable reduced-motion/editor state.
- On cleanup cancel animation, disconnect observers, remove listeners, detach the canvas and dispose owned geometries, materials, textures, render targets, composers and renderer resources. Do not dispose shared cached resources still used by another instance.
- Ignore or cancel stale asset loads; release late-loaded resources when no longer needed. Expose model/image URLs or Framer asset selectors with useful placeholders.
- Convert pointer coordinates relative to the component bounds. Account for touch, pointer exit and scroll. Keep essential content accessible outside a canvas.
- Handle unavailable WebGL and context loss with a useful fallback. Validate two instances and remounting without leaking canvases or GPU work.

## GSAP lifecycle

- In React, use `useGSAP` when its compatible import is available, or a carefully scoped effect with `gsap.context`. Scope selectors to the instance root.
- Revert the instance context on cleanup. Use `contextSafe` or explicit cleanup for animations created later by handlers. Avoid global `killAll`, global selectors and killing another instance's timeline.
- Declare dependencies deliberately. For rebuilt animations, revert previous state before reconstruction (`revertOnUpdate` where appropriate). Preserve progress if the requested interaction requires it. Controls must update the running effect, not only initial construction.
- Prefer transforms and opacity where appropriate. Avoid React rerendering on every frame. Animate Three.js object values/uniforms directly and retain one deliberate render-loop owner.
- Use reduced-motion branches that still show the content. Clean up media-query contexts and event listeners.

## Scroll and text

Use the actual scroll container in Framer Preview. Scope triggers, start/end values and pin targets to the component. Pinning needs enough scroll space and may affect surrounding layout; explain required section sizing. Do not hijack page scrolling without a request.

Refresh layout measurements after relevant fonts, images or content settle. Throttle refreshes; never refresh on every render or frame. Use readable static content in Canvas if Preview scrolling is needed for the effect.

When splitting text, retain accessible reading order, restore original DOM on cleanup and rebuild only when content/font/layout changes demand it. Verify the selected plugin API against its current official documentation.

## Known source correction: horizontal scroll

The imported GSAP ScrollTrigger horizontal-scroll example contains `Max.max` (undefined), mixes pixel distance with `xPercent`, and omits `scrub` from its code despite describing scrubbed scrolling. Do not copy it verbatim. For a left-moving overflow strip, derive a pixel distance from its own container, for example `x: () => -Math.max(0, strip.scrollWidth - viewport.clientWidth)`, use `ease: "none"`, enable `scrub` on the parent ScrollTrigger, and refresh/invalidate measurements when layout changes. Derive scroll distance and pin layout from the actual component. Preserve source excerpts for traceability; apply this correction when generating code.

## Checks for an advanced component

Change an exposed speed, color and effect setting after insertion. Check two instances, resize, removal/reinsertion, missing asset, reduced motion and Preview scrolling. For 3D, check no duplicate canvas/loop and reasonable mobile performance. For GSAP, check no orphan triggers or altered neighboring components. If these cannot be exercised, say precisely which checks remain.
