# BusinessNext Animation & Transition Utilities

## CSS Animation Variables
```css
--bnds-g-ani-spin: spin
--bnds-g-ani-ping: ping
--bnds-g-ani-pulse: pulse
--bnds-g-ani-bounce: bounce
--bnds-g-ani-none: none
--bnds-g-ani-top-left: topLeft
--bnds-g-ani-top-right: topRight
--bnds-g-ani-bottom-right: bottomRight
--bnds-g-ani-bottom-left: bottomLeft
--bnds-g-ani-expand-vertical: expandVertical
--bnds-g-ani-expand-horizontal: expandHorizontal
--bnds-g-ani-fade-in: fadeIn
--bnds-g-ani-fade-out: fadeOut
```

## Animation Classes

### Spin Animation
- `.bd-ani-spin` - Rotates 360 degrees (0.3s ease-in-out)

```html
<!-- Loading spinner -->
<div class="bd-ani-spin" style="display: inline-block;">⟳</div>

<!-- Spinning icon -->
<svg class="bd-ani-spin" width="24" height="24">
  <circle cx="12" cy="12" r="10" stroke="currentColor" fill="none"/>
</svg>
```

### Ping Animation
- `.bd-ani-ping` - Scales and fades (0.3s ease-in-out)

```html
<!-- Notification dot -->
<span style="position: relative; display: inline-block;">
  <span class="bd-ani-ping" 
        style="position: absolute; width: 12px; height: 12px; background: red; border-radius: 50%;"></span>
  <span style="width: 12px; height: 12px; background: red; border-radius: 50%; display: block;"></span>
</span>
```

### Pulse Animation
- `.bd-ani-pulse` - Opacity pulses to 50% (0.3s ease-in-out)

```html
<!-- Pulsing badge -->
<span class="bd-ani-pulse bd-pa-4 bd-br8" 
      style="background: var(--bnds-g-color-red-50); color: white;">
  Live
</span>
```

### Bounce Animation
- `.bd-ani-bounce` - Bounces vertically (0.3s ease-in-out)

```html
<!-- Bouncing arrow -->
<div class="bd-ani-bounce">↓</div>
```

### Slide Animations
- `.bd-ani-top-left` - Slides in from top-left
- `.bd-ani-top-right` - Slides in from top-right
- `.bd-ani-bottom-left` - Slides in from bottom-left
- `.bd-ani-bottom-right` - Slides in from bottom-right

```html
<!-- Notification sliding from top-right -->
<div class="bd-ani-top-right bd-card bd-pa-16" 
     style="position: fixed; top: 10px; right: 10px;">
  <p>New notification!</p>
</div>

<!-- Toast from bottom-left -->
<div class="bd-ani-bottom-left bd-card bd-pa-16"
     style="position: fixed; bottom: 10px; left: 10px;">
  <p>Action completed</p>
</div>
```

### Expand Animations
- `.bd-ani-expand-vertical` - Expands height from 0 to auto
- `.bd-ani-expand-horizontal` - Expands width from 0 to auto

```html
<!-- Accordion content -->
<div class="bd-ani-expand-vertical">
  <p>This content expands vertically</p>
</div>

<!-- Sidebar expanding -->
<div class="bd-ani-expand-horizontal">
  <nav>Navigation items</nav>
</div>
```

### Fade Animations
- `.bd-ani-fade-in` - Fades from opacity 0 to 1
- `.bd-ani-fade-out` - Fades from opacity 1 to 0

```html
<!-- Appearing modal -->
<div class="bd-ani-fade-in" style="position: fixed; inset: 0; background: rgba(0,0,0,0.5);">
  <div class="bd-card bd-pa-32">
    <h2>Modal Content</h2>
  </div>
</div>

<!-- Dismissing alert -->
<div class="bd-ani-fade-out bd-card bd-pa-16">
  <p>This will fade away</p>
</div>
```

### No Animation
- `.bd-ani-none` - Removes animation

## Transition Utilities

### Transition Duration
- `.bd-trans-01` - transition: all 0.1s
- `.bd-trans-02` - transition: all 0.2s
- `.bd-trans-03` - transition: all 0.3s
- `.bd-trans-04` - transition: all 0.4s
- `.bd-trans-05` - transition: all 0.5s
- `.bd-trans-06` - transition: all 0.6s
- `.bd-trans-1` - transition: all 1s
- `.bd-trans-2` - transition: all 2s
- `.bd-trans-3` - transition: all 3s
- `.bd-trans-4` - transition: all 4s
- `.bd-trans-5` - transition: all 5s

```html
<!-- Quick transition -->
<button class="bd-trans-02" 
        style="background: blue; color: white; padding: 8px 16px;"
        onmouseenter="this.style.background='darkblue'"
        onmouseleave="this.style.background='blue'">
  Hover Me
</button>

<!-- Slow transition -->
<div class="bd-trans-1 bd-o-100"
     onmouseenter="this.classList.replace('bd-o-100', 'bd-o-50')"
     onmouseleave="this.classList.replace('bd-o-50', 'bd-o-100')">
  Slow fade
</div>
```

## Transform Utilities

### Scale
- `.bd-ts-50` - transform: scale(0.5)
- `.bd-ts-100` - transform: scale(1)
- `.bd-ts-120` - transform: scale(1.2)
- `.bd-ts-140` - transform: scale(1.4)
- `.bd-ts-none` - transform: none

```html
<!-- Scale on hover -->
<img src="image.jpg" class="bd-ts-100 bd-trans-03"
     onmouseenter="this.classList.replace('bd-ts-100', 'bd-ts-120')"
     onmouseleave="this.classList.replace('bd-ts-120', 'bd-ts-100')">
```

