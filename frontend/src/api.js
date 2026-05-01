// API client for backend communication
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Track refresh token requests to avoid multiple simultaneous refreshes
let refreshPromise = null

export const api = {
  // Auth endpoints
  signup: async (email, username, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/signup/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        username,
        password,
      }),
    })
    return response.json()
  },

  login: async (email, password) => {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        password,
      }),
    })
    return response.json()
  },

  // Refresh access token using refresh token
  refreshAccessToken: async () => {
    // Prevent multiple simultaneous refresh requests
    if (refreshPromise) {
      return refreshPromise
    }

    refreshPromise = (async () => {
      try {
        const refresh = api.getRefreshToken()
        if (!refresh) {
          api.clearTokens()
          window.location.href = '/login'
          return false
        }

        const response = await fetch(`${API_BASE_URL}/auth/api/token/refresh/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            refresh,
          }),
        })

        if (response.ok) {
          const data = await response.json()
          api.setTokens(data.access, refresh)
          return true
        } else {
          // Refresh failed, redirect to login
          api.clearTokens()
          window.location.href = '/login'
          return false
        }
      } finally {
        refreshPromise = null
      }
    })()

    return refreshPromise
  },

  // Generic fetch with auto-refresh on 401
  authenticatedFetch: async (url, options = {}) => {
    // Add auth header
    const headers = {
      ...options.headers,
      ...api.getAuthHeader(),
    }

    let response = await fetch(url, {
      ...options,
      headers,
    })

    // If 401, try refreshing token and retry once
    if (response.status === 401) {
      const refreshed = await api.refreshAccessToken()
      if (refreshed) {
        // Retry request with new token
        const newHeaders = {
          ...options.headers,
          ...api.getAuthHeader(),
        }
        response = await fetch(url, {
          ...options,
          headers: newHeaders,
        })
      }
    }

    return response
  },

  // Utility functions
  setTokens: (access, refresh) => {
    localStorage.setItem('access_token', access)
    localStorage.setItem('refresh_token', refresh)
  },

  getAccessToken: () => localStorage.getItem('access_token'),
  getRefreshToken: () => localStorage.getItem('refresh_token'),

  clearTokens: () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  },

  isAuthenticated: () => !!localStorage.getItem('access_token'),

  // Helper to add auth header to requests
  getAuthHeader: () => {
    const token = api.getAccessToken()
    return token ? { Authorization: `Bearer ${token}` } : {}
  },
}

