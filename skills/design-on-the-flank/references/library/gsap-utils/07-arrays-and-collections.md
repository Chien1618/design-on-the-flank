[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Arrays and Collections

### selector(scope)

Returns a scoped selector function that finds elements only within the given element (or ref). Use in components so selectors like `".box"` match only descendants of that component, not the whole document. Accepts a DOM element or a ref (e.g. React ref; handles `.current`).

```javascript
const q = gsap.utils.selector(containerRef);
q(".box");        // array of .box elements inside container
gsap.to(q(".circle"), { x: 100 });
```

### toArray(value, scope?)

Converts a value to an array: selector string (scoped to element), NodeList, HTMLCollection, single element, or array. Use when passing mixed inputs to GSAP (e.g. targets) and a true array is needed.

```javascript
gsap.utils.toArray(".item");           // array of elements
gsap.utils.toArray(".item", container); // scoped to container
gsap.utils.toArray(nodeList);          // [ ... ] from NodeList
```

### pipe(...functions)

Composes functions: **pipe(f1, f2, f3)(value)** returns f3(f2(f1(value))). Use when applying a chain of transforms (e.g. normalize → mapRange → snap) in a tween or callback.

```javascript
const fn = gsap.utils.pipe(
  (v) => gsap.utils.normalize(0, 100, v),
  (v) => gsap.utils.snap(0.1, v)
);
fn(50); // normalized then snapped
```

### wrap(min, max, value?)

Wraps a value into the range min–max (inclusive min, exclusive max). Use for infinite scroll or cyclic values. Omit **value** to get a function: `wrap(min, max)(value)`.

```javascript
gsap.utils.wrap(0, 360, 370);  // 10
gsap.utils.wrap(0, 360, -10);   // 350

let wrapFn = gsap.utils.wrap(0, 360);
wrapFn(370); // 10
```

### wrapYoyo(min, max, value?)

Wraps value in range with a yoyo (bounces at ends). Use for back-and-forth within a range. Omit **value** to get a function: `wrapYoyo(min, max)(value)`.

```javascript
gsap.utils.wrapYoyo(0, 100, 150); // 50 (bounces back)

let wrapY = gsap.utils.wrapYoyo(0, 100);
wrapY(150); // 50
```


<!-- END SOURCE CONTENT -->
