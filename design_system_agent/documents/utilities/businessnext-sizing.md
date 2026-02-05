# BusinessNext Sizing & Width Utilities

## Sizing System

### CSS Variables
```css
--bnds-g-sizing-0: 0rem           /* 0px */
--bnds-g-sizing-1: 0.0625rem      /* 1px */
--bnds-g-sizing-2: 0.125rem       /* 2px */
--bnds-g-sizing-4: 0.25rem        /* 4px */
--bnds-g-sizing-6: 0.375rem       /* 6px */
--bnds-g-sizing-8: 0.5rem         /* 8px */
--bnds-g-sizing-10: 0.625rem      /* 10px */
--bnds-g-sizing-12: 0.75rem       /* 12px */
--bnds-g-sizing-14: 0.875rem      /* 14px */
--bnds-g-sizing-16: 1rem          /* 16px */
--bnds-g-sizing-20: 1.25rem       /* 20px */
--bnds-g-sizing-24: 1.5rem        /* 24px */
--bnds-g-sizing-28: 1.75rem       /* 28px */
--bnds-g-sizing-32: 2rem          /* 32px */
--bnds-g-sizing-36: 2.25rem       /* 36px */
--bnds-g-sizing-40: 2.5rem        /* 40px */
--bnds-g-sizing-48: 3rem          /* 48px */
--bnds-g-sizing-56: 3.5rem        /* 56px */
--bnds-g-sizing-64: 4rem          /* 64px */
--bnds-g-sizing-80: 5rem          /* 80px */
--bnds-g-sizing-100: 6.25rem      /* 100px */
--bnds-g-sizing-120: 7.5rem       /* 120px */
--bnds-g-sizing-160: 10rem        /* 160px */
--bnds-g-sizing-200: 12.5rem      /* 200px */
--bnds-g-sizing-240: 15rem        /* 240px */
--bnds-g-sizing-320: 20rem        /* 320px */
--bnds-g-sizing-480: 30rem        /* 480px */
```

## Width Utilities

### Fixed Width (Token-based)
- `.bd-wt-{size}` - width
- `.bd-min-wt-{size}` - min-width
- `.bd-max-wt-{size}` - max-width

Available sizes: 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 100, 120, 160, 200, 240, 320, 480

```html
<!-- Fixed width container -->
<div class="bd-wt-320">
  320px wide container
</div>

<!-- Max width constraint -->
<div class="bd-max-wt-480">
  Maximum 480px wide
</div>
```

### Percentage Width
- `.bd-w-{percent}` - width percentage
- `.bd-min-w-{percent}` - min-width percentage
- `.bd-max-w-{percent}` - max-width percentage

Available percentages: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

```html
<!-- Half width -->
<div class="bd-w-50">50% width</div>

<!-- Full width -->
<div class="bd-w-100">100% width</div>

<!-- Minimum width -->
<div class="bd-min-w-30">Minimum 30% width</div>
```

### Viewport Width
- `.bd-vw-{percent}` - Viewport width percentage

```html
<!-- 50% of viewport width -->
<div class="bd-vw-50">50vw width</div>

<!-- Full viewport width -->
<div class="bd-vw-100">100vw width</div>
```

### Special Width Values
- `.bd-w-auto` - width: auto
- `.bd-w-content` - width: content
- `.bd-w-min-content` - width: min-content
- `.bd-w-max-content` - width: max-content
- `.bd-w-fit-content` - width: fit-content
- `.bd-w-fill-available` - width: -webkit-fill-available

### Calculated Width
- `.bd-w-100-{1-10}` - calc(100% - {n}rem)

```html
<!-- 100% minus 1rem -->
<div class="bd-w-100-1">
  Takes full width minus 1rem
</div>

<!-- 100% minus 4rem -->
<div class="bd-w-100-4">
  Takes full width minus 4rem
</div>
```

## Height Utilities

### Fixed Height (Token-based)
- `.bd-ht-{size}` - height
- `.bd-min-ht-{size}` - min-height
- `.bd-max-ht-{size}` - max-height

