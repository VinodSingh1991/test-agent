# BusinessNext Border & Shadow Utilities

## Border Width

### Border Classes
- `.bd-ba-{width}` - border all sides
- `.bd-bt-{width}` - border-top
- `.bd-br-{width}` - border-right
- `.bd-bb-{width}` - border-bottom
- `.bd-bl-{width}` - border-left

Available widths: 0, 1 (0.063rem), 2 (0.125rem), 3 (0.188rem), 4 (0.25rem)

```html
<!-- All borders -->
<div class="bd-ba-1">1px border all sides</div>

<!-- Bottom border only -->
<div class="bd-bb-2">2px bottom border</div>

<!-- No border -->
<div class="bd-ba-0">No border</div>
```

## Border Radius

### CSS Variables
```css
--bnds-g-border-radius-4: 0.25rem    /* 4px */
--bnds-g-border-radius-8: 0.5rem     /* 8px */
--bnds-g-border-radius-12: 0.75rem   /* 12px */
--bnds-g-border-radius-16: 1rem      /* 16px */
--bnds-g-border-radius-20: 1.25rem   /* 20px */
--bnds-g-border-radius-circle: 100%
--bnds-g-border-radius-pill: 15rem
```

### Border Radius Classes
- `.bd-br4` - border-radius: 0.25rem
- `.bd-br8` - border-radius: 0.5rem
- `.bd-br12` - border-radius: 0.75rem
- `.bd-br16` - border-radius: 1rem
- `.bd-br20` - border-radius: 1.25rem
- `.bd-brcircle` - border-radius: 100%
- `.bd-brpill` - border-radius: 15rem

### Directional Border Radius
- `.bd-br-top-{size}` - Top corners
- `.bd-br-right-{size}` - Right corners
- `.bd-br-bottom-{size}` - Bottom corners
- `.bd-br-left-{size}` - Left corners

Available sizes: 4, 8, 12, 16, 20, circle, pill

```html
<!-- Rounded corners -->
<div class="bd-br8">Rounded corners</div>

<!-- Pill button -->
<button class="bd-brpill">Pill Button</button>

<!-- Circle avatar -->
<img class="bd-brcircle" src="avatar.jpg" alt="Avatar">

<!-- Top rounded card -->
<div class="bd-br-top-12">
  Rounded top corners only
</div>
```

## Border Styles

### All Sides
- `.bd-ba-solid` - border-style: solid
- `.bd-ba-dashed` - border-style: dashed
- `.bd-ba-dotted` - border-style: dotted
- `.bd-ba-double` - border-style: double
- `.bd-ba-none` - border-style: none
- `.bd-ba-hidden` - border-style: hidden

### Individual Sides
- `.bd-bt-{style}` - Top border style
- `.bd-br-{style}` - Right border style
- `.bd-bb-{style}` - Bottom border style
- `.bd-bl-{style}` - Left border style

```html
<!-- Dashed border -->
<div class="bd-ba-1 bd-ba-dashed">
  Dashed border
</div>

<!-- Dotted bottom border -->
<div class="bd-bb-2 bd-bb-dotted">
  Dotted bottom border
</div>
```

## Outline Utilities

### Outline Width
- `.bd-ol-{width}` - outline width
- `.bd-ol-0` - outline: 0

Available widths: 1, 2, 3, 4

### Outline Offset
- `.bd-of-{size}` - outline-offset

Available sizes: 0, 1, 2, 3, 4

### Outline Style
- `.bd-os-solid` - outline-style: solid
- `.bd-os-dashed` - outline-style: dashed
- `.bd-os-dotted` - outline-style: dotted
- `.bd-os-double` - outline-style: double
- `.bd-os-none` - outline-style: none

```html
<!-- Focus outline -->
<button class="bd-ol-2 bd-os-solid">
  Button with outline
</button>

<!-- Offset outline -->
<div class="bd-ol-2 bd-of-2">
  Outline with offset
</div>
```

## Box Shadow

