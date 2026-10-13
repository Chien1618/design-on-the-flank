[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Shared State Between Overrides

Use Framer's store for state shared across multiple overrides:

```typescript
import { createStore } from "https://framer.com/m/framer/store.js@^1.0.0"

const useStore = createStore({
    variant: "default",
    count: 0,
})

export function withTrigger(Component): ComponentType {
    return (props) => {
        const [store, setStore] = useStore()

        const handleClick = () => {
            setStore({ variant: "active" })
        }

        return <Component {...props} onClick={handleClick} />
    }
}

export function withReactor(Component): ComponentType {
    return (props) => {
        const [store] = useStore()
        return <Component {...props} variant={store.variant} />
    }
}
```


<!-- END SOURCE CONTENT -->
