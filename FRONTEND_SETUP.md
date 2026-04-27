# Frontend Setup Guide

## ✅ What's Been Set Up

### 🎨 RetroUI Styling
The frontend implements a RetroUI aesthetic using **Tailwind CSS** with custom styling that mimics the retroui.dev design language:
- Dark color scheme with blue/cyan accents
- Border-based UI elements (2px borders)
- Retro neon styling effects
- Glassmorphism components with backdrop blur

### 📦 Project Structure
```
frontend/
├── src/
│   ├── components/           # Reusable RetroUI components
│   │   ├── RetroUI.jsx      # Button, Card, Input, Badge, Alert
│   │   └── index.js         # Component exports
│   ├── pages/               # Page components
│   │   ├── Landing.jsx      # Landing page (like retroui.dev)
│   │   ├── Login.jsx        # Login page
│   │   └── SignUp.jsx       # Sign up page
│   ├── App.jsx              # Main app with routing
│   ├── main.jsx             # Entry point
│   └── index.css            # Global Tailwind styles
├── index.html               # HTML entry
├── vite.config.js           # Vite configuration with API proxy
├── tailwind.config.js       # Tailwind configuration
├── postcss.config.js        # PostCSS with Tailwind plugin
├── package.json             # Dependencies
├── .env.example             # Environment variables template
└── README.md                # Frontend documentation
```

## 🚀 Quick Start

### 1. Install Dependencies (Already Done ✓)
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm run dev
```
- Frontend runs on: **http://localhost:5173**
- Backend proxy configured to: **http://localhost:8000**

### 3. Build for Production
```bash
npm run build
```
Output goes to `dist/` folder.

## 🎯 Pages Available

### Landing Page (`/`)
- Hero section with feature highlights
- Navigation with login/signup buttons
- Features grid showcasing 6 key capabilities
- Call-to-action sections
- Footer with links
- Responsive design

### Login Page (`/login`)
- Email/password form with validation
- Remember me checkbox
- Forgot password link
- Social login options (Google, Microsoft)
- Link to sign up page

### Sign Up Page (`/signup`)
- Multi-field form (first name, last name, email)
- Company and branch information
- Password strength indicator
- Password confirmation
- Terms agreement checkbox
- Form validation with error messages
- Benefits display

## 🎨 UI Components

All components are in `src/components/RetroUI.jsx`:

### Button
```jsx
<Button variant="primary" size="lg">Click me</Button>
```
Variants: `primary`, `secondary`, `danger`, `success`
Sizes: `sm`, `md`, `lg`, `xl`

### Card
```jsx
<Card>
  <h3>Content</h3>
  <p>More content</p>
</Card>
```

### Input
```jsx
<Input 
  label="Email" 
  error={errors.email}
  type="email"
  placeholder="user@example.com"
/>
```

### Badge
```jsx
<Badge variant="success">Active</Badge>
```

### Alert
```jsx
<Alert type="error">Something went wrong</Alert>
```

## 🔌 Backend Integration

The frontend is configured to proxy API requests:
- Requests to `/api/*` are forwarded to `http://localhost:8000`
- Configure this in `vite.config.js`

Example API call:
```javascript
const response = await fetch('/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email, password })
})
```

## 🌐 Environment Variables

Create `.env.local`:
```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=Multi-Branch Inventory System
```

Access in code:
```javascript
const apiUrl = import.meta.env.VITE_API_URL
```

## 📱 Responsive Design

- Mobile-first approach
- Tailwind responsive classes (`sm:`, `md:`, `lg:`, etc.)
- All pages are mobile-friendly
- Tested breakpoints: 320px, 768px, 1024px, 1280px

## 🔐 Form Validation

All forms include:
- Required field validation
- Email format validation
- Password strength checking
- Password confirmation matching
- Error state styling with red borders
- Error messages below fields

## ⚡ Performance

- Vite for fast development and builds
- Code splitting for pages
- Optimized bundle size (~57KB gzipped)
- CSS purging with Tailwind

## 🛠️ Development Tips

### Adding a New Page
1. Create `src/pages/NewPage.jsx`
2. Add route in `App.jsx`
3. Import and use routing

### Adding a New Component
1. Create in `src/components/`
2. Export from `src/components/index.js`
3. Import where needed

### Styling
- Use Tailwind utility classes
- Maintain the retro aesthetic with borders
- Use blue/cyan colors from the theme
- Keep 2px borders for retro look

## 📚 Next Steps

1. **Connect Backend**: Update API endpoints in form handlers
2. **Add Features**: 
   - Dashboard page
   - Inventory management UI
   - Analytics pages
   - User profile
3. **Authentication**: Integrate with backend auth system
4. **State Management**: Consider Redux/Context API for state
5. **Testing**: Add Vitest and React Testing Library

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9
```

### Build Errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Styling Not Working
- Ensure Tailwind config includes correct paths
- Check that CSS is imported in main.jsx
- Run `npm install` again

## 📖 Resources

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [React Router Documentation](https://reactrouter.com/)
- [RetroUI Design Reference](https://www.retroui.dev/)