Available sizes: 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 100, 120, 160, 200, 240, 320, 480

```html
<!-- Fixed height -->
<div class="bd-ht-64">
  64px tall element
</div>

<!-- Minimum height -->
<div class="bd-min-ht-200">
  Minimum 200px height
</div>
```

### Percentage Height
- `.bd-h-{percent}` - height percentage
- `.bd-min-h-{percent}` - min-height percentage
- `.bd-max-h-{percent}` - max-height percentage

Available percentages: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

```html
<!-- Half height -->
<div class="bd-h-50">50% height</div>

<!-- Full height -->
<div class="bd-h-100">100% height</div>
```

### Viewport Height
- `.bd-vh-{percent}` - Viewport height
- `.bd-h-svh-{percent}` - Small viewport height
- `.bd-h-lvh-{percent}` - Large viewport height
- `.bd-h-dvh-{percent}` - Dynamic viewport height

```html
<!-- Full viewport height -->
<section class="bd-vh-100">
  Full screen section
</section>

<!-- Mobile-safe viewport height -->
<div class="bd-h-dvh-100">
  Dynamic viewport height (respects mobile browsers)
</div>
```

### Calculated Height
- `.bd-h-100-{1-10}` - calc(100% - {n}rem)

```html
<!-- 100% height minus header -->
<main class="bd-h-100-4">
  Content area accounting for header
</main>
```

## Aspect Ratio Utilities
- `.bd-ar-1x1` - aspect-ratio: 1/1 (square)
- `.bd-ar-2x1` - aspect-ratio: 2/1
- `.bd-ar-3x1` - aspect-ratio: 3/1
- `.bd-ar-4x1` - aspect-ratio: 4/1
- `.bd-ar-5x1` - aspect-ratio: 5/1
- `.bd-ar-3x2` - aspect-ratio: 3/2
- `.bd-ar-3x4` - aspect-ratio: 3/4
- `.bd-ar-4x3` - aspect-ratio: 4/3
- `.bd-ar-5x4` - aspect-ratio: 5/4
- `.bd-ar-16x9` - aspect-ratio: 16/9 (widescreen)
- `.bd-ar-21x9` - aspect-ratio: 21/9 (ultrawide)
- `.bd-ar-32x9` - aspect-ratio: 32/9 (super ultrawide)

```html
<!-- Square image container -->
<div class="bd-ar-1x1">
  <img src="avatar.jpg" alt="Avatar">
</div>

<!-- Video container -->
<div class="bd-ar-16x9">
  <iframe src="video.mp4"></iframe>
</div>
```

## Usage Examples

```html
<!-- Card with fixed dimensions -->
<div class="bd-wt-320 bd-ht-240">
  Fixed size card
</div>

<!-- Responsive container -->
<div class="bd-w-100 bd-max-wt-480 bd-h-auto">
  Mobile-first, max-width container
</div>

<!-- Full-screen hero -->
<section class="bd-w-100 bd-vh-100 bd-d-flex bd-ai-center bd-jc-center">
  <h1>Hero Content</h1>
</section>

<!-- Image with aspect ratio -->
<div class="bd-w-100 bd-ar-16x9">
  <img src="banner.jpg" class="bd-w-100 bd-h-100" style="object-fit: cover;">
</div>

<!-- Sidebar layout -->
<div class="bd-d-flex">
  <aside class="bd-wt-240 bd-min-ht-100">
    Sidebar
  </aside>
  <main class="bd-flex-1">
    Main content
  </main>
</div>
```

## Best Practices

1. **Use tokens for consistency**: Prefer token-based sizing (`bd-wt-*`, `bd-ht-*`) for UI elements
2. **Responsive sizing**: Combine percentage widths with max-width constraints
3. **Viewport units**: Use viewport units for full-screen sections
4. **Aspect ratios**: Apply aspect ratios to media containers for consistent layouts
5. **Min/Max constraints**: Always set min/max values for flexible layouts
