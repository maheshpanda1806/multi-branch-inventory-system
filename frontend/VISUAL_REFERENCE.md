# NeoBrutalism Visual Guide - Color & Style Reference

## Color Combinations Used

### Primary Combinations

#### Black + White (Main)
```
█████████ BLACK
░░░░░░░░░ WHITE

Usage: Navigation, main layout, text
High Contrast: ✓ PERFECT
```

#### Black + Yellow (Accent)
```
█████████ BLACK
■■■■■■■■■ YELLOW

Usage: Hover states, CTA buttons, highlights
High Contrast: ✓ PERFECT
```

#### Black + Pink (Info)
```
█████████ BLACK
■■■■■■■■■ PINK

Usage: Information boxes, highlights
High Contrast: ✓ EXCELLENT
```

#### Black + Cyan (Features)
```
█████████ BLACK
■■■■■■■■■ CYAN

Usage: Feature sections, highlights
High Contrast: ✓ EXCELLENT
```

#### White + Black (Main)
```
░░░░░░░░░ WHITE
█████████ BLACK

Usage: Background with text and borders
High Contrast: ✓ MAXIMUM
```

#### Yellow + Black (CTAs)
```
■■■■■■■■■ YELLOW
█████████ BLACK

Usage: Call-to-action buttons, important actions
High Contrast: ✓ PERFECT
```

## Typography Hierarchy

### Hero Text (Landing Page)
```
█████████████████████████████
█ MULTI-BRANCH INVENTORY    █
█████████████████████████████

Font: text-7xl font-black
Color: Black
Background: White
Border: 4px black
```

### Section Headings
```
██████████████████
█ BOLD FEATURES  █
██████████████████

Font: text-6xl font-black
Color: White (on black) / Black (on white)
Border: 4px
```

### Feature Titles
```
┌────────────────┐
│ ANALYTICS      │
│ Track metrics  │
└────────────────┘

Title: text-2xl font-black
Text: text-lg font-bold
Border: 4px black
```

### Form Labels
```
EMAIL ADDRESS

Font: text-lg font-black
Color: Black
Style: All uppercase
```

## Button Styles

### Primary Button (Call-to-Action)
```
┌─────────────────────────┐
│ ████████████████████    │
│ █  GET STARTED      █   │
│ ████████████████████    │
└─────────────────────────┘

Default:
- Background: Black
- Text: White
- Border: 4px Black
- Font: font-black

Hover:
- Background: Yellow
- Text: Black
- Border: 4px Black
```

### Secondary Button (Alternative)
```
┌──────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░    │
│ ░  WATCH DEMO       ░    │
│ ░░░░░░░░░░░░░░░░░░░░    │
└──────────────────────────┘

Default:
- Background: White
- Text: Black
- Border: 4px Black
- Font: font-black

Hover:
- Background: Black
- Text: White
- Border: 4px Black
```

### Accent Button (Sign Up)
```
┌──────────────────────────┐
│ ■■■■■■■■■■■■■■■■■■■■   │
│ ■  SIGN UP         ■     │
│ ■■■■■■■■■■■■■■■■■■■■   │
└──────────────────────────┘

Default:
- Background: Yellow
- Text: Black
- Border: 4px Black
- Font: font-black

Hover:
- Scale: 105%
- Slight elevation
```

## Card/Container Styles

### Feature Card (Black Background)
```
┌─────────────────────────────┐
│ █████████████████████████   │
│ █ 📊                      █ │
│ █ ANALYTICS               █ │
│ █ Track metrics...        █ │
│ █████████████████████████   │
└─────────────────────────────┘

- Background: Black (#000000)
- Text: White
- Border: 4px White
- Padding: p-6
- Hover: Background changes to Yellow, text to Black
```

### Info/Highlight Box
```
┌──────────────────────────────┐
│ ╔════════════════════════╗   │
│ ║  REAL-TIME            ║   │
│ ║  Instant sync across  ║   │
│ ║  all branches         ║   │
│ ╚════════════════════════╝   │
└──────────────────────────────┘

Color Options:
- Pink (bg-pink-300, border-black)
- Cyan (bg-cyan-300, border-black)
- Yellow (bg-yellow-300, border-black)

Styling:
- Border: 4px Black
- Text: Black (font-bold)
- Padding: p-6
```

### Form Input
```
┌────────────────────────────────┐
│ EMAIL ADDRESS (label)          │
│ ┌──────────────────────────────┐│
│ │ user@example.com       ┃    ││
│ │ (placeholder)          ┃    ││
│ └──────────────────────────────┘│
└────────────────────────────────┘

Normal State:
- Background: White
- Border: 4px Black
- Text: Black
- Font: font-bold

Error State:
- Background: White
- Border: 4px Red (#ef4444)
- Text: Red (error message)
- Font: font-bold

Focus State:
- Box shadow: 4px 4px 0 rgba(0,0,0,0.2)
```

