# Updates, animation, and troubleshooting

## Preserve configured instances

Read the existing file and identify the exact prop, callback, selector, animation, or binding concerned. Prefer a small change while returning the whole file to the user. Do not create replacement instances or rename media/CMS prop keys merely to make new defaults appear.

Framer can retain saved values on an existing instance. Check the saved value before assuming code is broken. A default change is not a migration of existing content. Add compatibility logic only when a requested change needs it; do not overwrite the user's configured content.

## Controls missing or stale

First check imports, exports, TypeScript errors, and that `addPropertyControls` references the exported function. Ask whether the user selected the actual code component or a wrapping frame. Compare a fresh test instance only if this helps isolate the issue and preserves the original instance.

The previous private workflow sometimes refreshed stale metadata by renaming the component function and updating its control registration. Treat this as an unverified workaround, not a documented Framer guarantee. Consider it only after reproducing stale metadata with otherwise valid code, explaining the change, and keeping the original code file, prop keys, and a backup. Do not rename by default.

## Animation and layering

Keep the existing animation model and timing unless requested otherwise. Dispose of timelines, event listeners, observers, timers, and animation frames when they are no longer needed. Scope refs and selectors per instance; do not alter global page styles casually.

For a mask or cover bug, establish which layer must be above which and which element should move. Inspect clipping and stacking contexts. Do not substitute opacity for a position or layering fix. Honor reduced motion and ensure that content remains usable without animation.

## CMS, Rive, and third-party services

Preserve CMS field mappings, selector names, ordering, Rive inputs, and trigger strings supplied by the user. DOM-based CMS extraction is fragile: document the markup dependency and avoid polling or observers unless required. If an observer is required, scope it narrowly and disconnect it.

When a feature requires a model, uploaded animation, image, service, or CMS collection, identify exactly what the user must select or supply in Framer. Show a helpful empty state. Do not fabricate a successful connection or include an API secret in browser code.

## Converting a sample

Carry over the sample's structure and behavior where compatible. Replace only what Framer requires, such as project-specific CSS imports or app routing. Explain substantive differences. Do not promise a pixel-identical result from an image alone; separate observed details from assumptions.
