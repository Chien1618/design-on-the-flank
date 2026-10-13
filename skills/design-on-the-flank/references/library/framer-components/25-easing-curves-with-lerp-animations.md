[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Easing Curves with Lerp Animations

**Problem:** Exponential lerp (`value += diff * speed`) naturally gives ease-out. Need to track initial distance to implement other curves.

**Solution:** Track `initialDiff` when animation starts:

```typescript
const animated = useRef({
    property: {
        current: 0,
        target: 0,
        initialDiff: 0,  // Track for easing calculations
    }
})

// When target changes, store initial distance
const updateTarget = (newTarget) => {
    const entry = animated.current.property
    entry.initialDiff = Math.abs(newTarget - entry.current)
    entry.target = newTarget
}

// Apply easing in animation loop
const applyEasing = (easingCurve) => {
    const v = animated.current.property
    const diff = v.target - v.current
    let speed = 0.05  // Base speed

    if (easingCurve !== "ease-out") {
        // Calculate progress: 0 at start, 1 near target
        const diffMagnitude = Math.abs(diff)
        const progress = v.initialDiff > 0
            ? Math.max(0, Math.min(1, 1 - (diffMagnitude / v.initialDiff)))
            : 1

        if (easingCurve === "ease-in") {
            // Start slow, end fast (cubic)
            speed *= (0.05 + Math.pow(progress, 3) * 10)
        } else if (easingCurve === "ease-in-out") {
            // Slow-fast-slow (smootherstep)
            const smoothed = progress * progress * progress *
                (progress * (progress * 6 - 15) + 10)
            speed *= (0.2 + smoothed * 3)
        }
    }
    // ease-out: use default exponential decay

    v.current += diff * speed
}
```

**Why aggressive curves?**
Exponential lerp naturally slows down approaching target. To create noticeable ease-in, need extreme multipliers (0.05x → 10x) to overcome the natural decay.

**Property control:**
```typescript
easingCurve: {
    type: ControlType.Enum,
    title: "Easing Curve",
    options: ["ease-out", "ease-in", "ease-in-out"],
    optionTitles: ["Ease Out", "Ease In", "Ease In/Out"],
    defaultValue: "ease-out",
}
```

<!-- END SOURCE CONTENT -->
