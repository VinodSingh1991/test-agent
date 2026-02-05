# BusinessNext Overflow & Scroll Utilities

## Overflow

### Basic Overflow
- `.bd-o-a` - overflow: auto
- `.bd-o-h` - overflow: hidden
- `.bd-o-c` - overflow: clip
- `.bd-o-v` - overflow: visible
- `.bd-o-s` - overflow: scroll

### Overflow X (Horizontal)
- `.bd-o-xa` - overflow-x: auto
- `.bd-o-xh` - overflow-x: hidden
- `.bd-o-xc` - overflow-x: clip
- `.bd-o-xv` - overflow-x: visible
- `.bd-o-xs` - overflow-x: scroll

### Overflow Y (Vertical)
- `.bd-o-ya` - overflow-y: auto
- `.bd-o-yh` - overflow-y: hidden
- `.bd-o-yc` - overflow-y: clip
- `.bd-o-yv` - overflow-y: visible
- `.bd-o-ys` - overflow-y: scroll

```html
<!-- Scrollable container -->
<div class="bd-o-a bd-ht-200">
  <p>Long content that scrolls...</p>
</div>

<!-- Horizontal scroll -->
<div class="bd-o-xa bd-o-yh bd-wt-320">
  <div style="width: 1000px;">
    Wide content
  </div>
</div>

<!-- Hide overflow -->
<div class="bd-o-h bd-ht-100">
  <p>Content is clipped</p>
</div>
```

## Scroll Utilities

### Scroll Margin
- `.bd-scroll-m-{size}` - scroll-margin
- `.bd-scroll-mt-{size}` - scroll-margin-top
- `.bd-scroll-mr-{size}` - scroll-margin-right
- `.bd-scroll-mb-{size}` - scroll-margin-bottom
- `.bd-scroll-ml-{size}` - scroll-margin-left
- `.bd-scroll-mb-{size}` - scroll-margin-block
- `.bd-scroll-mbe-{size}` - scroll-margin-block-end
- `.bd-scroll-mbs-{size}` - scroll-margin-block-start
- `.bd-scroll-mi-{size}` - scroll-margin-inline
- `.bd-scroll-mie-{size}` - scroll-margin-inline-end
- `.bd-scroll-mis-{size}` - scroll-margin-inline-start

Available sizes: 0, 8, 16, 20, 32, 48

```html
<!-- Scroll with margin offset -->
<div id="section" class="bd-scroll-mt-16">
  Content with scroll margin
</div>
```

### Scroll Padding
- `.bd-scroll-p-{size}` - scroll-padding
- `.bd-scroll-pt-{size}` - scroll-padding-top
- `.bd-scroll-pr-{size}` - scroll-padding-right
- `.bd-scroll-pb-{size}` - scroll-padding-bottom
- `.bd-scroll-pl-{size}` - scroll-padding-left
- `.bd-scroll-p-block-{size}` - scroll-padding-block
- `.bd-scroll-p-block-end-{size}` - scroll-padding-block-end
- `.bd-scroll-p-block-start-{size}` - scroll-padding-block-start
- `.bd-scroll-p-inline-{size}` - scroll-padding-inline
- `.bd-scroll-p-inline-end-{size}` - scroll-padding-inline-end
- `.bd-scroll-p-inline-start-{size}` - scroll-padding-inline-start

Available sizes: 0, 8, 16, 20, 32, 48

```html
<!-- Scroll container with padding -->
<div class="bd-o-a bd-scroll-p-16">
  <div>Scrollable content</div>
</div>
```

### Scroll Snap Align
- `.bd-scroll-sa-sa-s` - scroll-snap-align: start
- `.bd-scroll-sa-sa-e` - scroll-snap-align: end
- `.bd-scroll-sa-sa-c` - scroll-snap-align: center
- `.bd-scroll-sa-sa-n` - scroll-snap-align: none

```html
<!-- Snap to start -->
<div class="bd-scroll-sa-sa-s">
  Snaps to start of container
</div>
```

### Scroll Behavior
- `.bd-scroll-sb-sb-a` - scroll-behavior: auto
- `.bd-scroll-sb-sb-s` - scroll-behavior: smooth

```html
<!-- Smooth scrolling container -->
<div class="bd-scroll-sb-sb-s bd-o-a bd-ht-400">
  <div id="target" class="bd-mt-320">Target section</div>
</div>
```

### Scroll Snap Type
- `.bd-scroll-st-n` - scroll-snap-type: none
- `.bd-scroll-st-xm` - scroll-snap-type: x mandatory
- `.bd-scroll-st-ym` - scroll-snap-type: y mandatory
- `.bd-scroll-st-bom` - scroll-snap-type: both mandatory
- `.bd-scroll-st-blm` - scroll-snap-type: block mandatory
- `.bd-scroll-st-im` - scroll-snap-type: inline mandatory

```html
<!-- Horizontal snap scroll -->
<div class="bd-scroll-st-xm bd-o-xs bd-d-flex bd-fw-nowrap">
  <div class="bd-scroll-sa-sa-s" style="min-width: 100%;">Slide 1</div>
  <div class="bd-scroll-sa-sa-s" style="min-width: 100%;">Slide 2</div>
  <div class="bd-scroll-sa-sa-s" style="min-width: 100%;">Slide 3</div>
</div>
```

