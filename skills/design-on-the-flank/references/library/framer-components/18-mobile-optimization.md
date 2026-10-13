[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Mobile Optimization

For particle systems and heavy animations:
- Implement resize debouncing (500ms default)
- Add size change threshold (15% minimum)
- Handle orientation changes with dedicated listener
- Use `touchAction: "none"` to prevent scroll interference


<!-- END SOURCE CONTENT -->
