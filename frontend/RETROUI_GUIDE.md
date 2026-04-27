# RetroUI Components Guide

## Overview

This project uses **RetroUI** styling principles implemented with Tailwind CSS. The design emphasizes:
- Bold 2px borders
- Dark backgrounds with blue/cyan accents
- Glassmorphism with backdrop blur
- Neon-like glow effects
- Strong contrast for readability

## Color Palette

```
Primary Blue:    #0066cc (rgb(0, 102, 204))
Bright Blue:     #3b82f6 (Tailwind blue-500)
Light Blue:      #60a5fa (Tailwind blue-400)
Cyan:            #06b6d4 (Tailwind cyan-500)
Dark BG:         #0a0e27 (Custom dark blue)
Card BG:         #1f2937 (Tailwind gray-800)
Border:          rgba(59, 130, 246, 0.3) (blue-400 with opacity)
```

## Component Examples

### Button Component

```jsx
import { Button } from './components'

// Primary button
<Button>Save Changes</Button>

// Secondary button (outline)
<Button variant="secondary">Cancel</Button>

// Danger button
<Button variant="danger">Delete</Button>

// Success button
<Button variant="success">Confirm</Button>

// Different sizes
<Button size="sm">Small</Button>
<Button size="md">Medium</Button>
<Button size="lg">Large</Button>
<Button size="xl">Extra Large</Button>

// With custom styling
<Button className="w-full">Full Width</Button>

// Disabled state
<Button disabled>Disabled</Button>
```

### Card Component

```jsx
import { Card } from './components'

<Card>
  <h2>Card Title</h2>
  <p>Card content goes here</p>
</Card>

// With custom styling
<Card className="hover:border-blue-400">
  <h3>Hoverable Card</h3>
</Card>

// Grid of cards
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <Card>Card 1</Card>
  <Card>Card 2</Card>
  <Card>Card 3</Card>
</div>
```

### Input Component

```jsx
import { Input } from './components'

// Basic input
<Input 
  type="text"
  placeholder="Enter text"
/>

// With label and validation
<Input 
  label="Email"
  type="email"
  placeholder="user@example.com"
  error={errors.email}
  onChange={handleChange}
/>

// Password input
<Input 
  label="Password"
  type="password"
  placeholder="••••••••"
  error={errors.password}
/>

// Select input (custom styling needed)
<select className="w-full px-4 py-3 bg-gray-800/50 border-2 border-blue-400/50 text-white rounded">
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

### Badge Component

```jsx
import { Badge } from './components'

// Default badge
<Badge>Default</Badge>

// Success badge
<Badge variant="success">Active</Badge>

// Warning badge
<Badge variant="warning">Pending</Badge>

// Error badge
<Badge variant="error">Error</Badge>

// With custom styling
<Badge className="ml-2">Tag</Badge>
```

### Alert Component

```jsx
import { Alert } from './components'

// Info alert
<Alert type="info">This is an information message</Alert>

// Success alert
<Alert type="success">Operation completed successfully</Alert>

// Warning alert
<Alert type="warning">Please review this warning</Alert>

// Error alert
<Alert type="error">An error occurred</Alert>
```

## Tailwind CSS Utility Classes

### Common RetroUI Patterns

```jsx
// Border styling
className="border-2 border-blue-400"
className="border-2 border-blue-400/50"  // Semi-transparent

// Background styling
className="bg-gray-800/50"  // Semi-transparent gray
className="bg-blue-400/10"  // Very subtle blue background
className="backdrop-blur"   // Glassmorphism effect

// Text styling
className="text-white"
className="text-blue-400"
className="font-bold"
className="font-semibold"

// Spacing
className="p-4"   // Padding
className="px-4"  // Horizontal padding
className="py-3"  // Vertical padding
className="gap-4" // Gap between flex items
className="space-y-4"  // Vertical space between children

// Transitions
className="transition-colors duration-200"
className="hover:bg-blue-400"

// Responsive
className="md:grid-cols-2"  // 2 columns on medium screens
className="lg:grid-cols-3"  // 3 columns on large screens
```

## Form Patterns

### Login Form Pattern

```jsx
const [formData, setFormData] = useState({ email: '', password: '' })
const [errors, setErrors] = useState({})

const handleChange = (e) => {
  const { name, value } = e.target
  setFormData(prev => ({ ...prev, [name]: value }))
  if (errors[name]) setErrors(prev => ({ ...prev, [name]: '' }))
}

<form>
  <Input
    label="Email"
    type="email"
    name="email"
    value={formData.email}
    onChange={handleChange}
    error={errors.email}
  />
  <Input
    label="Password"
    type="password"
    name="password"
    value={formData.password}
    onChange={handleChange}
    error={errors.password}
  />
  <Button type="submit">Login</Button>
</form>
```

## Layout Patterns

### Hero Section

```jsx
<div className="min-h-screen bg-gradient-to-b from-gray-900 via-blue-900 to-gray-900">
  <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
    <h1 className="text-6xl font-bold text-white">Title</h1>
    <p className="text-xl text-gray-300">Description</p>
  </div>
</div>
```

### Card Grid

```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {items.map((item, idx) => (
    <Card key={idx}>
      <h3 className="text-lg font-bold text-white">{item.title}</h3>
      <p className="text-gray-400">{item.description}</p>
    </Card>
  ))}
</div>
```

### Navigation Bar

```jsx
<nav className="border-b border-gray-700 bg-gray-900/50 backdrop-blur-sm">
  <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
    <h1 className="text-2xl font-bold text-white">Logo</h1>
    <div className="flex gap-4">
      <Button variant="secondary">Login</Button>
      <Button>Sign Up</Button>
    </div>
  </div>
</nav>
```

## Animation & Hover Effects

```jsx
// Smooth transitions
className="transition-colors duration-200 hover:border-blue-400"

// Scale on hover
className="hover:scale-105 transition-transform"

// Background on hover
className="hover:bg-blue-400/10 transition-colors"

// Glow effect
className="shadow-lg shadow-blue-500/20"
```

## Responsive Breakpoints

```jsx
// Mobile first approach
className="w-full"           // Base: full width
className="sm:w-1/2"         // Small screens: 50%
className="md:w-1/3"         // Medium screens: 33%
className="lg:w-1/4"         // Large screens: 25%
className="xl:w-1/5"         // XL screens: 20%
className="2xl:w-1/6"        // 2XL screens: 16%

// Grid layout
className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"
```

## Best Practices

1. **Always use borders** - RetroUI is characterized by bold borders
2. **Maintain contrast** - Ensure text is readable on backgrounds
3. **Use consistent spacing** - Use Tailwind's spacing scale (4px, 8px, 12px, 16px, etc.)
4. **Keep it consistent** - Use the same button/card styles throughout
5. **Test responsiveness** - Check mobile, tablet, and desktop views
6. **Use semantic colors** - Red for danger, green for success, blue for info
7. **Add transitions** - Smooth color/transform transitions on interaction

## Common Issues & Solutions

### Borders not showing
- Check `border-2` class is present
- Verify border color (e.g., `border-blue-400`)
- Ensure element has background so border is visible

### Text not visible
- Check text color (e.g., `text-white`, `text-blue-400`)
- Ensure sufficient contrast with background
- Check for `opacity-0` or hidden states

### Components not responsive
- Use Tailwind's breakpoint prefixes (`sm:`, `md:`, `lg:`)
- Test at different screen sizes
- Use `max-w-*` for container width limits

### Styling not applying
- Check class names for typos
- Verify Tailwind config includes correct content paths
- Run `npm install` after adding new files
- Clear browser cache if needed