### Scroll Snap Stop
- `.bd-scroll-ss-n` - scroll-snap-stop: normal
- `.bd-scroll-ss-a` - scroll-snap-stop: always

```html
<!-- Force stop at each item -->
<div class="bd-scroll-ss-a bd-scroll-sa-sa-s">
  Item that forces stop
</div>
```

## Custom Scrollbar

### Slim Scroll
- `.slim-scroll` - Custom thin scrollbar with hover effect

```html
<!-- Container with custom scrollbar -->
<div class="slim-scroll bd-o-a bd-ht-320">
  <p>Content with custom slim scrollbar</p>
  <p>Scrollbar appears on hover</p>
</div>
```

## Usage Examples

### Scrollable Card Body
```html
<div class="bd-card">
  <div class="bd-card-heading bd-pa-16">
    <h3>Long Content</h3>
  </div>
  <div class="bd-card-body bd-o-a bd-max-ht-240 bd-pa-16">
    <p>Scrollable content...</p>
    <p>More content...</p>
    <p>Even more content...</p>
  </div>
</div>
```

### Horizontal Scrolling List
```html
<div class="bd-o-xa bd-o-yh bd-d-flex bd-grid-gap-16 bd-pb-8">
  <div class="bd-wt-200 bd-ht-160 bd-card bd-pa-16" style="flex-shrink: 0;">Item 1</div>
  <div class="bd-wt-200 bd-ht-160 bd-card bd-pa-16" style="flex-shrink: 0;">Item 2</div>
  <div class="bd-wt-200 bd-ht-160 bd-card bd-pa-16" style="flex-shrink: 0;">Item 3</div>
  <div class="bd-wt-200 bd-ht-160 bd-card bd-pa-16" style="flex-shrink: 0;">Item 4</div>
</div>
```

### Image Carousel with Snap
```html
<div class="bd-scroll-st-xm bd-scroll-sb-sb-s bd-o-xs bd-d-flex bd-fw-nowrap bd-o-yh" 
     style="scroll-snap-type: x mandatory;">
  <img src="1.jpg" class="bd-scroll-sa-sa-c" style="min-width: 100%; scroll-snap-align: center;">
  <img src="2.jpg" class="bd-scroll-sa-sa-c" style="min-width: 100%; scroll-snap-align: center;">
  <img src="3.jpg" class="bd-scroll-sa-sa-c" style="min-width: 100%; scroll-snap-align: center;">
</div>
```

### Modal with Scrollable Content
```html
<div class="bd-pos-fixed" style="inset: 0; background: rgba(0,0,0,0.5); z-index: 1000;">
  <div class="bd-d-flex bd-ai-center bd-jc-center bd-vh-100 bd-pa-16">
    <div class="bd-card bd-max-ht-90 bd-d-flex bd-fd-column" style="max-height: 90vh; width: 600px;">
      <div class="bd-card-heading bd-pa-16 bd-bb-1">
        <h3>Modal Title</h3>
      </div>
      <div class="bd-card-body bd-o-a bd-pa-16">
        <p>Long scrollable content...</p>
        <!-- More content -->
      </div>
      <div class="bd-card-footer bd-pa-16 bd-bt-1">
        <button>Close</button>
      </div>
    </div>
  </div>
</div>
```

### Sticky Header with Scroll
```html
<div class="bd-o-a bd-vh-100">
  <div class="bd-pos-sticky bd-top-0" style="background: white; z-index: 10;">
    <h2 class="bd-pa-16">Sticky Header</h2>
  </div>
  <div class="bd-pa-16">
    <p>Scrollable content...</p>
    <!-- Long content -->
  </div>
</div>
```

### Infinite Scroll Container
```html
<div class="bd-o-a bd-ht-400 slim-scroll" 
     onscroll="if(this.scrollTop + this.clientHeight >= this.scrollHeight - 100) { console.log('Load more') }">
  <div class="bd-pa-16">
    <!-- Content items -->
    <div class="bd-card bd-pa-16 bd-mb-16">Item 1</div>
    <div class="bd-card bd-pa-16 bd-mb-16">Item 2</div>
    <div class="bd-card bd-pa-16 bd-mb-16">Item 3</div>
  </div>
</div>
```

### Table with Fixed Header
```html
<div class="bd-o-a bd-max-ht-320">
  <table class="bd-table">
    <thead class="bd-pos-sticky bd-top-0" style="background: white;">
      <tr>
        <th class="bd-pa-8">Name</th>
        <th class="bd-pa-8">Email</th>
        <th class="bd-pa-8">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr><td class="bd-pa-8">John</td><td class="bd-pa-8">john@example.com</td><td class="bd-pa-8">Active</td></tr>
      <!-- More rows -->
    </tbody>
  </table>
</div>
```

## Best Practices

1. **Mobile scrolling**: Use `-webkit-overflow-scrolling: touch` for iOS
2. **Accessibility**: Ensure scrollable regions are keyboard accessible
3. **Scroll indicators**: Show visual cues for scrollable content
4. **Performance**: Use `overflow: hidden` instead of `visibility` when possible
5. **Snap points**: Use scroll-snap for better UX in carousels and galleries
6. **Custom scrollbars**: Test cross-browser compatibility
