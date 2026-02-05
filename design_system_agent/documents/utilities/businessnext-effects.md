# BusinessNext Effects & Visual Utilities

## Opacity

### Opacity Classes
- `.bd-o-100` - opacity: 1 (fully visible)
- `.bd-o-90` - opacity: 0.9
- `.bd-o-80` - opacity: 0.8
- `.bd-o-70` - opacity: 0.7
- `.bd-o-60` - opacity: 0.6
- `.bd-o-50` - opacity: 0.5
- `.bd-o-40` - opacity: 0.4
- `.bd-o-30` - opacity: 0.3
- `.bd-o-20` - opacity: 0.2
- `.bd-o-10` - opacity: 0.1
- `.bd-o-05` - opacity: 0.05
- `.bd-o-025` - opacity: 0.025
- `.bd-o-0` - opacity: 0 (invisible)

```html
<!-- Semi-transparent overlay -->
<div class="bd-o-50" style="background: black;">
  50% opacity overlay
</div>

<!-- Disabled state -->
<button class="bd-o-40" disabled>
  Disabled Button
</button>

<!-- Fade effect -->
<div class="bd-o-0" onmouseenter="this.classList.replace('bd-o-0', 'bd-o-100')">
  Hover to reveal
</div>
```

## Filters

### Blur
- `.bd-f-blr-{1-10}` - filter: blur(Npx)
- `.bd-f-none` - filter: none

```html
<!-- Blurred background -->
<div class="bd-f-blr-5">
  Blurred content
</div>
```

### Brightness
- `.bd-f-brit-10` - 10% brightness
- `.bd-f-brit-20` - 20%
- `.bd-f-brit-30` - 30%
- `.bd-f-brit-40` - 40%
- `.bd-f-brit-50` - 50%
- `.bd-f-brit-70` - 70%
- `.bd-f-brit-100` - 100% (normal)
- `.bd-f-brit-150` - 150% (brighter)
- `.bd-f-brit-200` - 200%
- `.bd-f-brit-300` - 300%

```html
<!-- Dimmed image -->
<img src="image.jpg" class="bd-f-brit-50" alt="Dimmed">

<!-- Brightened on hover -->
<img src="image.jpg" class="bd-f-brit-70" 
     onmouseenter="this.classList.replace('bd-f-brit-70', 'bd-f-brit-100')">
```

### Contrast
- `.bd-f-c-{10-300}` - filter: contrast(N%)

Values: 10, 20, 30, 40, 50, 70, 100, 150, 200, 300

```html
<!-- High contrast -->
<img src="image.jpg" class="bd-f-c-150" alt="High contrast">
```

### Grayscale
- `.bd-f-gs-{10-300}` - filter: grayscale(N%)

Values: 10, 20, 30, 40, 50, 70, 100, 150, 200, 300

```html
<!-- Black and white image -->
<img src="image.jpg" class="bd-f-gs-100" alt="Grayscale">

<!-- Partial grayscale -->
<img src="image.jpg" class="bd-f-gs-50" alt="50% grayscale">
```

### Hue Rotate
- `.bd-fhr-{degrees}` - filter: hue-rotate(Ndeg)

Values: 50, 70, 90, 100, 150, 200, 250, 300, 400, 500

```html
<!-- Color shift -->
<img src="image.jpg" class="bd-fhr-180" alt="Color shifted">
```

### Invert
- `.bd-f-i-{10-300}` - filter: invert(N%)

```html
<!-- Inverted colors -->
<div class="bd-f-i-100">
  Inverted content
</div>
```

### Saturation
- `.bd-f-sat-{1-10}` - filter: saturate(N)

```html
<!-- Vibrant colors -->
<img src="image.jpg" class="bd-f-sat-2" alt="Saturated">

<!-- Desaturated -->
<img src="image.jpg" class="bd-f-sat-5" alt="Less saturated">
```

### Sepia
- `.bd-fs-{10-300}` - filter: sepia(N%)

```html
<!-- Vintage effect -->
<img src="photo.jpg" class="bd-fs-100" alt="Sepia tone">
```

## Blend Modes

### Mix Blend Mode
- `.bd-mxb-n` - mix-blend-mode: normal
- `.bd-mxb-m` - multiply
- `.bd-mxb-scr` - screen
- `.bd-mxb-o` - overlay
- `.bd-mxb-dar` - darken
- `.bd-mxb-l` - lighten
- `.bd-mxb-cd` - color-dodge
- `.bd-mxb-cb` - color-burn
- `.bd-mxb-hl` - hard-light
- `.bd-mxb-sl` - soft-light
- `.bd-mxb-dif` - difference
- `.bd-mxb-e` - exclusion
- `.bd-mxb-h` - hue
- `.bd-mxb-sat` - saturation
- `.bd-mxb-c` - color
- `.bd-mxb-lum` - luminosity

```html
<!-- Blended overlay -->
<div style="position: relative;">
  <img src="background.jpg" alt="Background">
  <div class="bd-mxb-m" 
       style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: blue;">
  </div>
</div>
```