## Spacing System

### Padding Examples
```
p-3  = 12px (small components)
p-4  = 16px (medium components)
p-6  = 24px (cards, containers)
p-8  = 32px (large sections)
p-12 = 48px (CTA sections)

Visualized:
┌────────────────────────┐
│ p-3 ┌────────────────┐ │
│     │ content        │ │
│     └────────────────┘ │
└────────────────────────┘
```

### Gap Examples
```
gap-2 = 8px   (close elements)
gap-3 = 12px  (normal spacing)
gap-4 = 16px  (medium gap)
gap-6 = 24px  (large gap)
gap-8 = 32px  (extra large)

Visual:
[Button] gap-2 [Button] - close
[Button] gap-4 [Button] - normal
[Button] gap-8 [Button] - spacious
```

## Border System

### Border Styles
```
border-4 border-black
┌──────────────────────┐
│                      │
│    CONTENT AREA      │
│                      │
└──────────────────────┘

4px = Thick, bold appearance
Black = Maximum contrast
Square corners = NeoBrutalism style
```

### Border Variants
```
border-t-4    (Top border - navigation, dividers)
border-b-4    (Bottom border - separators)
border-4      (All sides - cards, buttons)
border-x-4    (Left & right - containers)
```

## Complete Page Examples

### Landing Page Layout
```
┌────────────────────────────────────┐
│ INVENTORY  [LOGIN] [SIGN UP]       │ ← Navigation
├────────────────────────────────────┤
│                                    │
│  MULTI-BRANCH INVENTORY            │
│  Bold description text             │ ← Hero
│  [GET STARTED] [WATCH DEMO]        │
│                                    │
├────────────────────────────────────┤
│                                    │
│ BLACK SECTION                      │
│ ┌──────────┐ ┌──────────┐ ... 6   │ ← Features
│ │ 📊       │ │ 🔄       │ cards   │
│ │ ANALYTICS│ │ SYNC     │         │
│ └──────────┘ └──────────┘         │
│                                    │
├────────────────────────────────────┤
│ ┌──────────────────────────────┐  │
│ │ READY TO TRANSFORM?          │  │ ← CTA
│ │ [START FREE TRIAL]           │  │
│ └──────────────────────────────┘  │
│                                    │
└────────────────────────────────────┘
```

### Form Page Layout
```
┌────────────────────────────────────┐
│ INVENTORY                          │
│ Sign in to your account            │
├────────────────────────────────────┤
│                                    │
│ ┌──────────────────────────────┐  │
│ │ EMAIL ADDRESS                │  │
│ │ ┌────────────────────────────┐ │
│ │ │ user@example.com           │ │
│ │ └────────────────────────────┘ │
│ │                                │
│ │ PASSWORD                       │
│ │ ┌────────────────────────────┐ │
│ │ │ ••••••••                   │ │
│ │ └────────────────────────────┘ │
│ │                                │
│ │ [SIGN IN]                      │
│ │                                │
│ │ ─────────────────────────      │
│ │        OR                      │
│ │ ─────────────────────────      │
│ │                                │
│ │ [GOOGLE] [MICROSOFT]          │
│ │                                │
│ │ Don't have account? CREATE ONE │
│ └──────────────────────────────┘  │
└────────────────────────────────────┘
```

## Responsive Behavior

### Desktop (lg:)
```
3 Columns
┌──────────┐ ┌──────────┐ ┌──────────┐
│ Card 1   │ │ Card 2   │ │ Card 3   │
└──────────┘ └──────────┘ └──────────┘
```

### Tablet (md:)
```
2 Columns
┌──────────┐ ┌──────────┐
│ Card 1   │ │ Card 2   │
└──────────┘ └──────────┘
┌──────────┐ ┌──────────┐
│ Card 3   │ │ Card 4   │
└──────────┘ └──────────┘
```

### Mobile (no prefix)
```
1 Column
┌──────────┐
│ Card 1   │
└──────────┘
┌──────────┐
│ Card 2   │
└──────────┘
┌──────────┐
│ Card 3   │
└──────────┘
```

## Design Principles

✅ **Bold**: All elements are loud and noticeable
✅ **Clear**: High contrast for readability
✅ **Simple**: No fancy effects or gradients
✅ **Geometric**: Square shapes, straight lines
✅ **Consistent**: Same styling throughout
✅ **Fast**: Quick transitions (duration-100)
✅ **Modern**: Contemporary NeoBrutalism trend
✅ **Professional**: Strong, confident design

---

This is authentic **NeoBrutalism** - bold, brave, and unapologetically different! 🎨
