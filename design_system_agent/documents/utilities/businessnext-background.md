# BusinessNext Background Utilities

## Background Attachment
- `.bd-bga-f` - background-attachment: fixed
- `.bd-bga-l` - background-attachment: local
- `.bd-bga-s` - background-attachment: scroll

```html
<!-- Parallax effect -->
<div class="bd-bga-f" 
     style="height: 500px; background-image: url('hero.jpg'); background-size: cover;">
  <h1>Fixed Background</h1>
</div>
```

## Background Clip
- `.bd-bgc-bb` - background-clip: border-box
- `.bd-bgc-pb` - background-clip: padding-box
- `.bd-bgc-cb` - background-clip: content-box
- `.bd-bgc-t` - background-clip: text (gradient text effect)

```html
<!-- Gradient text -->
<h1 class="bd-bgc-t bd-font-48" 
    style="background: linear-gradient(to right, #0176D3, #9050E9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
  Gradient Text
</h1>

<!-- Background within padding -->
<div class="bd-bgc-pb bd-pa-32" 
     style="background: var(--bnds-g-color-blue-10); border: 4px solid var(--bnds-g-color-blue-50);">
  Background stops at padding
</div>
```

## Background Image
- `.bd-bg-img-n` - background-image: none

```html
<!-- Remove background image -->
<div class="bd-bg-img-n">
  No background image
</div>
```

## Background Origin
- `.bd-bgo-bb` - background-origin: border-box
- `.bd-bgo-pb` - background-origin: padding-box
- `.bd-bgo-cb` - background-origin: content-box

```html
<!-- Background starts from content -->
<div class="bd-bgo-cb bd-pa-32" 
     style="background: url('pattern.png'); border: 4px solid black;">
  Background origin content-box
</div>
```

## Background Repeat
- `.bd-bgr-rep` - background-repeat: repeat
- `.bd-bgr-nr` - background-repeat: no-repeat
- `.bd-bgr-x` - background-repeat: repeat-x (horizontal only)
- `.bd-bgr-y` - background-repeat: repeat-y (vertical only)
- `.bd-bgr-s` - background-repeat: space
- `.bd-bgr-rou` - background-repeat: round

```html
<!-- No repeat -->
<div class="bd-bgr-nr" 
     style="background-image: url('logo.png'); height: 200px;">
</div>

<!-- Repeat horizontally -->
<div class="bd-bgr-x" 
     style="background-image: url('pattern.png'); height: 100px;">
</div>

<!-- Round (scales to fit) -->
<div class="bd-bgr-rou" 
     style="background-image: url('tile.png'); height: 300px;">
</div>
```

## Background Size
- `.bd-bgs-a` - background-size: auto
- `.bd-bgs-cov` - background-size: cover (fill container)
- `.bd-bgs-con` - background-size: contain (fit within container)

```html
<!-- Cover entire area -->
<div class="bd-bgs-cov" 
     style="background-image: url('hero.jpg'); height: 400px;">
  <h2>Hero Section</h2>
</div>

<!-- Contain image -->
<div class="bd-bgs-con bd-bgr-nr" 
     style="background-image: url('logo.png'); height: 200px; background-position: center;">
</div>
```

## Background Position
- `.bd-bgp-tl` - background-position: top left
- `.bd-bgp-t` - background-position: top
- `.bd-bgp-tr` - background-position: top right
- `.bd-bgp-l` - background-position: left
- `.bd-bgp-c` - background-position: center
- `.bd-bgp-r` - background-position: right
- `.bd-bgp-bl` - background-position: bottom left
- `.bd-bgp-b` - background-position: bottom
- `.bd-bgp-br` - background-position: bottom right

```html
<!-- Centered background -->
<div class="bd-bgp-c bd-bgr-nr" 
     style="background-image: url('icon.png'); height: 200px;">
</div>

<!-- Bottom right -->
<div class="bd-bgp-br bd-bgr-nr" 
     style="background-image: url('watermark.png'); height: 300px;">
</div>
```

## Mask Utilities

### Mask Clip
- `.bd-mc-bb` - mask-clip: border-box
- `.bd-mc-pb` - mask-clip: padding-box
- `.bd-mc-cb` - mask-clip: content-box
- `.bd-mc-fb` - mask-clip: fill-box
- `.bd-mc-sb` - mask-clip: stroke-box
- `.bd-mc-vb` - mask-clip: view-box
- `.bd-mc-nc` - mask-clip: no-clip

### Mask Composite
- `.bd-mc-a` - mask-composite: add
- `.bd-mc-s` - mask-composite: subtract
- `.bd-mc-i` - mask-composite: intersect
- `.bd-mc-e` - mask-composite: exclude

### Mask Size
- `.bd-ms-a` - mask-size: auto
- `.bd-ms-cov` - mask-size: cover
- `.bd-ms-con` - mask-size: contain

### Mask Repeat
- `.bd-ms-rep` - mask-repeat: repeat
- `.bd-ms-nr` - mask-repeat: no-repeat
- `.bd-ms-e-x` - mask-repeat: repeat-x
- `.bd-ms-r-y` - mask-repeat: repeat-y
- `.bd-ms-s` - mask-repeat: space
- `.bd-ms-rou` - mask-repeat: round

