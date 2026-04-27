# RetroUI - NeoBrutalism Styling Guide

## 🎨 Design System Update

Your inventory system now features **authentic NeoBrutalism** styling inspired by the actual RetroUI design philosophy. This is a bold, high-contrast design that stands out!

## Color Palette

### Primary Colors
```
White:      #ffffff (Main background)
Black:      #000000 (Text & Borders)
Yellow:     #fde047 (Accent - Action/Hover states)
Pink:       #f472b6 (Highlight boxes - Warning/Info)
Cyan:       #06b6d4 (Feature highlights)
Red:        #ef4444 (Error/Alert)
```

### Color Usage

| Element | Color | Usage |
|---------|-------|-------|
| Background | White | Main page background |
| Borders | Black (4px) | All elements have bold 4px borders |
| Text | Black | Main text color |
| Primary Action | Black bg, White text | Main buttons |
| Secondary Action | White bg, Black border | Outline buttons |
| Accent | Yellow (#fde047) | Hover effects, CTAs |
| Info Boxes | Pink (#f472b6) | Information/highlights |
| Features | Cyan (#06b6d4) | Feature highlights |
| Errors | Red (#ef4444) | Error messages |

## Design Characteristics

### Typography
- **Font Weight**: Extra bold (font-black) for headers
- **Font Weight**: Bold (font-bold) for regular text
- **Font Size**: Large sizes (text-lg, text-2xl, text-5xl, text-7xl)
- **All caps**: Buttons and labels use uppercase text

### Spacing
- **Padding**: Large padding (p-6, p-8, p-12)
- **Borders**: Thick 4px borders throughout (border-4)
- **Gap**: Generous spacing between elements (gap-3, gap-6, gap-8)

### Interactive Elements

#### Buttons
```jsx
// Primary Button (Black)
<button className="px-8 py-4 bg-black text-white font-black border-4 border-black hover:bg-yellow-300 hover:text-black">
  BUTTON TEXT
</button>

// Secondary Button (White with border)
<button className="px-8 py-4 bg-white text-black border-4 border-black hover:bg-black hover:text-white">
  BUTTON TEXT
</button>

// Accent Button (Yellow)
<button className="px-8 py-4 bg-yellow-300 text-black font-black border-4 border-black hover:scale-105">
  SIGN UP
</button>
```

#### Forms
- **Input fields**: 4px black borders, white background, bold text
- **Error states**: Red borders (#ef4444)
- **Placeholders**: Gray text
- **Focus states**: Box shadow for depth

#### Cards/Containers
- **Border**: 4px solid black
- **Padding**: Generous internal spacing (p-6, p-8)
- **Hover effects**: Background color changes on hover
- **No rounded corners**: Square, bold design

## Page Styling

### Landing Page
- **Background**: White
- **Navigation**: Black 4px bottom border, sticky positioning
- **Hero**: Large black text (text-7xl), bold typography
- **Feature Cards**: Black borders, white background, hover to yellow
- **Dark section**: Black background with white text
- **CTA Section**: Yellow background with black text

### Login Page
- **Center aligned**: Full screen form
- **Container**: Black 4px border, white background
- **Form elements**: White background with 4px black borders
- **Error styling**: Red borders and red text
- **Buttons**: Black with yellow hover

### Sign Up Page
- **Multi-column layout**: Fields in grid layout on desktop
- **Password strength**: Visual indicator with color-coded bars
- **Error handling**: Red borders and error messages
- **Benefits section**: Three colored boxes (Pink, Cyan, Yellow)

## Component Structure

### Borders
All major elements use `border-4 border-black`:
- Navigation: `border-b-4 border-black`
- Cards: `border-4 border-black`
- Buttons: `border-4 border-black`
- Inputs: `border-4 border-black` (or red when error)
- Dividers: `border-t-4 border-black`

### Transitions
- Duration: `duration-100` (fast transitions)
- Properties: `transition-all`, `transition-colors`, `transition-transform`
- Hover effects: Color change, scale, background change

### Responsive Design
- Mobile-first approach
- `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` for layouts
- Stacked on mobile, side-by-side on larger screens

## Examples

### Feature Card
```jsx
<div className="border-4 border-white bg-black p-6 hover:bg-yellow-300 hover:text-black hover:border-black text-white font-bold">
  <p className="text-5xl mb-3">📊</p>
  <h3 className="text-2xl font-black mb-2">ANALYTICS</h3>
  <p className="text-lg">Track metrics and predict demands</p>
</div>
```

### Input with Label
```jsx
<div>
  <label className="block text-lg font-black text-black mb-2">
    EMAIL ADDRESS
  </label>
  <input
    type="email"
    className="w-full px-4 py-4 bg-white border-4 border-black text-black font-bold text-lg focus:outline-none"
    placeholder="you@example.com"
  />
</div>
```

### CTA Section
```jsx
<div className="border-4 border-black bg-yellow-300 p-12 text-center">
  <h2 className="text-5xl font-black text-black mb-4">READY?</h2>
  <p className="text-2xl text-black font-bold mb-8">Start today</p>
  <button className="px-8 py-4 bg-black text-white font-black border-4 border-black hover:bg-white hover:text-black">
    GET STARTED
  </button>
</div>
```

## Font Scales Used
- `text-lg` - Small text (labels, captions)
- `text-xl` - Medium text
- `text-2xl` - Large text (subheadings)
- `text-4xl` - Very large (stats)
- `text-5xl` - Header size
- `text-6xl` - Large header
- `text-7xl` - Hero text

## Hover & Interactive States

### Button Hover
```
Black → Yellow background, Black text
White → Black background, White text
Yellow → Scale 1.05, slightly larger
```

### Card Hover
```
White bg → Yellow background
Black text → Yellow text (when on black)
```

### Link Hover
```
Black text → Yellow text
Underline appears
```

## Accessibility

- **High Contrast**: Black text on white, white text on black
- **Large Text**: Bold, large font sizes for readability
- **Clear Borders**: 4px borders make elements easily distinguishable
- **Focus States**: Clear focus indicators on inputs
- **Error Messages**: Red color with bold text

## Best Practices for Extending

When adding new components:

1. **Use 4px borders**: `border-4 border-black`
2. **Bold typography**: `font-black` for headings, `font-bold` for text
3. **Thick spacing**: Use p-6, p-8 for padding
4. **High contrast**: Black & white with yellow accents
5. **No gradients**: Solid colors only
6. **Square elements**: No rounded corners
7. **Fast transitions**: `duration-100`
8. **Large interactive elements**: Buttons 4px border, 4px padding

## NeoBrutalism Philosophy

✅ **DO:**
- Use bold, thick borders
- High contrast colors
- Large, legible typography
- Generous spacing
- Clear visual hierarchy
- Strong geometric shapes
- Vibrant accent colors

❌ **DON'T:**
- Use shadows and subtle effects
- Rounded corners or curves
- Light borders
- Small text
- Gradients
- Transparency effects
- Soft colors

---

Your frontend is now fully NeoBrutalism/RetroUI styled! 🚀
