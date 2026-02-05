# BusinessNext Typography Utilities

## Font Family
The BusinessNext Design System uses **Poppins** as the primary font family.

### Font Weight Classes
- `.bd-ff-light` - Font weight 300
- `.bd-ff-normal` - Font weight 400
- `.bd-ff-semibold` - Font weight 500
- `.bd-ff-bold` - Font weight 600
- `.bd-ff-bolder` - Font weight 900

### Font Weight Utilities
- `.bd-fw-light` - 300
- `.bd-fw-regular` - 400
- `.bd-fw-medium` - 500
- `.bd-fw-semibold` - 600
- `.bd-fw-bold` - 700
- `.bd-fw-bolder` - 800

## Font Sizes

### CSS Variables
```css
--bnds-g-font-size-10: 0.625rem   /* 10px */
--bnds-g-font-size-12: 0.75rem    /* 12px */
--bnds-g-font-size-14: 0.875rem   /* 14px */
--bnds-g-font-size-16: 1rem       /* 16px */
--bnds-g-font-size-20: 1.25rem    /* 20px */
--bnds-g-font-size-24: 1.5rem     /* 24px */
--bnds-g-font-size-28: 1.75rem    /* 28px */
--bnds-g-font-size-32: 2rem       /* 32px */
--bnds-g-font-size-36: 2.25rem    /* 36px */
--bnds-g-font-size-40: 2.5rem     /* 40px */
--bnds-g-font-size-48: 3rem       /* 48px */
```

### Font Size Classes
- `.bd-font-10` - 0.625rem (10px)
- `.bd-font-12` - 0.75rem (12px)
- `.bd-font-14` - 0.875rem (14px) - Default body size
- `.bd-font-16` - 1rem (16px)
- `.bd-font-20` - 1.25rem (20px)
- `.bd-font-24` - 1.5rem (24px)
- `.bd-font-28` - 1.75rem (28px)
- `.bd-font-32` - 2rem (32px)
- `.bd-font-36` - 2.25rem (36px)
- `.bd-font-40` - 2.5rem (40px)
- `.bd-font-48` - 3rem (48px)

## Headings

### Heading Classes
- `.bd-h1`, `<h1>` - 2.25rem (36px), font-weight: 600
- `.bd-h2`, `<h2>` - 1.75rem (28px), font-weight: 600
- `.bd-h3`, `<h3>` - 1.5rem (24px), font-weight: 600
- `.bd-h4`, `<h4>` - 1.25rem (20px), font-weight: 600
- `.bd-h5`, `<h5>` - 1rem (16px), font-weight: 600
- `.bd-h6`, `<h6>` - 0.875rem (14px), font-weight: 600

All headings have line-height: 1

## Line Height

### CSS Variables
```css
--bnds-g-line-height-1: 1
--bnds-g-line-height-2: 1.25
--bnds-g-line-height-3: 1.375
--bnds-g-line-height-4: 1.5
--bnds-g-line-height-5: 1.75
--bnds-g-line-height-6: 2
--bnds-g-line-height-7: 2.25
--bnds-g-line-height-8: 2.5
```

### Line Height Classes
- `.bd-lh-1` - line-height: 1
- `.bd-lh-2` - line-height: 1.25
- `.bd-lh-3` - line-height: 1.375
- `.bd-lh-4` - line-height: 1.5
- `.bd-lh-5` - line-height: 1.75
- `.bd-lh-6` - line-height: 2
- `.bd-lh-7` - line-height: 2.25
- `.bd-lh-8` - line-height: 2.5

## Text Utilities

### Text Alignment
- `.bd-txt-l` - text-align: left
- `.bd-txt-c` - text-align: center
- `.bd-txt-r` - text-align: right

### Text Transform
- `.bd-txt-t-u` - text-transform: uppercase
- `.bd-txt-t-l` - text-transform: lowercase
- `.bd-txt-t-c` - text-transform: capitalize

### Text Decoration
- `.bd-txt-d-u` - text-decoration: underline
- `.bd-txt-d-lt` - text-decoration: line-through
- `.bd-txt-d-o` - text-decoration: overline
- `.bd-txt-d-n` - text-decoration: none

### Text Decoration Style
- `.bd-txt-ds-solid` - text-decoration-style: solid
- `.bd-txt-ds-dashed` - text-decoration-style: dashed
- `.bd-txt-ds-dotted` - text-decoration-style: dotted
- `.bd-txt-ds-double` - text-decoration-style: double
- `.bd-txt-ds-wavy` - text-decoration-style: wavy

### Letter Spacing
- `.bd-ls-tighter` - letter-spacing: -0.05em
- `.bd-ls-tight` - letter-spacing: -0.025em
- `.bd-ls-normal` - letter-spacing: 0
- `.bd-ls-wide` - letter-spacing: 0.025em
- `.bd-ls-wider` - letter-spacing: 0.05em
- `.bd-ls-widest` - letter-spacing: 0.1em

### White Space
- `.bd-ws-normal` - white-space: normal
- `.bd-ws-nowrap` - white-space: nowrap
- `.bd-ws-pre` - white-space: pre
- `.bd-ws-pre-line` - white-space: pre-line
- `.bd-ws-pre-wrap` - white-space: pre-wrap

### Word Break
- `.bd-wb-normal` - word-break: normal
- `.bd-wb-break-all` - word-break: break-all
- `.bd-wb-keep-all` - word-break: keep-all

### Text Truncation
- `.bd-truncate` - Single line truncate with ellipsis
- `.bd-truncate-all` - Truncate all child elements

### Line Clamp
- `.bd-ln-clamp-1` - Clamp to 1 line
- `.bd-ln-clamp-2` - Clamp to 2 lines
- `.bd-ln-clamp-3` - Clamp to 3 lines
- `.bd-ln-clamp-4` - Clamp to 4 lines
- `.bd-ln-clamp-5` - Clamp to 5 lines

## Usage Examples

```html
<!-- Heading with custom styling -->
<h1 class="bd-h1 bd-txt-c bd-mb-16">Welcome to BusinessNext</h1>

<!-- Paragraph with line height -->
<p class="bd-font-14 bd-lh-4">
  This is body text with comfortable line height for readability.
</p>

<!-- Truncated text -->
<p class="bd-truncate" style="width: 200px;">
  This is a very long text that will be truncated with ellipsis
</p>

<!-- Multi-line clamp -->
<div class="bd-ln-clamp-3">
  This text will be clamped to 3 lines maximum, with an ellipsis at the end if it overflows.
</div>

<!-- Uppercase label -->
<span class="bd-font-12 bd-txt-t-u bd-ls-wide">Label</span>

<!-- Styled link -->
<a href="#" class="bd-txt-d-u bd-txt-ds-dashed">Dashed underline link</a>
```

## Semantic Elements

### Links
- `.bd-a`, `<a>` - Blue color, underlined

### Strong/Bold
- `.bd-b`, `.bd-strong`, `<b>`, `<strong>` - font-weight: 600

### Code
- `.bd-code`, `<code>` - Blue background, inline code styling

### Keyboard
- `.bd-kbd`, `<kbd>` - Keyboard input styling with shadow

### Blockquote
- `.bd-blockquote`, `<blockquote>` - Left border, indented

### Delete
- `.bd-del`, `<del>` - Line-through with red color
