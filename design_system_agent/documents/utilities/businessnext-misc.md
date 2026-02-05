# BusinessNext Miscellaneous Utilities

## List Styles

### List Style Type
- `.bd-li-disc` - list-style-type: disc (•)
- `.bd-li-circle` - list-style-type: circle (○)
- `.bd-li-square` - list-style-type: square (■)
- `.bd-li-decimal` - list-style-type: decimal (1, 2, 3)
- `.bd-li-lower-alpha` - list-style-type: lower-alpha (a, b, c)
- `.bd-li-upper-alpha` - list-style-type: upper-alpha (A, B, C)
- `.bd-li-decimal-leading-zero` - list-style-type: decimal-leading-zero (01, 02, 03)

### List Style Position
- `.bd-li-i` - list-style-position: inside
- `.bd-li-o` - list-style-position: outside

```html
<!-- Disc list -->
<ul class="bd-li-disc">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>

<!-- Numbered list -->
<ol class="bd-li-decimal">
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
</ol>

<!-- Inside position -->
<ul class="bd-li-i bd-li-square">
  <li>Inside item</li>
  <li>Inside item</li>
</ul>
```

## Table Layout

### Table Layout
- `.bd-tl-a` - table-layout: auto
- `.bd-tl-f` - table-layout: fixed

### Caption Side
- `.bd-cs-t` - caption-side: top
- `.bd-cs-b` - caption-side: bottom

### Empty Cells
- `.bd-ec-s` - empty-cells: show
- `.bd-ec-h` - empty-cells: hide

```html
<!-- Fixed layout table -->
<table class="bd-table bd-tl-f">
  <caption class="bd-cs-t bd-pa-8 bd-fw-bold">Table Caption</caption>
  <thead>
    <tr>
      <th class="bd-pa-8">Name</th>
      <th class="bd-pa-8">Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="bd-pa-8">John Doe</td>
      <td class="bd-pa-8">john@example.com</td>
    </tr>
  </tbody>
</table>

<!-- Hide empty cells -->
<table class="bd-table bd-ec-h">
  <tr>
    <td class="bd-pa-8">Data</td>
    <td class="bd-pa-8"></td>
    <td class="bd-pa-8">Data</td>
  </tr>
</table>
```

## Vertical Align
- `.bd-va-t` - vertical-align: top
- `.bd-va-m` - vertical-align: middle
- `.bd-va-b` - vertical-align: bottom
- `.bd-va-ini` - vertical-align: initial
- `.bd-va-inh` - vertical-align: inherit

```html
<!-- Table cells -->
<table class="bd-table">
  <tr>
    <td class="bd-va-t bd-pa-8">Top aligned</td>
    <td class="bd-va-m bd-pa-8">Middle aligned</td>
    <td class="bd-va-b bd-pa-8">Bottom aligned</td>
  </tr>
</table>

<!-- Inline elements -->
<div style="line-height: 3;">
  Text <img src="icon.png" class="bd-va-m" style="height: 24px;"> with icon
</div>
```

## Writing Mode
- `.bd-wm-wm-h` - writing-mode: horizontal-tb (horizontal)
- `.bd-wm-wm-v` - writing-mode: vertical-rl (vertical right-to-left)

```html
<!-- Vertical text -->
<div class="bd-wm-wm-v bd-pa-16" style="height: 200px;">
  Vertical Text
</div>
```

## Direction
- `.bd-dir-dir-ltr` - direction: ltr (left-to-right)
- `.bd-dir-dir-rtl` - direction: rtl (right-to-left)
- `.bd-dir-dir-ini` - direction: initial

```html
<!-- Right-to-left -->
<div class="bd-dir-dir-rtl bd-pa-16">
  <p>This text flows right to left</p>
  <p>مرحبا بك (Arabic text example)</p>
</div>

<!-- Left-to-right -->
<div class="bd-dir-dir-ltr">
  <p>Normal left-to-right text</p>
</div>
```

## Font Variant
- `.bd-fv-normal` - font-variant: normal
- `.bd-fv-ordinal` - font-variant: ordinal (1st, 2nd, 3rd)
- `.bd-fv-slashed-zero` - font-variant: slashed-zero (0̸)
- `.bd-fv-lining-nums` - font-variant: lining-nums
- `.bd-fv-oldstyle-nums` - font-variant: oldstyle-nums
- `.bd-fv-proportional-nums` - font-variant: proportional-nums
- `.bd-fv-tabular-nums` - font-variant: tabular-nums (monospace numbers)
- `.bd-fv-diagonal-fractions` - font-variant: diagonal-fractions (½)
- `.bd-fv-stacked-fractions` - font-variant: stacked-fractions

```html
<!-- Tabular numbers for alignment -->
<div class="bd-fv-tabular-nums">
  <p>Price: $1,234.56</p>
  <p>Price:   $987.65</p>
  <p>Price:    $12.34</p>
</div>

<!-- Ordinal numbers -->
<p class="bd-fv-ordinal">
  1st place, 2nd place, 3rd place
</p>
```

