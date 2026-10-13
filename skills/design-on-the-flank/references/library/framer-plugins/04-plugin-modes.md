[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Plugin Modes

| Mode | Purpose | `framer.mode` value |
|------|---------|---------------------|
| `canvas` | General-purpose canvas access | `"canvas"` |
| `configureManagedCollection` | CMS: first-time setup / field config | `"configureManagedCollection"` |
| `syncManagedCollection` | CMS: re-sync existing collection | `"syncManagedCollection"` |
| `image` | User picks an image | `"image"` |
| `editImage` | Edit existing image | `"editImage"` |
| `collection` | Access user-editable collections | `"collection"` |

CMS plugins use both `configureManagedCollection` + `syncManagedCollection`.


<!-- END SOURCE CONTENT -->