### CSS Variables
```css
--bnds-g-shadow-1: 0px 0px 4px 2px rgba(0, 0, 0, 0.2)
--bnds-g-shadow-2: 0px 0px 8px 2px rgba(0, 0, 0, 0.2)
--bnds-g-shadow-3: 2px 2px 4px 2px rgba(0, 0, 0, 0.2)
--bnds-g-shadow-4: 0 1px 4px 0 rgba(0, 0, 0, 0.14)
--bnds-g-shadow-5: 4px 4px 8px 0px rgba(0, 0, 0, 0.2)
--bnds-g-shadow-6: 0 1px 2px 0 rgba(0, 0, 0, 0.10)
--bnds-g-shadow-7: 0px 3px 6px -4px rgba(0, 0, 0, 0.24)
--bnds-g-shadow-none: none
```

### Shadow Classes
- `.bd-bx-sh-1` - Small glow shadow
- `.bd-bx-sh-2` - Medium glow shadow
- `.bd-bx-sh-3` - Offset shadow
- `.bd-bx-sh-4` - Subtle shadow
- `.bd-bx-sh-5` - Strong offset shadow
- `.bd-bx-sh-6` - Minimal shadow
- `.bd-bx-sh-7` - Top shadow
- `.bd-bx-sh-none` - box-shadow: none

```html
<!-- Card with shadow -->
<div class="bd-bx-sh-4 bd-br12 bd-pa-16">
  Card with subtle shadow
</div>

<!-- Elevated element -->
<div class="bd-bx-sh-5">
  Elevated element
</div>

<!-- Remove shadow -->
<div class="bd-bx-sh-none">
  No shadow
</div>
```

## Text Shadow

### Text Shadow Classes
- `.bd-txt-sh-1` - Soft glow: 0 0 4px rgba(0,0,0,0.6)
- `.bd-txt-sh-2` - Offset shadow: 2px 2px 2px rgba(0,0,0,0.2)
- `.bd-txt-sh-3` - Similar offset
- `.bd-txt-sh-4` - Left offset: -2px 2px 0 rgba(0,0,0,0.2)
- `.bd-txt-sh-5` - Top-left: -2px -2px 1px rgba(0,0,0,0.2)

```html
<!-- Glowing text -->
<h1 class="bd-txt-sh-1">Glowing Heading</h1>

<!-- Subtle depth -->
<p class="bd-txt-sh-2">Text with depth</p>
```

## Common Patterns

```html
<!-- Card Component -->
<div class="bd-bx-sh-4 bd-br12 bd-ba-1 bd-pa-16" 
     style="border-color: var(--bnds-g-color-gray-30)">
  <h3>Card Title</h3>
  <p>Card content with shadow and rounded corners</p>
</div>

<!-- Button with Border -->
<button class="bd-ba-1 bd-brpill bd-pa-12" 
        style="border-color: var(--bnds-g-color-blue-50)">
  Outlined Button
</button>

<!-- Divider -->
<div class="bd-bb-1 bd-bb-solid bd-pb-16" 
     style="border-color: var(--bnds-g-color-gray-30)">
  Section content
</div>

<!-- Focus Ring -->
<input class="bd-ba-1 bd-br8 bd-pa-8" 
       style="outline: none; border-color: var(--bnds-g-color-gray-30)"
       onfocus="this.style.borderColor='var(--bnds-g-color-blue-50)'"
       type="text">

<!-- Elevated Card on Hover -->
<div class="bd-bx-sh-4 bd-br12"
     onmouseenter="this.classList.replace('bd-bx-sh-4', 'bd-bx-sh-5')"
     onmouseleave="this.classList.replace('bd-bx-sh-5', 'bd-bx-sh-4')">
  Hover to elevate
</div>
```

## Border Collapse (Tables)
- `.bd-bc-c` - border-collapse: collapse
- `.bd-bc-s` - border-collapse: separate

## Border Spacing (Tables)
- `.bd-bs-{size}` - border-spacing

Available sizes: 0, 1, 2, 3, 4, 8, 12

```html
<!-- Table with spacing -->
<table class="bd-bc-s bd-bs-8">
  <tr><td>Cell</td><td>Cell</td></tr>
</table>
```

## Best Practices

1. **Combine utilities**: Use border + shadow + radius together for polished components
2. **Color borders**: Set border color using inline styles with CSS variables
3. **Consistent shadows**: Use shadow-4 or shadow-6 for most cards
4. **Accessible focus**: Always provide visible focus indicators
5. **Hover states**: Increase shadow on hover for interactive elements
