[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## framer Global Object

### Mode & Identity

```typescript
framer.mode: string                    // Current plugin mode
framer.getProjectInfo(): Promise<{ id: string; name: string }>
```

### UI Management

```typescript
framer.showUI(options?: {
    position?: "center" | "top left" | "bottom left" | "top right" | "bottom right"
    width?: number
    height?: number
    minWidth?: number
    minHeight?: number
    maxWidth?: number
    maxHeight?: number
    resizable?: boolean | "width" | "height"
}): Promise<void>

framer.hideUI(): Promise<void>

framer.closePlugin(message?: string, options?: {
    variant?: "success" | "info" | "error"
}): never
// Throws FramerPluginClosedError internally. Code after this never executes.

framer.notify(message: string, options?: {
    variant?: "info" | "success" | "warning" | "error"
    durationMs?: number | typeof Infinity
    button?: { text: string; onClick: () => void }
}): void

framer.setCloseWarning(message: string | false): Promise<void>
// Show confirmation dialog when user tries to close plugin during operations.

framer.setBackgroundMessage(message: string): void
// Status text shown while plugin UI is hidden.

framer.setMenu(items: Array<
    | { label: string; onAction: () => void; visible?: boolean }
    | { type: "separator" }
>): void
```

### Collection Access

```typescript
framer.getActiveManagedCollection(): Promise<ManagedCollection>
framer.getActiveCollection(): Promise<Collection>
framer.getManagedCollections(): Promise<ManagedCollection[]>
framer.getCollections(): Promise<Collection[]>
framer.createManagedCollection(): Promise<ManagedCollection>
```

### Canvas / Node Methods

```typescript
framer.addImage(options: {
    image: string        // URL
    name?: string
    altText?: string
}): Promise<void>

framer.setImage(options: {
    image: string
    name?: string
    altText?: string
}): Promise<void>

framer.getImage(): Promise<{ image: string; altText?: string } | null>

framer.addText(text: string): Promise<void>
framer.addFrame(): Promise<void>
framer.addSVG(svg: string, name?: string): Promise<void>  // max 10kB
framer.addComponentInstance(options: {
    url: string
    attributes?: Record<string, unknown>
}): Promise<void>

framer.getSelection(): Promise<Node[]>
framer.subscribeToSelection(callback: (selection: Node[]) => void): () => void
framer.subscribeToCanvasRoot(callback: (root: Node) => void): () => void
```

### Project-Level Plugin Data

```typescript
framer.setPluginData(key: string, value: string | null): Promise<void>
// Pass null to delete. 2kB per entry, 4kB total across all keys.

framer.getPluginData(key: string): Promise<string | null>
```

### Permissions

```typescript
framer.isAllowedTo(...methods: ProtectedMethod[]): boolean
// Synchronous check. Returns true if ALL methods are allowed.

framer.subscribeToIsAllowedTo(
    callback: (isAllowed: boolean) => void,
    ...methods: ProtectedMethod[]
): () => void
```

### Draggable Component

```typescript
import { Draggable } from "framer-plugin"

<Draggable data={{
    type: "image",
    image: "https://...",
    previewImage: "https://...",
    name: "Photo",
    altText: "Description",
}}>
    <div>Drag me</div>
</Draggable>
```

---


<!-- END SOURCE CONTENT -->
