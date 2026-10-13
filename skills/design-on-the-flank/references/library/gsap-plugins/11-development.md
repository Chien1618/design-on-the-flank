[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Development

### GSDevTools

UI for scrubbing timelines, toggling animations, and debugging. Use during development only; do not ship. Register and create an instance with a timeline reference.

```javascript
gsap.registerPlugin(GSDevTools);
GSDevTools.create({ animation: tl });
```


<!-- END SOURCE CONTENT -->