### Mask Position
- `.bd-ms-tl` - mask-position: top left
- `.bd-ms-t` - mask-position: top
- `.bd-ms-tr` - mask-position: top right
- `.bd-ms-l` - mask-position: left
- `.bd-ms-c` - mask-position: center
- `.bd-ms-r` - mask-position: right
- `.bd-ms-bl` - mask-position: bottom left
- `.bd-ms-b` - mask-position: bottom
- `.bd-ms-br` - mask-position: bottom right

### Mask Origin
- `.bd-mo-bb` - mask-origin: border-box
- `.bd-mo-pb` - mask-origin: padding-box
- `.bd-mo-cb` - mask-origin: content-box
- `.bd-mo-fb` - mask-origin: fill-box
- `.bd-mo-sb` - mask-origin: stroke-box
- `.bd-mo-vb` - mask-origin: view-box

### Mask Mode
- `.bd-mm-alp` - mask-mode: alpha
- `.bd-mm-lum` - mask-mode: luminance
- `.bd-mm-sou` - mask-mode: match-source

## Usage Examples

### Hero Section
```html
<section class="bd-bgs-cov bd-bgp-c bd-bgr-nr" 
         style="background-image: url('hero.jpg'); height: 600px; position: relative;">
  <div class="bd-pos-absolute" style="inset: 0; background: rgba(0,0,0,0.5);"></div>
  <div class="bd-pos-relative bd-d-flex bd-ai-center bd-jc-center bd-h-100">
    <div class="bd-txt-c" style="color: white;">
      <h1 class="bd-font-48 bd-mb-16">Welcome to BusinessNext</h1>
      <p class="bd-font-20">Your design system solution</p>
    </div>
  </div>
</section>
```

### Pattern Background
```html
<div class="bd-bgr-rep" 
     style="background-image: url('pattern.svg'); background-size: 50px 50px; padding: 64px;">
  <div class="bd-card bd-pa-32">
    <h2>Card on Pattern</h2>
    <p>Content with patterned background</p>
  </div>
</div>
```

### Gradient Text Effect
```html
<h1 class="bd-bgc-t bd-font-48 bd-fw-bold" 
    style="background: linear-gradient(135deg, var(--bnds-g-color-blue-50), var(--bnds-g-color-purple-50)); 
           -webkit-background-clip: text; 
           -webkit-text-fill-color: transparent;
           background-clip: text;">
  Amazing Gradient Text
</h1>
```

### Parallax Scroll
```html
<div class="bd-bga-f bd-bgs-cov bd-bgp-c" 
     style="background-image: url('parallax.jpg'); height: 500px;">
  <div class="bd-d-flex bd-ai-center bd-jc-center bd-h-100">
    <h2 style="color: white; font-size: 48px;">Parallax Effect</h2>
  </div>
</div>
<div style="background: white; padding: 64px;">
  <p>Scroll to see parallax effect</p>
</div>
```

### Image with Overlay Gradient
```html
<div class="bd-pos-relative bd-bgs-cov bd-bgp-c" 
     style="background-image: url('product.jpg'); height: 400px;">
  <div class="bd-pos-absolute" 
       style="inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);"></div>
  <div class="bd-pos-absolute bd-pa-24" style="bottom: 0; color: white;">
    <h3 class="bd-font-24">Product Name</h3>
    <p>Product description</p>
  </div>
</div>
```

### Tiled Background
```html
<div class="bd-bgr-rep" 
     style="background-image: url('tile.png'); background-size: 100px 100px; min-height: 400px; padding: 32px;">
  <div class="bd-card bd-pa-24">
    <h3>Content on Tiles</h3>
  </div>
</div>
```

### Multiple Backgrounds
```html
<div style="background-image: url('pattern.svg'), linear-gradient(135deg, var(--bnds-g-color-blue-10), var(--bnds-g-color-purple-10));
            background-size: 50px 50px, cover;
            background-repeat: repeat, no-repeat;
            padding: 64px;">
  <h2>Multiple Backgrounds</h2>
  <p>Pattern over gradient</p>
</div>
```

### Watermark
```html
<div class="bd-pos-relative bd-card bd-pa-24" style="min-height: 300px;">
  <div class="bd-pos-absolute bd-bgp-c bd-bgr-nr bd-o-10" 
       style="inset: 0; background-image: url('watermark.svg'); background-size: 200px; pointer-events: none;">
  </div>
  <div class="bd-pos-relative">
    <h3>Document Title</h3>
    <p>Content with watermark in background</p>
  </div>
</div>
```

## Best Practices

1. **Performance**: Optimize background images for web
2. **Responsive**: Use background-size: cover for responsive images
3. **Accessibility**: Ensure text has sufficient contrast over background images
4. **Loading**: Consider lazy loading for below-fold background images
5. **Fallback**: Always provide a background-color as fallback
6. **Gradients**: Combine with images for sophisticated effects
