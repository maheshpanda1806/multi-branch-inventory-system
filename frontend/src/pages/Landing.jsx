import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className="border-b-4 border-black bg-white sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex justify-between items-center">
          <div className="text-4xl font-black text-black">INVENTORY</div>
          <div className="flex gap-2">
            <Link 
              to="/login"
              className="px-6 py-3 border-4 border-black bg-white text-black font-black hover:bg-black hover:text-white transition-all duration-100 text-lg"
            >
              LOGIN
            </Link>
            <Link 
              to="/signup"
              className="px-6 py-3 border-4 border-black bg-yellow-300 text-black font-black hover:scale-105 transition-transform duration-100 text-lg"
            >
              SIGN UP
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          {/* Left Content */}
          <div className="space-y-6">
            <div className="inline-block">
              <div className="px-6 py-3 border-4 border-black bg-pink-300 font-black text-black text-xl">
                🚀 NEXT GENERATION
              </div>
            </div>
            
            <h1 className="text-7xl font-black text-black leading-tight">
              MULTI-BRANCH<br/>INVENTORY
            </h1>
            
            <p className="text-2xl text-black font-bold max-w-lg">
              Bold. Modern. Powerful. Manage your inventory with style.
            </p>

            <div className="flex gap-3 pt-4 flex-wrap">
              <Link 
                to="/signup"
                className="px-8 py-4 bg-black text-white font-black hover:bg-yellow-300 hover:text-black transition-all duration-100 border-4 border-black text-lg"
              >
                GET STARTED
              </Link>
              <button className="px-8 py-4 border-4 border-black text-black font-black hover:bg-yellow-300 transition-all duration-100 bg-white text-lg">
                WATCH DEMO
              </button>
            </div>

            <div className="flex gap-8 pt-8 text-lg font-bold border-t-4 border-black pt-8">
              <div>
                <p className="text-4xl font-black text-black">10K+</p>
                <p className="text-black">Active Users</p>
              </div>
              <div>
                <p className="text-4xl font-black text-black">99.9%</p>
                <p className="text-black">Uptime</p>
              </div>
              <div>
                <p className="text-4xl font-black text-black">24/7</p>
                <p className="text-black">Support</p>
              </div>
            </div>
          </div>

          {/* Right - Visual */}
          <div className="relative">
            <div className="border-4 border-black bg-cyan-300 p-8">
              <div className="space-y-4 bg-white border-4 border-black p-6">
                <div className="flex items-center gap-2">
                  <div className="w-4 h-4 bg-red-500 border-2 border-black"></div>
                  <div className="w-4 h-4 bg-yellow-300 border-2 border-black"></div>
                  <div className="w-4 h-4 bg-lime-300 border-2 border-black"></div>
                </div>
                
                <pre className="text-sm text-black font-mono overflow-auto font-bold">
                  <code>{`// REAL-TIME INVENTORY
const inventory = {
  branches: 3,
  sync: "ACTIVE",
  status: "✓ ONLINE"
}

// ANALYTICS
const metrics = {
  stock: 50000,
  orders: 2847,
  profit: "$124,500"
}`}</code>
                </pre>
              </div>
            </div>

            {/* Floating card */}
            <div className="absolute -bottom-6 -left-6 border-4 border-black bg-pink-300 p-6 w-56 font-bold text-black">
              <p className="text-2xl font-black">REAL-TIME</p>
              <p className="text-lg">Track inventory across all branches instantly</p>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="bg-black text-white py-16 mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-6xl font-black text-center mb-16">
            BOLD FEATURES
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { icon: "📊", title: "ANALYTICS", desc: "Track metrics and predict demands" },
              { icon: "🔄", title: "REAL-TIME SYNC", desc: "Instant synchronization" },
              { icon: "👥", title: "MULTI-USER", desc: "Team collaboration" },
              { icon: "🛡️", title: "SECURE", desc: "Enterprise-grade security" },
              { icon: "📱", title: "MOBILE", desc: "Works on all devices" },
              { icon: "⚡", title: "FAST", desc: "Lightning quick performance" }
            ].map((feature, idx) => (
              <div
                key={idx}
                className="border-4 border-white bg-black p-6 hover:bg-yellow-300 hover:text-black hover:border-black transition-all duration-100 group font-bold text-lg"
              >
                <p className="text-5xl mb-3">{feature.icon}</p>
                <h3 className="text-2xl font-black mb-2">{feature.title}</h3>
                <p className="text-lg">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="border-4 border-black bg-yellow-300 p-12 text-center">
          <h2 className="text-5xl font-black text-black mb-4">READY TO TRANSFORM?</h2>
          <p className="text-2xl text-black font-bold mb-8">Start with a free account and manage your inventory today.</p>
          
          <div className="flex gap-3 justify-center flex-wrap">
            <Link 
              to="/signup"
              className="px-8 py-4 bg-black text-white font-black hover:bg-white hover:text-black transition-all duration-100 border-4 border-black text-lg"
            >
              START FREE TRIAL
            </Link>
            <button className="px-8 py-4 border-4 border-black text-black font-black hover:bg-black hover:text-yellow-300 transition-all duration-100 bg-white text-lg">
              SCHEDULE DEMO
            </button>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="border-t-4 border-black bg-white py-12 mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <p className="text-black font-black text-2xl mb-4">PRODUCT</p>
              <ul className="space-y-2 text-black font-bold text-lg">
                <li><a href="#" className="hover:underline">Features</a></li>
                <li><a href="#" className="hover:underline">Pricing</a></li>
                <li><a href="#" className="hover:underline">Security</a></li>
              </ul>
            </div>
            <div>
              <p className="text-black font-black text-2xl mb-4">COMPANY</p>
              <ul className="space-y-2 text-black font-bold text-lg">
                <li><a href="#" className="hover:underline">About</a></li>
                <li><a href="#" className="hover:underline">Blog</a></li>
                <li><a href="#" className="hover:underline">Careers</a></li>
              </ul>
            </div>
            <div>
              <p className="text-black font-black text-2xl mb-4">RESOURCES</p>
              <ul className="space-y-2 text-black font-bold text-lg">
                <li><a href="#" className="hover:underline">Docs</a></li>
                <li><a href="#" className="hover:underline">Support</a></li>
                <li><a href="#" className="hover:underline">API</a></li>
              </ul>
            </div>
            <div>
              <p className="text-black font-black text-2xl mb-4">LEGAL</p>
              <ul className="space-y-2 text-black font-bold text-lg">
                <li><a href="#" className="hover:underline">Privacy</a></li>
                <li><a href="#" className="hover:underline">Terms</a></li>
                <li><a href="#" className="hover:underline">Contact</a></li>
              </ul>
            </div>
          </div>
          
          <div className="border-t-4 border-black pt-8 text-center text-black font-bold text-lg">
            <p>© 2024 Multi-Branch Inventory System. ALL RIGHTS RESERVED.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
