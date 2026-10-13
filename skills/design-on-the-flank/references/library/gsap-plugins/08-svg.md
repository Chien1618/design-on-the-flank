[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## SVG

### DrawSVG (DrawSVGPlugin)

Reveals or hides the stroke of SVG elements by animating `stroke-dashoffset` / `stroke-dasharray`. Works on `<path>`, `<line>`, `<polyline>`, `<polygon>`, `<rect>`, `<ellipse>`. Use when “drawing” or “erasing” strokes.

**drawSVG value:** Describes the **visible segment** of the stroke along the path (start and end positions), not “animate from A to B over time.” Format: `"start end"` in percent or length. Examples: `"0% 100%"` = full stroke; `"20% 80%"` = stroke only between 20% and 80% (gaps at both ends). The tween animates from the element’s **current** segment to the **target** segment — e.g. `gsap.to("#path", { drawSVG: "0% 100%" })` goes from whatever it is now to full stroke. Single value (e.g. `0`, `"100%"`) means start is 0: `"100%"` is equivalent to `"0% 100%"`. 

**Required:** The element must have a visible stroke — set `stroke` and `stroke-width` in CSS or as SVG attributes; otherwise nothing is drawn.

```javascript
gsap.registerPlugin(DrawSVGPlugin);

// draw from nothing to full stroke
gsap.from("#path", { duration: 1, drawSVG: 0 });
// or explicit segment: from 0–0 to 0–100%
gsap.fromTo("#path", { drawSVG: "0% 0%" }, { drawSVG: "0% 100%", duration: 1 });
// stroke only in the middle (gaps at ends)
gsap.to("#path", { duration: 1, drawSVG: "20% 80%" });
```

**Caveats:** Only affects stroke (not fill). Prefer single-segment `<path>` elements; multi-segment paths can render oddly in some browsers. Contents of `<use>` cannot be visually changed. **DrawSVGPlugin.getLength(element)** and **DrawSVGPlugin.getPosition(element)** return stroke length and current position.

**Learn more:** [DrawSVG](https://gsap.com/docs/v3/Plugins/DrawSVGPlugin)

### MorphSVG (MorphSVGPlugin)

Morphs one SVG shape into another by animating the `d` attribute (path data). Start and end shapes do not need the same number of points — MorphSVG converts to cubic beziers and adds points as needed. Use for icon-to-icon morphs, shape transitions, or path-based animations. Works on `<path>`, `<polyline>`, and `<polygon>`; `<circle>`, `<rect>`, `<ellipse>`, and `<line>` are converted internally or via **MorphSVGPlugin.convertToPath(selector | element)** (replaces the element in the DOM with a `<path>`).

**morphSVG value:** Can be a **selector** (e.g. `"#lightning"`), an **element**, **raw path data** (e.g. `"M47.1,0.8 73.3,0.8..."`), or for polygon/polyline a **points string** (e.g. `"240,220 240,70 70,70 70,220"`). For full config use the **object form** with **shape** as the only required property.

```javascript
gsap.registerPlugin(MorphSVGPlugin);

// convert primitives to path first if needed:
MorphSVGPlugin.convertToPath("circle, rect, ellipse, line");

gsap.to("#diamond", { duration: 1, morphSVG: "#lightning", ease: "power2.inOut" });
// object form:
gsap.to("#diamond", {
  duration: 1,
  morphSVG: { shape: "#lightning", type: "rotational", shapeIndex: 2 }
});

```

**MorphSVG — key config (morphSVG object):**

| Option | Description |
|--------|-------------|
| **shape** | _(Required.)_ Target shape: selector, element, or raw path string. |
| **type** | `"linear"` (default) or `"rotational"`. Rotational uses angle/length interpolation and can avoid kinks mid-morph; try it when linear looks wrong. |
| **map** | How segments are matched: `"size"` (default), `"position"`, or `"complexity"`. Use when start/end segments don’t line up; if none work, split into multiple paths and morph each. |
| **shapeIndex** | Offsets which point in the start path maps to the first point in the end path (avoids shape “crossing over” or inverting). Number for single-segment paths; **array** for multi-segment (e.g. `[5, 1, -8]`). Negative reverses that segment. Use **shapeIndex: "log"** once to log the auto-calculated value, then paste the number/array into the tween. **findShapeIndex(start, end)** (separate utility) provides an interactive UI to find a good value. Only applies to closed paths. |
| **smooth** | (v3.14+). Adds smoothing points. Number (e.g. `80`), `"auto"`, or object: `{ points: 40 \| "auto", redraw: true \| false, persist: true \| false }`. `redraw: false` keeps original anchors (perfect fidelity, less even spacing). `persist: false` removes added points when the tween ends. Use when the default morph looks jagged or unnatural. |
| **curveMode** | Boolean (v3.14+). Interpolates control-handle angle/length instead of raw x/y to avoid kinks on curves. Try if a morph has a mid-morph kink. |
| **origin** | Rotation origin for **type: "rotational"**. String: `"50% 50%"` (default) or `"20% 60%, 35% 90%"` for different start/end origins. |
| **precision** | Decimal places for output path data; default `2`. |
| **precompile** | Array of precomputed path strings (or use **precompile: "log"** once, copy from console). Skips expensive startup calculations; use for very complex morphs. Only for `<path>` (convert polygon/polyline first). |
| **render** | Function(rawPath, target) called each update — e.g. draw to canvas. RawPath is an array of segments (each segment = array of alternating x,y cubic bezier coords). |
| **updateTarget** | When using **render** (e.g. canvas-only), set **updateTarget: false** so the original `<path>` is not updated. **MorphSVGPlugin.defaultUpdateTarget** sets default. |

**Utilities:** **MorphSVGPlugin.convertToPath(selector | element)** converts circle/rect/ellipse/line/polygon/polyline to `<path>` in the DOM. **MorphSVGPlugin.rawPathToString(rawPath)** and **stringToRawPath(d)** convert between path strings and raw arrays. The plugin stores the original `d` on the target (e.g. for tweening back: `morphSVG: "#originalId"` or the same element).

**Tips:** For twisted or inverted morphs, set **shapeIndex** (use `"log"` or findShapeIndex()). For multi-segment paths, **shapeIndex** is an array (one value per segment). Precompile only when the first frame is slow; it does not fix jank during the tween (simplify the SVG or reduce size if needed).

**Learn more:** [MorphSVG](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin)

### MotionPath (MotionPathPlugin)

Animates an element along an SVG path. Use when moving an object along a path (e.g. a curve or custom route).

```javascript
gsap.registerPlugin(MotionPathPlugin);

gsap.to(".dot", {
  duration: 2,
  motionPath: { path: "#path", align: "#path", alignOrigin: [0.5, 0.5] }
});
```

**MotionPath — key config (motionPath object):**

| Option | Description |
|--------|-------------|
| `path` | SVG path element, selector, or path data string |
| `align` | Path element or selector to align the target to |
| `alignOrigin` | `[x, y]` origin (0–1); default `[0.5, 0.5]` |
| `autoRotate` | Rotate element to follow path tangent |
| `curviness` | 0–2; path smoothing |

### MotionPathHelper

Visual editor for MotionPath (alignment, offset). Use during development to tune path alignment.

```javascript
gsap.registerPlugin(MotionPathPlugin, MotionPathHelperPlugin);

const helper = MotionPathHelper.create(".dot", "#path", { end: 0.5 });
// adjust in UI, then use helper.path or helper.getProgress() in your animation
```


<!-- END SOURCE CONTENT -->