## Font Style
- `.bd-fs-normal` - font-style: normal
- `.bd-fs-italic` - font-style: italic
- `.bd-fs-oblique` - font-style: oblique

```html
<!-- Italic text -->
<p class="bd-fs-italic">
  This text is italicized
</p>

<!-- Emphasis -->
<em class="bd-fs-normal">Not italic despite em tag</em>
```

## Box Sizing
- `.bd-bs-cb` - box-sizing: content-box
- `.bd-bs-bb` - box-sizing: border-box
- `.bd-bs-ini` - box-sizing: initial
- `.bd-bs-inh` - box-sizing: inherit

```html
<!-- Border-box sizing -->
<div class="bd-bs-bb bd-wt-200 bd-pa-16 bd-ba-2">
  Width includes padding and border
</div>

<!-- Content-box sizing -->
<div class="bd-bs-cb bd-wt-200 bd-pa-16 bd-ba-2">
  Width is content only
</div>
```

## Box Decoration Break
- `.bd-bd-clone` - box-decoration-break: clone
- `.bd-bd-slice` - box-decoration-break: slice
- `.bd-bd-inherit` - box-decoration-break: inherit
- `.bd-bd-unset` - box-decoration-break: unset

```html
<!-- Clone decoration on line break -->
<span class="bd-bd-clone bd-pa-4 bd-br8" 
      style="background: var(--bnds-g-color-yellow-30); display: inline;">
  This highlighted text wraps to multiple lines with decoration preserved
</span>
```

## Usage Examples

### Styled List
```html
<div class="bd-card bd-pa-24">
  <h3 class="bd-mb-16">Features</h3>
  <ul class="bd-li-disc bd-pl-20">
    <li class="bd-mb-8">Easy to use</li>
    <li class="bd-mb-8">Fast performance</li>
    <li class="bd-mb-8">Modern design</li>
  </ul>
</div>
```

### Ordered List with Custom Style
```html
<div class="bd-card bd-pa-24">
  <h3 class="bd-mb-16">Steps</h3>
  <ol class="bd-li-decimal bd-pl-24">
    <li class="bd-mb-8">Create account</li>
    <li class="bd-mb-8">Verify email</li>
    <li class="bd-mb-8">Complete profile</li>
  </ol>
</div>
```

### Data Table with Alignment
```html
<table class="bd-table bd-tl-f bd-w-100">
  <thead>
    <tr style="background: var(--bnds-g-color-gray-20);">
      <th class="bd-pa-12 bd-txt-l">Product</th>
      <th class="bd-pa-12 bd-txt-r">Price</th>
      <th class="bd-pa-12 bd-txt-r">Quantity</th>
      <th class="bd-pa-12 bd-txt-r">Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="bd-pa-12 bd-va-m">Product A</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">$1,234.56</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">3</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">$3,703.68</td>
    </tr>
    <tr>
      <td class="bd-pa-12 bd-va-m">Product B</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">$987.65</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">2</td>
      <td class="bd-pa-12 bd-txt-r bd-fv-tabular-nums">$1,975.30</td>
    </tr>
  </tbody>
</table>
```

### Bilingual Content
```html
<div class="bd-card bd-pa-24">
  <div class="bd-dir-dir-ltr bd-mb-16">
    <h4>English</h4>
    <p>This is left-to-right text</p>
  </div>
  <div class="bd-dir-dir-rtl">
    <h4>العربية</h4>
    <p>هذا نص من اليمين إلى اليسار</p>
  </div>
</div>
```

### Highlighted Quote
```html
<blockquote class="bd-pa-16 bd-bl-4 bd-bd-clone" 
            style="background: var(--bnds-g-color-blue-10); border-color: var(--bnds-g-color-blue-50);">
  <p class="bd-fs-italic">
    "This is a multi-line quote that maintains its styling across line breaks with box-decoration-break."
  </p>
  <cite class="bd-font-12">— Author Name</cite>
</blockquote>
```

### Numbered Steps
```html
<div class="bd-card bd-pa-24">
  <h3 class="bd-mb-16">Getting Started</h3>
  <ol class="bd-li-decimal-leading-zero bd-pl-32" style="list-style-type: decimal-leading-zero;">
    <li class="bd-mb-12 bd-pl-8">
      <strong>Install</strong>
      <p class="bd-font-12 bd-mt-4">Run npm install</p>
    </li>
    <li class="bd-mb-12 bd-pl-8">
      <strong>Configure</strong>
      <p class="bd-font-12 bd-mt-4">Update config file</p>
    </li>
    <li class="bd-mb-12 bd-pl-8">
      <strong>Deploy</strong>
      <p class="bd-font-12 bd-mt-4">Push to production</p>
    </li>
  </ol>
</div>
```

## Best Practices

1. **Lists**: Use semantic HTML (`<ul>`, `<ol>`) with styling utilities
2. **Tables**: Use `table-layout: fixed` for consistent column widths
3. **Numbers**: Use tabular-nums for aligned number columns
4. **Direction**: Set direction at the container level, not individual elements
5. **Box Sizing**: Use border-box for predictable sizing
6. **Accessibility**: Maintain proper heading hierarchy and semantic markup
