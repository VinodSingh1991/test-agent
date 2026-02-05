# BusinessNext Interaction Utilities

## Cursor

### Cursor Classes
- `.bd-cur-a` - cursor: auto
- `.bd-cur-d` - cursor: default
- `.bd-cur-n` - cursor: none
- `.bd-cur-h` - cursor: help
- `.bd-cur-cm` - cursor: context-menu
- `.bd-cur-p` - cursor: pointer
- `.bd-cur-na` - cursor: not-allowed
- `.bd-cur-nd` - cursor: no-drop
- `.bd-cur-c` - cursor: copy
- `.bd-cur-ali` - cursor: alias
- `.bd-cur-w` - cursor: wait
- `.bd-cur-pro` - cursor: progress
- `.bd-cur-t` - cursor: text
- `.bd-cur-cro` - cursor: crosshair
- `.bd-cur-ce` - cursor: cell
- `.bd-cur-m` - cursor: move
- `.bd-cur-grb` - cursor: grab
- `.bd-cur-gbin` - cursor: grabbing

### Resize Cursors
- `.bd-cur-nr` - cursor: n-resize
- `.bd-cur-sr` - cursor: s-resize
- `.bd-cur-er` - cursor: e-resize
- `.bd-cur-wr` - cursor: w-resize
- `.bd-cur-nsr` - cursor: ns-resize
- `.bd-cur-ewr` - cursor: ew-resize
- `.bd-cur-rr` - cursor: row-resize
- `.bd-cur-cr` - cursor: col-resize
- `.bd-cur-ner` - cursor: ne-resize
- `.bd-cur-nwr` - cursor: nw-resize
- `.bd-cur-ser` - cursor: se-resize
- `.bd-cur-swr` - cursor: sw-resize
- `.bd-cur-neswr` - cursor: nesw-resize
- `.bd-cur-nwser` - cursor: nwse-resize

### Zoom Cursors
- `.bd-cur-z-i` - cursor: zoom-in
- `.bd-cur-z-o` - cursor: zoom-out

```html
<!-- Clickable element -->
<div class="bd-cur-p" onclick="alert('Clicked!')">
  Click me
</div>

<!-- Help tooltip -->
<span class="bd-cur-h" title="Need help?">
  Hover for help
</span>

<!-- Disabled button -->
<button class="bd-cur-na bd-o-50" disabled>
  Disabled
</button>

<!-- Draggable item -->
<div class="bd-cur-grb" draggable="true">
  Drag me
</div>

<!-- Resizable handle -->
<div class="bd-cur-nwser" style="position: absolute; bottom: 0; right: 0; width: 20px; height: 20px;">
  ⇲
</div>

<!-- Zoom on image -->
<img src="image.jpg" class="bd-cur-z-i" onclick="this.style.transform='scale(2)'">
```

## User Select

### User Select Classes
- `.bd-us-n` - user-select: none (prevent text selection)
- `.bd-us-t` - user-select: text (allow text selection)
- `.bd-us-al` - user-select: all (select all on click)
- `.bd-us-a` - user-select: auto

```html
<!-- Prevent selection -->
<div class="bd-us-n">
  You can't select this text
</div>

<!-- Select all on click -->
<code class="bd-us-al bd-pa-8 bd-br8" style="display: block; background: var(--bnds-g-color-gray-20);">
  npm install businessnext-design
</code>

<!-- Buttons should not be selectable -->
<button class="bd-us-n bd-pa-12 bd-br8">
  Click Me
</button>
```

## Pointer Events

### Pointer Events Classes
- `.bd-p-auto` - pointer-events: auto
- `.bd-p-none` - pointer-events: none (click-through)

```html
<!-- Disabled overlay (click-through) -->
<div style="position: relative;">
  <img src="image.jpg" alt="Image">
  <div class="bd-p-none" style="position: absolute; inset: 0; background: rgba(0,0,0,0.3);">
    Loading overlay (click-through)
  </div>
</div>

<!-- Enable interactions -->
<div class="bd-p-auto">
  Interactive content
</div>
```

## Touch Action

### Touch Action Classes
- `.bn-ta-a` - touch-action: auto
- `.bn-ta-n` - touch-action: none
- `.bn-ta-px` - touch-action: pan-x (horizontal pan only)
- `.bn-ta-pl` - touch-action: pan-left
- `.bn-ta-pr` - touch-action: pan-right
- `.bn-ta-py` - touch-action: pan-y (vertical pan only)
- `.bn-ta-pu` - touch-action: pan-up
- `.bn-ta-pd` - touch-action: pan-down
- `.bn-ta-pz` - touch-action: pinch-zoom
- `.bn-ta-m` - touch-action: manipulation

```html
<!-- Horizontal scrolling only -->
<div class="bn-ta-px bd-o-xs">
  <div style="width: 2000px;">
    Wide content - horizontal scroll only
  </div>
</div>

<!-- Vertical scrolling only -->
<div class="bn-ta-py bd-o-ys bd-ht-200">
  <div style="height: 1000px;">
    Tall content - vertical scroll only
  </div>
</div>

<!-- Prevent zoom and double-tap -->
<div class="bn-ta-m">
  Content that prevents zoom
</div>
```

## Resize

