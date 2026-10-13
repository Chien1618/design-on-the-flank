[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## CMS Content Timing

CMS content loads asynchronously after hydration. Processing sequence:
1. SSR: Placeholder content
2. Hydration: React attaches
3. CMS Load: Real content (~50-200ms)

Add delay before processing CMS data:
```typescript
useEffect(() => {
    if (isClient && props.children) {
        const timer = setTimeout(() => {
            processContent(props.children)
        }, 100)
        return () => clearTimeout(timer)
    }
}, [isClient, props.children])
```


<!-- END SOURCE CONTENT -->
