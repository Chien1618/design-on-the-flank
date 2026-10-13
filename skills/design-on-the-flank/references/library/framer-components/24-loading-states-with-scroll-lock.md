[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Loading States with Scroll Lock

**Pattern:** Show loading overlay and prevent page scroll until content is ready.

```typescript
const [isLoading, setIsLoading] = useState(true)
const [fadeOut, setFadeOut] = useState(false)

// Prevent scroll while loading (published site only)
useEffect(() => {
    const isPublished = RenderTarget.current() !== "CANVAS"
    if (!isPublished || !isLoading) return

    const originalOverflow = document.body.style.overflow
    document.body.style.overflow = "hidden"

    return () => {
        document.body.style.overflow = originalOverflow
    }
}, [isLoading])

// Two-phase hide: fade-out → remove from DOM
const hideLoader = () => {
    setFadeOut(true)
    setTimeout(() => setIsLoading(false), 300) // Match CSS transition
}
```

**Scroll to top on load** (fixes variant sequence issues):
```typescript
useEffect(() => {
    const isPublished = RenderTarget.current() !== "CANVAS"
    if (isPublished) {
        window.scrollTo(0, 0)
    }
}, [])
```


<!-- END SOURCE CONTENT -->