### Resize Classes
- `.bd-rs-n` - resize: none
- `.bd-rs-b` - resize: both
- `.bd-rs-v` - resize: vertical
- `.bd-rs-h` - resize: horizontal

```html
<!-- Resizable textarea -->
<textarea class="bd-rs-v bd-pa-8 bd-br8 bd-ba-1" rows="5">
  Vertically resizable textarea
</textarea>

<!-- Resizable element -->
<div class="bd-rs-b bd-ba-2 bd-pa-16" style="overflow: auto; min-width: 200px; min-height: 100px;">
  Resize me (both directions)
</div>

<!-- Non-resizable textarea -->
<textarea class="bd-rs-n bd-pa-8 bd-br8 bd-ba-1" rows="3">
  Fixed size textarea
</textarea>
```

## Clear

### Clear Classes
- `.bd-cl-l` - clear: left
- `.bd-cl-r` - clear: right
- `.bd-cl-b` - clear: both
- `.bd-cl-is` - clear: inline-start
- `.bd-cl-ie` - clear: inline-end
- `.bd-cl-n` - clear: none

```html
<!-- Float layout with clear -->
<div>
  <img src="image.jpg" style="float: left; margin-right: 16px;">
  <p>Text wraps around image...</p>
  <p class="bd-cl-l">This text clears the float</p>
</div>
```

## Usage Examples

### Interactive Card
```html
<div class="bd-card bd-pa-16 bd-cur-p bd-trans-03 bd-us-n"
     onclick="alert('Card clicked')"
     onmouseenter="this.style.transform='translateY(-4px)'"
     onmouseleave="this.style.transform='translateY(0)'">
  <h3>Clickable Card</h3>
  <p>Hover and click me</p>
</div>
```

### Draggable Item
```html
<div class="bd-card bd-pa-16 bd-cur-grb bd-us-n"
     draggable="true"
     ondragstart="this.style.opacity='0.5'"
     ondragend="this.style.opacity='1'">
  <h4>📦 Drag Me</h4>
  <p>Draggable item</p>
</div>
```

### Code Block with Select All
```html
<div class="bd-card bd-pa-0">
  <div class="bd-pa-12" style="background: var(--bnds-g-color-gray-80); color: white;">
    <div class="bd-d-flex bd-jc-between bd-ai-center">
      <span class="bd-font-12">code.js</span>
      <button class="bd-font-10 bd-pa-4 bd-br4 bd-cur-p bd-us-n"
              onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.textContent)">
        Copy
      </button>
    </div>
  </div>
  <pre class="bd-us-al bd-pa-16 bd-ma-0" style="background: var(--bnds-g-color-gray-90); color: white; overflow-x: auto;">
const greeting = 'Hello, World!'
console.log(greeting)</pre>
</div>
```

### Mobile-Friendly Carousel
```html
<div class="bn-ta-px bd-o-xs bd-d-flex bd-grid-gap-16 bd-pb-16"
     style="scroll-snap-type: x mandatory;">
  <div class="bd-card bd-pa-16" style="min-width: 280px; scroll-snap-align: start;">
    <h4>Slide 1</h4>
  </div>
  <div class="bd-card bd-pa-16" style="min-width: 280px; scroll-snap-align: start;">
    <h4>Slide 2</h4>
  </div>
  <div class="bd-card bd-pa-16" style="min-width: 280px; scroll-snap-align: start;">
    <h4>Slide 3</h4>
  </div>
</div>
```

### Disabled State
```html
<button class="bd-cur-na bd-o-50 bd-p-none bd-us-n bd-pa-12 bd-br8"
        style="background: var(--bnds-g-color-gray-40);">
  Disabled Button
</button>
```

### Loading State
```html
<div class="bd-pos-relative">
  <button class="bd-pa-12 bd-br8" disabled>
    Submit
  </button>
  <div class="bd-pos-absolute bd-cur-w" 
       style="inset: 0; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.8);">
    <span class="bd-ani-spin">⟳</span>
  </div>
</div>
```

### Image Zoom
```html
<div class="bd-o-h bd-pos-relative">
  <img src="product.jpg" 
       class="bd-cur-z-i bd-trans-03"
       style="width: 100%;"
       onmouseenter="this.style.transform='scale(1.5)'"
       onmouseleave="this.style.transform='scale(1)'">
</div>
```

### Tooltip Trigger
```html
<span class="bd-cur-h bd-pos-relative"
      onmouseenter="document.getElementById('tooltip').classList.remove('bd-d-none')"
      onmouseleave="document.getElementById('tooltip').classList.add('bd-d-none')">
  Hover me
  <span id="tooltip" 
        class="bd-d-none bd-pos-absolute bd-card bd-pa-8 bd-font-12"
        style="bottom: 100%; left: 50%; transform: translateX(-50%); margin-bottom: 8px; white-space: nowrap;">
    Helpful tooltip
  </span>
</span>
```

## Best Practices

1. **Cursor feedback**: Always provide appropriate cursor for interactive elements
2. **Touch devices**: Use touch-action to prevent unwanted gestures
3. **Accessibility**: Don't rely solely on cursor changes for interaction feedback
4. **User select**: Disable selection on buttons and UI controls
5. **Pointer events**: Use sparingly, as it affects accessibility
6. **Loading states**: Change cursor to `wait` or `progress` during async operations