### Background Blend Mode
- `.bd-bgb-n` - background-blend-mode: normal
- `.bd-bgb-m` - multiply
- `.bd-bgb-scr` - screen
- `.bd-bgb-o` - overlay
- `.bd-bgb-dar` - darken
- `.bd-bgb-l` - lighten
- `.bd-bgb-cd` - color-dodge
- `.bd-bgb-cb` - color-burn
- `.bd-bgb-hl` - hard-light
- `.bd-bgb-sl` - soft-light
- `.bd-bgb-dif` - difference
- `.bd-bgb-e` - exclusion
- `.bd-bgb-h` - hue
- `.bd-bgb-sat` - saturation
- `.bd-bgb-c` - color
- `.bd-bgb-lum` - luminosity

```html
<!-- Gradient blend -->
<div class="bd-bgb-m" 
     style="background: linear-gradient(red, blue), url('texture.jpg');">
  Blended background
</div>
```

## Object Fit
- `.bd-of-contain` - object-fit: contain
- `.bd-of-cover` - object-fit: cover
- `.bd-of-fill` - object-fit: fill
- `.bd-of-none` - object-fit: none
- `.bd-of-scale-down` - object-fit: scale-down

```html
<!-- Cover image in container -->
<div class="bd-wt-320 bd-ht-240">
  <img src="image.jpg" class="bd-w-100 bd-h-100 bd-of-cover" alt="Cover">
</div>

<!-- Contain image -->
<div class="bd-wt-320 bd-ht-240">
  <img src="image.jpg" class="bd-w-100 bd-h-100 bd-of-contain" alt="Contain">
</div>
```

## Appearance
- `.bd-appearance-none` - appearance: none (remove default browser styling)
- `.bd-appearance-auto` - appearance: auto

```html
<!-- Custom styled select -->
<select class="bd-appearance-none bd-ba-1 bd-br8 bd-pa-8">
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

## Color Scheme
- `.bd-cs-n` - color-scheme: normal
- `.bd-cs-l` - color-scheme: light
- `.bd-cs-d` - color-scheme: dark
- `.bd-cs-ol` - color-scheme: only light
- `.bd-cs-od` - color-scheme: only dark
- `.bd-cs-ld` - color-scheme: light dark

```html
<!-- Force dark mode inputs -->
<div class="bd-cs-d">
  <input type="text" placeholder="Dark mode input">
</div>
```

## Accent Color
- `.bd-ac-brand` - accent-color: var(--brand)
- `.bd-ac-secondary` - accent-color: var(--brand-secondary)
- `.bd-ac-active` - accent-color: var(--active)
- `.bd-ac-red` - accent-color: var(--red)
- `.bd-ac-green` - accent-color: var(--green)

```html
<!-- Branded checkbox -->
<input type="checkbox" class="bd-ac-brand">

<!-- Custom radio -->
<input type="radio" class="bd-ac-green" checked>
```

## Usage Examples

```html
<!-- Disabled Card -->
<div class="bd-card bd-pa-16 bd-o-50 bd-f-gs-50">
  <h3>Disabled Content</h3>
  <p>This card appears disabled</p>
</div>

<!-- Image Gallery with Hover -->
<div class="bd-d-grid bd-grid-col-3 bd-grid-gap-16">
  <img src="1.jpg" class="bd-f-gs-100 bd-trans-03" 
       onmouseenter="this.classList.remove('bd-f-gs-100')"
       onmouseleave="this.classList.add('bd-f-gs-100')">
  <img src="2.jpg" class="bd-f-gs-100 bd-trans-03"
       onmouseenter="this.classList.remove('bd-f-gs-100')"
       onmouseleave="this.classList.add('bd-f-gs-100')">
  <img src="3.jpg" class="bd-f-gs-100 bd-trans-03"
       onmouseenter="this.classList.remove('bd-f-gs-100')"
       onmouseleave="this.classList.add('bd-f-gs-100')">
</div>

<!-- Blurred Background Modal -->
<div style="position: fixed; inset: 0;">
  <div class="bd-f-blr-10" 
       style="position: absolute; inset: 0; background: url('bg.jpg'); background-size: cover;">
  </div>
  <div class="bd-pos-relative bd-d-flex bd-ai-center bd-jc-center bd-vh-100">
    <div class="bd-card bd-pa-32">
      <h2>Modal Content</h2>
    </div>
  </div>
</div>

<!-- Custom File Input -->
<input type="file" class="bd-appearance-none bd-ba-1 bd-br8 bd-pa-8">
```

## Best Practices

1. **Performance**: Use filters sparingly, they can impact performance
2. **Accessibility**: Don't rely solely on opacity for disabled states
3. **Browser Support**: Check compatibility for blend modes
4. **Combine Effects**: Multiple filters can be combined but may be slow
5. **Transitions**: Add transitions for smooth filter changes
