[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Dependency array, scope, and revertOnUpdate

By default, useGSAP() passes an empty dependency array to the internal useEffect()/useLayoutEffect() so that it doesn't get called on every render. The 2nd argument is optional; it can pass either a dependency array (like useEffect()) or a config object for more flexibility:

```javascript
useGSAP(() => {
		// gsap code here, just like in a useEffect()
},{ 
  dependencies: [endX], // dependency array (optional)
  scope: container,     // scope selector text (optional, recommended)
  revertOnUpdate: true  // causes the context to be reverted and the cleanup function to run every time the hook re-synchronizes (when any dependency changes)
});
```


<!-- END SOURCE CONTENT -->
