[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Stagger

Offset the animation of each item by 0.1 second like this: 
```javascript 
gsap.to(".item", {
  y: -20,
  stagger: 0.1
});
```
Or use the object syntax for advanced options like how each successive stagger amount is applied to the targets array (`from: "random" | "start" | "center" | "end" | "edges" | (index)`)

### Learn More

https://gsap.com/resources/getting-started/Staggers


<!-- END SOURCE CONTENT -->
