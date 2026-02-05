# BusinessNext Spacing Utilities

## Overview
The BusinessNext Design System provides comprehensive spacing utilities for margins and padding using the `bnds` (BusinessNext Design System) prefix.

## CSS Variables

### Spacing Scale
```css
--bnds-g-spacing-0: 0rem          /* 0px */
--bnds-g-spacing-1: 0.0625rem     /* 1px */
--bnds-g-spacing-2: 0.125rem      /* 2px */
--bnds-g-spacing-4: 0.25rem       /* 4px */
--bnds-g-spacing-6: 0.375rem      /* 6px */
--bnds-g-spacing-8: 0.5rem        /* 8px */
--bnds-g-spacing-10: 0.625rem     /* 10px */
--bnds-g-spacing-12: 0.75rem      /* 12px */
--bnds-g-spacing-14: 0.875rem     /* 14px */
--bnds-g-spacing-16: 1rem         /* 16px */
--bnds-g-spacing-20: 1.25rem      /* 20px */
--bnds-g-spacing-24: 1.5rem       /* 24px */
--bnds-g-spacing-28: 1.75rem      /* 28px */
--bnds-g-spacing-32: 2rem         /* 32px */
--bnds-g-spacing-36: 2.25rem      /* 36px */
--bnds-g-spacing-40: 2.5rem       /* 40px */
--bnds-g-spacing-48: 3rem         /* 48px */
--bnds-g-spacing-56: 3.5rem       /* 56px */
--bnds-g-spacing-64: 4rem         /* 64px */
--bnds-g-spacing-80: 5rem         /* 80px */
--bnds-g-spacing-100: 6.25rem     /* 100px */
```

## Margin Utilities

### All Sides
- `.bd-ma-{size}` - Margin all sides
- Example: `.bd-ma-16` applies 1rem margin to all sides

### Individual Sides
- `.bd-mt-{size}` - Margin top
- `.bd-mb-{size}` - Margin bottom
- `.bd-ml-{size}` - Margin left
- `.bd-mr-{size}` - Margin right

### Horizontal/Vertical
- `.bd-mh-{size}` - Margin horizontal (left + right)
- `.bd-mv-{size}` - Margin vertical (top + bottom)

### Available Sizes
0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 100

### Responsive Variants (md/lg breakpoints)
- `.md:bd-ma-{size}` - Medium breakpoint (48rem / 768px)
- `.lg:bd-ma-{size}` - Large breakpoint (64rem / 1024px)

## Padding Utilities

### All Sides
- `.bd-pa-{size}` - Padding all sides
- Example: `.bd-pa-16` applies 1rem padding to all sides

### Individual Sides
- `.bd-pt-{size}` - Padding top
- `.bd-pb-{size}` - Padding bottom
- `.bd-pl-{size}` - Padding left
- `.bd-pr-{size}` - Padding right

### Horizontal/Vertical
- `.bd-ph-{size}` - Padding horizontal (left + right)
- `.bd-pv-{size}` - Padding vertical (top + bottom)

### Available Sizes
0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 100

### Responsive Variants (md/lg breakpoints)
- `.md:bd-pa-{size}` - Medium breakpoint
- `.lg:bd-pa-{size}` - Large breakpoint

## Usage Examples

```html
<!-- Card with consistent spacing -->
<div class="bd-pa-16 bd-ma-8">
  <h2 class="bd-mb-8">Card Title</h2>
  <p class="bd-mb-16">Card content with bottom margin</p>
  <button class="bd-pa-12">Click Me</button>
</div>

<!-- Responsive spacing -->
<div class="bd-pa-8 md:bd-pa-16 lg:bd-pa-24">
  Increases padding at larger screens
</div>

<!-- Horizontal/Vertical spacing -->
<div class="bd-ph-16 bd-pv-8">
  Different horizontal and vertical padding
</div>
```

## Best Practices

1. **Consistency**: Use the predefined spacing scale for consistent layouts
2. **Responsive**: Apply responsive variants for better mobile experience
3. **Composability**: Combine margin and padding utilities as needed
4. **Variables**: Use CSS variables in custom CSS: `var(--bnds-g-spacing-16)`
