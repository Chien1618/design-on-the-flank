[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Scroll

### ScrollToPlugin

Animates scroll position (window or a scrollable element). Use for “scroll to element” or “scroll to position” without ScrollTrigger.

```javascript
gsap.registerPlugin(ScrollToPlugin);

gsap.to(window, { duration: 1, scrollTo: { y: 500 } });
gsap.to(window, { duration: 1, scrollTo: { y: "#section", offsetY: 50 } });
gsap.to(scrollContainer, { duration: 1, scrollTo: { x: "max" } });
```

**ScrollToPlugin — key config (scrollTo object):**

| Option | Description |
|--------|-------------|
| `x`, `y` | Target scroll position (number), or `"max"` for maximum |
| `element` | Selector or element to scroll to (for scroll-into-view) |
| `offsetX`, `offsetY` | Offset in pixels from the target position |

### ScrollSmoother

Smooth scroll wrapper (smooths native scroll). Requires ScrollTrigger and a specific DOM structure (content wrapper + smooth wrapper). Use when smooth, momentum-style scroll is needed. See GSAP docs for setup; register after ScrollTrigger. DOM structure would look like: 

```html
<body>
	<div id="smooth-wrapper">
		<div id="smooth-content">
			<!--- ALL YOUR CONTENT HERE --->
		</div>
	</div>
	<!-- position: fixed elements can go outside --->
</body>
```


<!-- END SOURCE CONTENT -->
