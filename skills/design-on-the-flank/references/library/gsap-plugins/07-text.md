[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Text

### SplitText

Splits an element’s text into characters, words, and/or lines (each in its own element) for staggered or per-unit animation. Use when animating text character-by-character, word-by-word, or line-by-line. Returns an instance with **chars**, **words**, **lines** (and **masks** when `mask` is set). Restore original markup with **revert()** or let **gsap.context()** revert. Integrates with **gsap.context()**, **matchMedia()**, and **useGSAP()**. API: **SplitText.create(target, vars)** (target = selector, element, or array).

```javascript
gsap.registerPlugin(SplitText);

const split = SplitText.create(".heading", { type: "words, chars" });
gsap.from(split.chars, { opacity: 0, y: 20, stagger: 0.03, duration: 0.4 });
// later: split.revert() or let gsap.context() cleanup revert
```

With **onSplit()** (v3.13.0+), animations run on each split and on re-split when **autoSplit** is used; returning a tween/timeline from **onSplit()** lets SplitText clean up and sync progress on re-split:

```javascript
SplitText.create(".split", {
  type: "lines",
  autoSplit: true,
  onSplit(self) {
    return gsap.from(self.lines, { y: 100, opacity: 0, stagger: 0.05, duration: 0.5 });
  }
});
```

**SplitText — key config (SplitText.create vars):**

| Option | Description |
|--------|-------------|
| **type** | Comma-separated: `"chars"`, `"words"`, `"lines"`. Default `"chars,words,lines"`. Only split what is needed (e.g. `"words, chars"` if not using lines) for performance. Avoid chars-only without words/lines or use **smartWrap: true** to prevent odd line breaks. |
| **charsClass**, **wordsClass**, **linesClass** | CSS class on each split element. Append `"++"` to add an incremented class (e.g. `linesClass: "line++"` → `line1`, `line2`, …). |
| **aria** | `"auto"` (default), `"hidden"`, or `"none"`. Accessibility: `"auto"` adds `aria-label` on the split element and `aria-hidden` on line/word/char elements so screen readers read the label; `"hidden"` hides all from readers; `"none"` leaves aria unchanged. Use `"none"` plus a screen-reader-only duplicate if nested links/semantics must be exposed. |
| **autoSplit** | When `true`, reverts and re-splits when fonts finish loading or when the element width changes (and lines are split), avoiding wrong line breaks. **Animations must be created inside onSplit()** so they target the newly split elements; **return** the animation from **onSplit()** for automatic cleanup and time-sync on re-split. |
| **onSplit(self)** | Callback when split completes (and on each re-split if **autoSplit** is `true`). Receives the SplitText instance. Returning a GSAP tween or timeline enables automatic revert/sync of that animation when re-splitting. |
| **mask** | `"lines"`, `"words"`, or `"chars"`. Wraps each unit in an extra element with `overflow: clip` for mask/reveal effects. Only one type; access wrappers on the instance’s **masks** array (or use class `-mask` if a class is set). |
| **tag** | Wrapper element tag; default `"div"`. Use `"span"` for inline (note: transforms like rotation/scale may not render on inline elements in some browsers). |
| **deepSlice** | When `true` (default), nested elements (e.g. `<strong>`) that span multiple lines are subdivided so lines don’t stretch vertically. Only applies when splitting lines. |
| **ignore** | Selector or element(s) to leave unsplit (e.g. `ignore: "sup"`). |
| **smartWrap** | When splitting **chars** only, wraps words in a `white-space: nowrap` span to avoid mid-word line breaks. Ignored if words or lines are split. Default `false`. |
| **wordDelimiter** | Word boundary: string (default `" "`), RegExp, or `{ delimiter: RegExp, replaceWith: string }` for custom splitting (e.g. zero-width joiner for hashtags, or non-Latin). |
| **prepareText(text, parent)** | Function that receives raw text and parent element; return modified text before splitting (e.g. to insert break markers for languages without spaces). |
| **propIndex** | When `true`, adds a CSS variable with index on each split element (e.g. `--word: 1`, `--char: 2`). |
| **reduceWhiteSpace** | Collapse consecutive spaces; default `true`. From v3.13.0 also honors line breaks and can insert `<br>` for `<pre>`. |
| **onRevert** | Callback when the instance is reverted. |

**Tips:** Split only what is animated (e.g. skip chars if only animating words). For custom fonts, split after they load (e.g. `document.fonts.ready.then(...)`) or use **autoSplit: true** with **onSplit()**. To avoid kerning shift when splitting chars, use CSS `font-kerning: none; text-rendering: optimizeSpeed;`. Avoid `text-wrap: balance`; it can interfere with splitting. SplitText does not support SVG `<text>`.

**Learn more:** [SplitText](https://gsap.com/docs/v3/Plugins/SplitText/)

### ScrambleText

Animates text with a scramble/glitch effect. Use when revealing or transitioning text with a scramble.

```javascript
gsap.registerPlugin(ScrambleTextPlugin);

gsap.to(".text", {
  duration: 1,
  scrambleText: { text: "New message", chars: "01", revealDelay: 0.5 }
});
```


<!-- END SOURCE CONTENT -->
