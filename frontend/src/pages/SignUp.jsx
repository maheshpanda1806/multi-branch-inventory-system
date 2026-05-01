import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api } from '../api'

export default function SignUp() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    agreeTerms: false
  })
  const [errors, setErrors] = useState({})
  const [loading, setLoading] = useState(false)
  const [passwordStrength, setPasswordStrength] = useState(0)

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target
    const newValue = type === 'checkbox' ? checked : value
    
    setFormData(prev => ({
      ...prev,
      [name]: newValue
    }))

    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }))
    }

    if (name === 'password') {
      let strength = 0
      if (value.length >= 8) strength++
      if (/[a-z]/.test(value)) strength++
      if (/[A-Z]/.test(value)) strength++
      if (/[0-9]/.test(value)) strength++
      if (/[^a-zA-Z0-9]/.test(value)) strength++
      setPasswordStrength(strength)
    }
  }

  const validateForm = () => {
    const newErrors = {}
    
    if (!formData.email) newErrors.email = 'Email is required'
    else if (!/\S+@\S+\.\S+/.test(formData.email)) newErrors.email = 'Email is invalid'
    
    if (!formData.username.trim()) newErrors.username = 'Username is required'
    
    if (!formData.password) newErrors.password = 'Password is required'
    else if (formData.password.length < 8) newErrors.password = 'Password must be at least 8 characters'
    
    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match'
    }
    
    if (!formData.agreeTerms) newErrors.agreeTerms = 'You must agree to the terms'
    
    return newErrors
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const newErrors = validateForm()
    
    if (Object.keys(newErrors).length === 0) {
      setLoading(true)
      try {
        const response = await api.signup(formData.email, formData.username, formData.password)
        
        if (response.access) {
          // Store tokens
          api.setTokens(response.access, response.refresh)
          // Redirect to dashboard
          navigate('/dashboard')
        } else if (response.email) {
          setErrors({ email: Array.isArray(response.email) ? response.email[0] : response.email })
        } else if (response.username) {
          setErrors({ username: Array.isArray(response.username) ? response.username[0] : response.username })
        } else if (response.password) {
          setErrors({ password: Array.isArray(response.password) ? response.password[0] : response.password })
        } else {
          setErrors({ submit: 'Sign up failed. Please try again.' })
        }
      } catch (error) {
        setErrors({ submit: 'Sign up failed. Please try again.' })
      } finally {
        setLoading(false)
      }
    } else {
      setErrors(newErrors)
    }
  }

  const passwordStrengthColor = {
    0: 'bg-gray-400',
    1: 'bg-red-500',
    2: 'bg-orange-500',
    3: 'bg-yellow-300',
    4: 'bg-lime-300',
    5: 'bg-green-500'
  }

  const passwordStrengthText = {
    0: 'Enter a password',
    1: 'Very weak',
    2: 'Weak',
    3: 'Fair',
    4: 'Good',
    5: 'Strong'
  }

  return (
    <div className="min-h-screen bg-white flex items-center justify-center px-4 py-8">
      <div className="w-full max-w-2xl">
        {/* Header */}
        <div className="text-center mb-8">
          <Link to="/" className="inline-block mb-6">
            <h1 className="text-5xl font-black text-black hover:text-yellow-300 transition-colors">
              INVENTORY
            </h1>
          </Link>
          <p className="text-black font-bold text-xl">Create your account and get started</p>
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
                  errors.email ? 'border-red-500' : 'border-black'
                }`}
              />
              {errors.email && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.email}</p>
              )}
            </div>

            {/* Username Field */}
            <div>
              <label htmlFor="username" className="block text-lg font-black text-black mb-2">
                USERNAME
              </label>
              <input
                type="text"
                id="username"
                name="username"
                value={formData.username}
                onChange={handleChange}
                placeholder="username"
                className={`w-full px-4 py-4 bg-white border-4 text-black placeholder-gray-500 focus:outline-none font-bold text-lg ${
                  errors.username ? 'border-red-500' : 'border-black'
                }`}
              />
              {errors.username && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.username}</p>
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
                  errors.password ? 'border-red-500' : 'border-black'
                }`}
              />
              
              {formData.password && (
                <div className="mt-2">
                  <div className="flex gap-1 mb-2">
                    {[...Array(5)].map((_, i) => (
                      <div
                        key={i}
                        className={`h-2 flex-1 border-2 border-black ${
                          i < passwordStrength ? passwordStrengthColor[passwordStrength] : 'bg-white'
                        }`}
                      ></div>
                    ))}
                  </div>
                  <p className="text-lg font-black text-black">{passwordStrengthText[passwordStrength]}</p>
                </div>
              )}
              
              {errors.password && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.password}</p>
              )}
            </div>

            {/* Confirm Password */}
            <div>
              <label htmlFor="confirmPassword" className="block text-lg font-black text-black mb-2">
                CONFIRM PASSWORD
              </label>
              <input
                type="password"
                id="confirmPassword"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleChange}
                placeholder="••••••••"
                className={`w-full px-4 py-4 bg-white border-4 text-black placeholder-gray-500 focus:outline-none font-bold text-lg ${
                  errors.confirmPassword ? 'border-red-500' : 'border-black'
                }`}
              />
              {errors.confirmPassword && (
                <p className="mt-2 text-lg font-bold text-red-500">{errors.confirmPassword}</p>
              )}
            </div>

            {/* Terms Checkbox */}
            <div className="space-y-3">
              <label className="flex items-start gap-3 cursor-pointer">
                <input
                  type="checkbox"
                  name="agreeTerms"
                  checked={formData.agreeTerms}
                  onChange={handleChange}
                  className="w-6 h-6 border-2 border-black mt-1"
                />
                <span className="text-lg font-bold text-black">
                  I agree to the{' '}
                  <a href="#" className="underline hover:text-yellow-300">
                    Terms of Service
                  </a>{' '}
                  and{' '}
                  <a href="#" className="underline hover:text-yellow-300">
                    Privacy Policy
                  </a>
                </span>
              </label>
              {errors.agreeTerms && (
                <p className="text-lg font-bold text-red-500">{errors.agreeTerms}</p>
              )}
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-4 px-4 bg-black hover:bg-yellow-300 disabled:bg-gray-400 text-white hover:text-black font-black border-4 border-black transition-all duration-100 text-lg"
            >
              {loading ? 'CREATING ACCOUNT...' : 'CREATE ACCOUNT'}
            </button>
          </form>

          {/* Sign In Link */}
          <div className="mt-6 text-center text-black font-bold text-lg">
            Already have an account?{' '}
            <Link to="/login" className="text-black font-black hover:text-yellow-300 transition-colors">
              SIGN IN
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
