[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Context-Safe Callbacks

If GSAP-related objects get created inside functions that run AFTER the useGSAP executes (like pointer event handlers) they won't get reverted on unmount/re-render because they're not in the context. Use **contextSafe** (from useGSAP) for those functions:

```javascript
const container = useRef();
const badRef = useRef();
const goodRef = useRef();

useGSAP((context, contextSafe) => {
	// ✅ safe, created during execution
	gsap.to(goodRef.current, { x: 100 });

	// ❌ DANGER! This animation is created in an event handler that executes AFTER useGSAP() executes. It's not added to the context so it won't get cleaned up (reverted). The event listener isn't removed in cleanup function below either, so it persists between component renders (bad).
	badRef.current.addEventListener('click', () => {
		gsap.to(badRef.current, { y: 100 });
	});

	// ✅ safe, wrapped in contextSafe() function
	const onClickGood = contextSafe(() => {
		gsap.to(goodRef.current, { rotation: 180 });
	});

	goodRef.current.addEventListener('click', onClickGood);

	// 👍 we remove the event listener in the cleanup function below.
	return () => {
		// <-- cleanup
		goodRef.current.removeEventListener('click', onClickGood);
	};
},{ scope: container });
```


<!-- END SOURCE CONTENT -->
