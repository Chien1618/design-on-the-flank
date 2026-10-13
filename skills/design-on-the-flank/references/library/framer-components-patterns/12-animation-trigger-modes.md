[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Animation Trigger Modes

```typescript
// On Load - triggers immediately
useEffect(() => {
    if (props.triggerOnLoad && !hasTriggered) {
        setHasTriggered(true)
        setTriggerTime(Date.now())
    }
}, [])

// On Scroll - triggers when visible
useEffect(() => {
    if (props.triggerOnLoad) return

    const observer = new IntersectionObserver(
        ([entry]) => {
            if (entry.isIntersecting && !hasTriggered) {
                setHasTriggered(true)
                setTriggerTime(Date.now())
            }
        },
        { threshold: 0.1 }
    )

    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
}, [props.triggerOnLoad, hasTriggered])
```


<!-- END SOURCE CONTENT -->
