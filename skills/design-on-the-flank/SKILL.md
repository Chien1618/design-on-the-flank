---
name: design-on-the-flank
description: Build complex Framer Code Components with Three.js, WebGL shaders, GSAP timelines, scroll animation, and working Property Controls. Convert or repair existing components and deliver one complete paste-ready TSX file. Includes on-demand references for Framer overrides and plugins when explicitly requested.
metadata:
  version: "0.2.0"
---

# Design on the Flank

Create the component the user describes. Common requests include interactive 3D scenes, particle fields, shader effects, scroll stories, and animated typography. Speak the user's language and explain insertion in everyday words.

## Read only what the task needs

1. Read [Framer contract](references/framer-contract.md) for component work.
2. Choose a route below. Open its index, then only the topic files needed. Never read the entire library or source manifest to begin a task.
3. For Three.js or GSAP, also read [Framer integration](references/advanced-integration.md). Source examples are reference material; standalone app setup must be adapted to Framer.
4. For edits, read the current component and [updates and effects](references/updates-and-effects.md).
5. Before delivery, follow [verification](references/verification.md). Report checks actually performed.

| Need | Start here |
|---|---|
| Component, layout, override | [Framer components](references/library/framer-components/index.md) |
| Editable controls | [Property Controls](references/library/framer-components-property-controls/index.md) |
| Framer patterns, CMS, shader examples | [Framer topics](references/catalog.md#framer) |
| Three.js scene, model, material, particles, shader, interaction | [Three.js topics](references/catalog.md#threejs) |
| GSAP animation, timeline, scroll, React, plugins, performance | [GSAP topics](references/catalog.md#gsap) |
| Framer plugin explicitly requested | [Plugin topics](references/catalog.md#plugins) |

A combined request can use multiple routes. For a scroll-controlled 3D scene, select scene setup, the relevant Three.js topic, GSAP React and ScrollTrigger. Do not load all topics under those routes.

## Component output

- Return one complete `.tsx` per component. Include imports, helpers, styles, exported component, sensible runtime defaults, layout annotations and `addPropertyControls` on that component.
- Every advertised control must change the visible result or behavior. Keep existing prop keys and saved settings when editing. Use defaults that display something useful without optional assets.
- Do not scaffold an app or ask the user to install npm packages, use a terminal, or assemble snippets. Verify and disclose external imports and required assets. One file does not mean dependency-free.
- Do not simplify an advanced request into a basic card or button. If a requested effect is infeasible in Framer, explain the concrete constraint and propose the closest practical behavior.
- Guard browser APIs, handle loading/errors, scope effects per instance, support reduced motion and clean up resources.
- Return complete code, never ellipses or just a patch. With file tools, provide the file; with chat only, use one complete TSX code block.
- Explain where to paste, which settings to change, required assets and what was checked. Never claim code runs in Framer unless actually tested there.

## Existing work and other outputs

Read supplied code before modifying it. Preserve the export, prop names, callbacks, CMS selectors, Rive inputs, timing and animation mechanism unless the request requires a change. Explain meaningful conversion changes. Ask for missing source before claiming to preserve it.

Overrides and plugins have different output requirements. Use those references only when requested; a Framer plugin is not a code component that can be pasted into a page.

## Chat-only access

When local files are unavailable, use the public URLs in the supplied knowledge index. Open only the relevant index and topics. If links cannot be opened, ask for the exact linked topic file or the named module download. Never claim the whole library is loaded from an index alone.

## Handoff

Give short steps: open the Framer project → create a code file in Assets → replace starter code with the complete TSX → add the component → change settings → open Preview. If it fails, ask for the exact error and complete current code, then return the corrected whole file. This skill does not authorize publishing a website.
