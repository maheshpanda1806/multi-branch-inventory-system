export function Button({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  className = '',
  ...props 
}) {
  const baseStyles = 'font-semibold transition-colors duration-200 border-2 rounded'
  
  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
    xl: 'px-8 py-4 text-lg'
  }

  const variants = {
    primary: 'bg-blue-500 hover:bg-blue-600 text-white border-blue-500',
    secondary: 'border-2 border-blue-400 text-blue-400 hover:bg-blue-400/10',
    danger: 'bg-red-500 hover:bg-red-600 text-white border-red-500',
    success: 'bg-green-500 hover:bg-green-600 text-white border-green-500'
  }

  return (
    <button 
      className={`${baseStyles} ${sizes[size]} ${variants[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  )
}

export function Card({ children, className = '', ...props }) {
  return (
    <div 
      className={`border-2 border-blue-400/30 bg-gray-800/50 backdrop-blur rounded-lg p-6 ${className}`}
      {...props}
    >
      {children}
    </div>
  )
}

export function Input({ 
  label, 
  error, 
  className = '',
  ...props 
}) {
  return (
    <div>
      {label && (
        <label className="block text-sm font-semibold text-white mb-2">
          {label}
        </label>
      )}
      <input
        className={`w-full px-4 py-3 bg-gray-800/50 border-2 text-white placeholder-gray-500 focus:outline-none transition-colors duration-200 rounded ${
          error
            ? 'border-red-400 focus:border-red-500'
            : 'border-blue-400/50 focus:border-blue-400'
        } ${className}`}
        {...props}
      />
      {error && (
        <p className="mt-2 text-sm text-red-400">{error}</p>
      )}
    </div>
  )
}

export function Badge({ 
  children, 
  variant = 'default',
  className = ''
}) {
  const variants = {
    default: 'bg-blue-400/10 border-blue-400 text-blue-400',
    success: 'bg-green-400/10 border-green-400 text-green-400',
    warning: 'bg-yellow-400/10 border-yellow-400 text-yellow-400',
    error: 'bg-red-400/10 border-red-400 text-red-400'
  }

  return (
    <span className={`inline-block px-3 py-1 border border-current rounded-full text-sm ${variants[variant]} ${className}`}>
      {children}
    </span>
  )
}

export function Alert({ 
  children, 
  type = 'info',
  className = ''
}) {
  const types = {
    info: 'border-blue-400 bg-blue-400/10 text-blue-400',
    success: 'border-green-400 bg-green-400/10 text-green-400',
    warning: 'border-yellow-400 bg-yellow-400/10 text-yellow-400',
    error: 'border-red-400 bg-red-400/10 text-red-400'
  }

  return (
    <div className={`border-2 p-4 rounded ${types[type]} ${className}`}>
      {children}
    </div>
  )
}
