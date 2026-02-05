# BusinessNext Layout Utilities

## Display Utilities

### Display Classes
- `.bd-d-block` - display: block
- `.bd-d-inline-block` - display: inline-block
- `.bd-d-inline` - display: inline
- `.bd-d-none` - display: none
- `.bd-d-flex` - display: flex
- `.bd-d-inline-flex` - display: inline-flex
- `.bd-d-grid` - display: grid
- `.bd-d-inline-grid` - display: inline-grid
- `.bd-d-table` - display: table
- `.bd-d-table-cell` - display: table-cell

### Responsive Display
- `.md:bd-d-{type}` - Medium breakpoint (768px)
- `.lg:bd-d-{type}` - Large breakpoint (1024px)

## Flexbox Utilities

### Flex Direction
- `.bd-fd-row` - flex-direction: row
- `.bd-fd-row-reverse` - flex-direction: row-reverse
- `.bd-fd-column` - flex-direction: column
- `.bd-fd-column-reverse` - flex-direction: column-reverse

### Flex Wrap
- `.bd-fw-nowrap` - flex-wrap: nowrap
- `.bd-fw-wrap` - flex-wrap: wrap
- `.bd-fw-wrap-reverse` - flex-wrap: wrap-reverse

### Justify Content
- `.bd-jc-start` - justify-content: flex-start
- `.bd-jc-end` - justify-content: flex-end
- `.bd-jc-center` - justify-content: center
- `.bd-jc-between` - justify-content: space-between
- `.bd-jc-around` - justify-content: space-around
- `.bd-jc-evenly` - justify-content: space-evenly

### Align Items
- `.bd-ai-flex-start` - align-items: flex-start
- `.bd-ai-flex-end` - align-items: flex-end
- `.bd-ai-center` - align-items: center
- `.bd-ai-baseline` - align-items: baseline
- `.bd-ai-stretch` - align-items: stretch

### Align Self
- `.bd-as-auto` - align-self: auto
- `.bd-as-flex-start` - align-self: flex-start
- `.bd-as-flex-end` - align-self: flex-end
- `.bd-as-center` - align-self: center
- `.bd-as-stretch` - align-self: stretch

### Flex Grow/Shrink
- `.bd-fg-{0-12}` - flex-grow values from 0 to 12
- `.bd-fs-{0-5}` - flex-shrink values from 0 to 5
- `.bd-flex-{0-12}` - flex property values
- `.bd-flex-n` - flex: none

## Grid System

### Grid Templates
- `.bd-grid-col-{1-12}` - Grid columns (1-12)
- `.bd-grid-row-{1-12}` - Grid rows (1-12)

### Grid Gap
- `.bd-grid-gap-{size}` - gap property
- `.bd-grid-col-gap-{size}` - column-gap
- `.bd-grid-row-gap-{size}` - row-gap

Available gap sizes: 0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32

### Grid Auto Flow
- `.bd-grid-flow-row` - grid-auto-flow: row
- `.bd-grid-flow-col` - grid-auto-flow: column
- `.bd-grid-flow-dense` - grid-auto-flow: dense

### Grid Alignment
- `.bd-grid-justify-start` - justify-items: start
- `.bd-grid-justify-center` - justify-items: center
- `.bd-grid-justify-end` - justify-items: end
- `.bd-grid-justify-stretch` - justify-items: stretch

## 12-Column Grid

### Row Container
- `.bd-row` - Creates a flex row container

### Column Classes
- `.bd-col` - Flexible column (flex: 1)
- `.bd-col-size-{1-12}` - Fixed width columns

Width percentages:
- `.bd-col-size-1`: 8.33% (1/12)
- `.bd-col-size-2`: 16.67% (2/12)
- `.bd-col-size-3`: 25% (3/12)
- `.bd-col-size-4`: 33.33% (4/12)
- `.bd-col-size-6`: 50% (6/12)
- `.bd-col-size-12`: 100% (full width)

### Responsive Columns
- `.md:bd-col-size-{1-12}` - Medium breakpoint
- `.lg:bd-col-size-{1-12}` - Large breakpoint

## Position Utilities

### Position Classes
- `.bd-pos-static` - position: static
- `.bd-pos-relative` - position: relative
- `.bd-pos-absolute` - position: absolute
- `.bd-pos-fixed` - position: fixed
- `.bd-pos-sticky` - position: sticky

### Positioning Values
- `.bd-top-{value}` - top positioning
- `.bd-right-{value}` - right positioning
- `.bd-bottom-{value}` - bottom positioning
- `.bd-left-{value}` - left positioning

Available values: 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 80, 100

## Order Utilities
- `.bd-odr-{-1 to 10}` - Order property for flex/grid items

## Usage Examples

```html
<!-- Flex Container Centered -->
<div class="bd-d-flex bd-jc-center bd-ai-center">
  <p>Centered content</p>
</div>

<!-- 12-Column Grid Layout -->
<div class="bd-row">
  <div class="bd-col-size-4">Sidebar</div>
  <div class="bd-col-size-8">Main Content</div>
</div>

<!-- Responsive Grid -->
<div class="bd-row">
  <div class="bd-col-size-12 md:bd-col-size-6 lg:bd-col-size-4">
    Card 1
  </div>
  <div class="bd-col-size-12 md:bd-col-size-6 lg:bd-col-size-4">
    Card 2
  </div>
  <div class="bd-col-size-12 md:bd-col-size-6 lg:bd-col-size-4">
    Card 3
  </div>
</div>

<!-- CSS Grid Layout -->
<div class="bd-d-grid bd-grid-col-3 bd-grid-gap-16">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>

<!-- Absolute Positioning -->
<div class="bd-pos-relative">
  <div class="bd-pos-absolute bd-top-0 bd-right-0">
    Badge
  </div>
</div>
```

## Helper Classes

### Centering
- `.bd-mid` - Flex center (both axes)
- `.bd-mid-h` - Horizontal center
- `.bd-mid-v` - Vertical center

### Container Query
- `.bd-cq` - Container query support
