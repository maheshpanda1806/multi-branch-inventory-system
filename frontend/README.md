# Multi-Branch Inventory System - React Frontend

A modern React frontend built with Vite, Tailwind CSS, and RetroUI components for managing multi-branch inventory.

## 🚀 Features

- **Modern UI Design**: Built with Tailwind CSS and RetroUI components
- **Fast Build**: Powered by Vite for rapid development
- **Responsive Design**: Mobile-first approach
- **Component-Based**: Reusable React components
- **Real-time Updates**: Ready to integrate with backend API

## 📋 Prerequisites

- Node.js (v16 or higher)
- npm or yarn

## 🛠️ Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file for environment variables:
```bash
cp .env.example .env.local
```

## 🏃 Running the Development Server

Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## 🏗️ Building for Production

Build the project:
```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

## 📁 Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable components
│   ├── pages/           # Page components
│   │   ├── Landing.jsx  # Landing page
│   │   ├── Login.jsx    # Login page
│   │   └── SignUp.jsx   # Sign up page
│   ├── App.jsx          # Main app component
│   ├── main.jsx         # Entry point
│   └── index.css        # Global styles
├── index.html           # HTML entry point
├── vite.config.js       # Vite configuration
├── tailwind.config.js   # Tailwind CSS configuration
└── package.json         # Dependencies
```

## 🎨 Styling

The project uses:
- **Tailwind CSS**: Utility-first CSS framework
- **RetroUI Components**: Retro-styled UI components
- **Custom CSS**: In `src/index.css`

## 🔌 API Integration

The frontend is configured to proxy API requests to the backend. Update the proxy configuration in `vite.config.js`:

```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8000',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, '')
  }
}
```

## 📝 Pages

### Landing Page
- Hero section with feature highlights
- Call-to-action buttons
- Feature showcase grid
- Responsive navigation

### Login Page
- Email/password login form
- Form validation
- Social login options
- Sign up link

### Sign Up Page
- Multi-step form
- Password strength indicator
- Company and branch information
- Terms agreement
- Form validation

## 🔐 Environment Variables

Create a `.env.local` file:

```env
VITE_API_URL=http://localhost:8000/api
VITE_APP_NAME=Multi-Branch Inventory System
```

## 🧪 Testing

To add testing capabilities, install testing libraries:

```bash
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom
```

## 📦 Dependencies

- **React**: UI library
- **React Router**: Routing
- **Tailwind CSS**: Styling
- **RetroUI**: Retro UI components
- **Vite**: Build tool

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## 📄 License

This project is part of the Multi-Branch Inventory System.

## 🆘 Support

For issues and questions, please check the main project README or contact support.
