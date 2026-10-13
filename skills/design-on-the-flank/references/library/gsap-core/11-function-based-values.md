[Topic index](index.md)

Source excerpt. Read the package Framer integration rules before adapting code.

<!-- BEGIN SOURCE CONTENT -->
## Function-based values
Use a function for a `vars` value and it will get called **once for each target** the first time the tween renders, and whatever is returned by that function will be used as the animation value.

```javascript
gsap.to(".item", {
  x: (i, target, targetsArray) => i * 50, // first item animates to 0, the second to 50, the third to 100, etc.
  stagger: 0.1
});
```


<!-- END SOURCE CONTENT -->
