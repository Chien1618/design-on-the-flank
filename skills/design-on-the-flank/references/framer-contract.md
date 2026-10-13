# Framer component contract

## One-file delivery

Use React 18-compatible code as required by the current Framer component documentation; avoid React 19-only APIs unless Framer explicitly adds support. Include every helper and style needed for the component in its TSX file. Avoid project-specific aliases, local CSS imports, Tailwind build dependencies, environment variables, and assumed files next to the component. React and Framer are platform imports; other dependencies must be checked and named.

Do not add `@framerDisableUnlink` by default: it changes sharing behavior and is not needed to make a component run. Only produce overrides, plugins, or page-wide custom code when that is the user's actual request.

## Visual settings

Build a small mapping before implementation: visible label → prop → rendered effect. Remove controls that do nothing.

Use the appropriate documented control type for editable text, numbers, colors, toggles, fonts, images, options, or repeatable content. Set sensible ranges for numeric values. Keep runtime fallback values aligned with the control defaults. Retain meaningful values such as `0`, `false`, and an intentionally empty string; do not replace them using truthiness-based fallback logic.

When a font control is offered, apply the returned font style object instead of extracting only its family. When an image control returns a responsive image object, handle its `src`, `srcSet`, and alternative text as appropriate. Do not use the whole object as a URL string. Re-check current Framer documentation for unfamiliar control shapes rather than guessing.

## Layout and rendering

Choose sizing behavior based on the component's content. Keep intrinsic dimensions useful for first insertion. Pass Framer's incoming `style` through to the outer element so the user's sizing choices can take effect. Avoid fixed dimensions deep inside the layout that defeat responsive behavior.

Use CSS for layout and responsive text where possible. Scope any CSS to the component so two instances and unrelated page elements do not interfere. Do not impose the original author's typography or breakpoint preset on every user.

Avoid accessing `window`, `document`, or browser-only constructors at module evaluation or during a server render. Use guarded effects for browser-only work. Avoid random or time-dependent initial markup that creates hydration mismatches.

Only branch on Canvas versus Preview when there is a reason, such as keeping a continuous animation still while editing. Explain any visible difference. Offer a useful editor placeholder for content that requires data or user interaction.

## Interaction

Use actual buttons and links for their respective behaviors. Provide keyboard operation and accessible names. Scope IDs to the instance, such as with React `useId` when needed. Avoid hover-only access to essential content. For animation, include a reduced-motion path and clean up resources.

## Sources

Checked 2026-10-13. Use these official references for API details; this file records the project's delivery conventions.

- [Code Components](https://www.framer.com/developers/components-introduction)
- [Property Controls](https://www.framer.com/developers/property-controls)
- [Auto-Sizing](https://www.framer.com/developers/auto-sizing)
- [Asset Sharing](https://www.framer.com/developers/component-sharing)
