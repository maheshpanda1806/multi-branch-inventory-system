import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

export default function Login() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  })
  const [errors, setErrors] = useState({})
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }))
    }
  }

  const validateForm = () => {
    const newErrors = {}
    if (!formData.email) newErrors.email = 'Email is required'
    else if (!/\S+@\S+\.\S+/.test(formData.email)) newErrors.email = 'Email is invalid'
    if (!formData.password) newErrors.password = 'Password is required'
    return newErrors
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const newErrors = validateForm()
    
    if (Object.keys(newErrors).length === 0) {
      setLoading(true)
      try {
        console.log('Login attempt:', formData)
        await new Promise(resolve => setTimeout(resolve, 1000))
        navigate('/dashboard')
      } catch (error) {
        setErrors({ submit: 'Login failed. Please try again.' })
      } finally {
        setLoading(false)
      }
    } else {
      setErrors(newErrors)
    }
  }

  return (
    <div className="min-h-screen bg-white flex items-center justify-center px-4">
      <div className="w-full max-w-md">
        {/* Header */}
        <div className="text-center mb-8">
          <Link to="/" className="inline-block mb-6">
            <h1 className="text-5xl font-black text-black hover:text-yellow-300 transition-colors">
              INVENTORY
            </h1>
          </Link>
          <p className="text-black font-bold text-xl">Sign in to your account</p>
        </div>

        {/* Form Container */}
        <div className="border-4 border-black bg-white p-8">
          {errors.submit && (
            <div className="mb-6 p-4 border-4 border-red-500 bg-red-200 text-black font-bold text-lg">
              {errors.submit}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Email Field */}
            <div>
              <label htmlFor="email" className="block text-lg font-black text-black mb-2">
                EMAIL ADDRESS
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="you@example.com"
                className={`w-full px-4 py-4 bg-white border-4 text-black placeholder-gray-500 focus:outline-none font-bold text-lg ${
                  errors.email
                    ? 'border-red-500'
                    : 'border-black'
                }`}
              />
              {errors.email && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.email}</p>
              )}
            </div>

            {/* Password Field */}
            <div>
              <label htmlFor="password" className="block text-lg font-black text-black mb-2">
                PASSWORD
              </label>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="••••••••"
                className={`w-full px-4 py-4 bg-white border-4 text-black placeholder-gray-500 focus:outline-none font-bold text-lg ${
                  errors.password
                    ? 'border-red-500'
                    : 'border-black'
                }`}
              />
              {errors.password && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.password}</p>
              )}
            </div>

            {/* Remember & Forgot */}
            <div className="flex items-center justify-between text-lg font-bold">
              <label className="flex items-center gap-2 cursor-pointer text-black hover:text-yellow-300 transition-colors">
                <input type="checkbox" className="w-5 h-5 border-2 border-black" />
                <span>Remember me</span>
              </label>
              <a href="#" className="text-black hover:text-yellow-300 transition-colors">
                Forgot?
              </a>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-4 px-4 bg-black hover:bg-yellow-300 disabled:bg-gray-400 text-white hover:text-black font-black border-4 border-black transition-all duration-100 text-lg"
            >
              {loading ? 'SIGNING IN...' : 'SIGN IN'}
            </button>
          </form>

          {/* Divider */}
          <div className="relative my-6">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t-4 border-black"></div>
            </div>
            <div className="relative flex justify-center text-lg font-bold">
              <span className="px-2 bg-white text-black">OR</span>
            </div>
          </div>

          {/* Social Buttons */}
          <div className="space-y-3">
            <button className="w-full py-4 px-4 border-4 border-black text-black font-bold hover:bg-black hover:text-white transition-all duration-100 bg-white text-lg">
              🔵 GOOGLE
            </button>
            <button className="w-full py-4 px-4 border-4 border-black text-black font-bold hover:bg-black hover:text-white transition-all duration-100 bg-white text-lg">
              📘 MICROSOFT
            </button>
          </div>

          {/* Sign Up Link */}
          <div className="mt-6 text-center text-black font-bold text-lg">
            Don't have an account?{' '}
            <Link to="/signup" className="text-black font-black hover:text-yellow-300 transition-colors">
              CREATE ONE
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
