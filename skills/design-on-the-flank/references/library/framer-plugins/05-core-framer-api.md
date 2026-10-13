[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Core framer API

### UI Management

```typescript
framer.showUI({ position?, width, height, minWidth?, minHeight?, maxWidth?, resizable? })
framer.hideUI()
framer.closePlugin(message?, { variant: "success" | "error" | "info" })  // returns never
framer.notify(message, { variant?, durationMs?, button?: { text, onClick } })
framer.setCloseWarning(message | false)  // warn before closing during sync
framer.setBackgroundMessage(message)     // status while plugin runs hidden
framer.setMenu([{ label, onAction, visible? }, { type: "separator" }])
```

- `closePlugin` throws `FramerPluginClosedError` internally — always ignore in catch blocks
- `showUI` should be called in `useLayoutEffect` to avoid flicker

### Properties

- `framer.mode` — current mode string

### Collection Access

```typescript
framer.getActiveManagedCollection()    // → Promise<ManagedCollection>
framer.getActiveCollection()           // → Promise<Collection> (unmanaged)
framer.getManagedCollections()          // → Promise<ManagedCollection[]>
framer.getCollections()                // → Promise<Collection[]>
framer.createManagedCollection()       // → Promise<ManagedCollection>
```

### Canvas Methods (canvas mode)

```typescript
framer.addImage({ image, name, altText })
framer.setImage({ image, name, altText })
framer.getImage()
framer.addText(text)
framer.addFrame()
framer.addSVG(svg, name)              // max 10kB
framer.addComponentInstance({ url, attributes? })
framer.getSelection()
framer.subscribeToSelection(callback)
```


<!-- END SOURCE CONTENT -->