### Rotate
- `.bd-tr-20` - transform: rotate(20deg)
- `.bd-tr-40` - transform: rotate(40deg)
- `.bd-tr-60` - transform: rotate(60deg)
- `.bd-tr-90` - transform: rotate(90deg)
- `.bd-tr-100` - transform: rotate(100deg)
- `.bd-tr-180` - transform: rotate(180deg)
- `.bd-tr-360` - transform: rotate(360deg)

```html
<!-- Rotated icon -->
<span class="bd-tr-90">→</span>

<!-- Flip on click -->
<div class="bd-trans-03" 
     onclick="this.classList.toggle('bd-tr-180')">
  🔄 Click to flip
</div>
```

### Transform Origin
- `.bd-to-c` - transform-origin: center
- `.bd-to-t` - transform-origin: top
- `.bd-to-tr` - transform-origin: top right
- `.bd-to-r` - transform-origin: right
- `.bd-to-br` - transform-origin: bottom right
- `.bd-to-b` - transform-origin: bottom
- `.bd-to-bl` - transform-origin: bottom left
- `.bd-to-l` - transform-origin: left
- `.bd-to-tl` - transform-origin: top left

```html
<!-- Scale from corner -->
<div class="bd-to-tl bd-ts-100 bd-trans-03"
     onmouseenter="this.classList.replace('bd-ts-100', 'bd-ts-120')">
  Scales from top-left
</div>
```

### Transform Style
- `.bd-tr-sty-3d` - transform-style: preserve-3d
- `.bd-tr-sty-flat` - transform-style: flat

### Perspective
- `.bd-p-small` - perspective: 3rem
- `.bd-p-mid` - perspective: 5rem
- `.bd-p-lg` - perspective: 8rem
- `.bd-p-xl` - perspective: 12rem
- `.bd-p-none` - perspective: none

### Perspective Origin
- `.bd-po-c` - perspective-origin: center
- `.bd-po-t` - perspective-origin: top
- `.bd-po-tr` - perspective-origin: top right
- `.bd-po-ri` - perspective-origin: right
- `.bd-po-br` - perspective-origin: bottom right
- `.bd-po-b` - perspective-origin: bottom
- `.bd-po-bl` - perspective-origin: bottom left
- `.bd-po-l` - perspective-origin: left
- `.bd-po-tl` - perspective-origin: top left

### Backface Visibility
- `.bd-bf-h` - backface-visibility: hidden
- `.bd-bf-v` - backface-visibility: visible

## Usage Examples

### Interactive Card
```html
<div class="bd-card bd-pa-16 bd-trans-03 bd-ts-100"
     onmouseenter="this.classList.replace('bd-ts-100', 'bd-ts-120'); this.style.boxShadow='var(--bnds-g-shadow-7)'"
     onmouseleave="this.classList.replace('bd-ts-120', 'bd-ts-100'); this.style.boxShadow='var(--bnds-g-shadow-4)'">
  <h3>Hover to scale</h3>
  <p>This card grows on hover</p>
</div>
```

### Loading Indicator
```html
<div class="bd-d-flex bd-ai-center bd-grid-gap-8">
  <div class="bd-ani-spin" style="width: 24px; height: 24px; border: 3px solid var(--bnds-g-color-blue-50); border-top-color: transparent; border-radius: 50%;"></div>
  <span>Loading...</span>
</div>
```

### Notification Toast
```html
<div class="bd-ani-bottom-right bd-ani-fade-in bd-card bd-pa-16"
     style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
  <div class="bd-d-flex bd-ai-center bd-grid-gap-12">
    <span class="bd-ani-pulse" style="width: 8px; height: 8px; background: green; border-radius: 50%;"></span>
    <p class="bd-ma-0">Success! Action completed.</p>
  </div>
</div>
```

### Expandable Accordion
```html
<div class="bd-card">
  <button class="bd-pa-16 bd-w-100 bd-txt-l bd-trans-02"
          onclick="document.getElementById('content').classList.toggle('bd-d-none'); this.querySelector('span').classList.toggle('bd-tr-180')">
    <span class="bd-trans-03 bd-tr-0">▼</span> Click to expand
  </button>
  <div id="content" class="bd-d-none bd-ani-expand-vertical bd-pa-16 bd-bt-1">
    <p>Hidden content that expands</p>
  </div>
</div>
```

### Flip Card
```html
<div class="bd-p-mid" style="width: 300px; height: 200px;">
  <div class="bd-tr-sty-3d bd-trans-06" 
       style="position: relative; width: 100%; height: 100%;"
       onclick="this.style.transform = this.style.transform === 'rotateY(180deg)' ? '' : 'rotateY(180deg)'">
    <!-- Front -->
    <div class="bd-bf-h bd-card bd-pa-16" 
         style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden;">
      <h3>Front</h3>
    </div>
    <!-- Back -->
    <div class="bd-bf-h bd-card bd-pa-16" 
         style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; transform: rotateY(180deg);">
      <h3>Back</h3>
    </div>
  </div>
</div>
```

### Button with Multiple Effects
```html
<button class="bd-pa-12 bd-ph-24 bd-br8 bd-trans-02 bd-ts-100"
        style="background: var(--bnds-g-color-blue-50); color: white; border: none;"
        onmouseenter="this.classList.replace('bd-ts-100', 'bd-ts-120')"
        onmouseleave="this.classList.replace('bd-ts-120', 'bd-ts-100')"
        onclick="this.classList.add('bd-ani-pulse')">
  Click Me
</button>
```

## Best Practices

1. **Duration**: Use 0.2-0.3s for most UI interactions
2. **Performance**: Prefer transforms over position/size changes
3. **Accessibility**: Respect `prefers-reduced-motion` media query
4. **Consistency**: Use the same transition duration across similar elements
5. **Combine carefully**: Don't overload with multiple animations
