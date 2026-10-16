import { useState } from 'react'
import QRCode from 'react-qr-code'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('shorten') // 'shorten' or 'analytics'
  
  // Shorten State
  const [originalUrl, setOriginalUrl] = useState('')
  const [shortUrl, setShortUrl] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [copied, setCopied] = useState(false)

  // Analytics State
  const [trackUrl, setTrackUrl] = useState('')
  const [stats, setStats] = useState(null)
  const [isTracking, setIsTracking] = useState(false)
  const [trackError, setTrackError] = useState('')

  const handleShorten = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setCopied(false) 
    
    try {
      const response = await fetch('https://trimly-backend-w8ge.onrender.com/api/create/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ original_url: originalUrl }) 
      })
      const data = await response.json()
      if (response.ok) {
        setShortUrl(`https://trimly-backend-w8ge.onrender.com/${data.short_code}`)
      }
    } catch (error) {
      console.error("Failed to shorten URL:", error)
    } finally {
      setIsLoading(false)
    }
  }

  const handleTrack = async (e) => {
    e.preventDefault()
    setIsTracking(true)
    setTrackError('')
    setStats(null)

    // Extract just the code if they pasted the full short link
    const code = trackUrl.split('/').filter(Boolean).pop()

    try {
      const response = await fetch(`https://trimly-backend-w8ge.onrender.com/api/stats/${code}/`)
      if (response.ok) {
        const data = await response.json()
        setStats(data)
      } else {
        setTrackError("Link not found. Please check the URL and try again.")
      }
    } catch (error) {
      setTrackError("Failed to connect to the server.")
    } finally {
      setIsTracking(false)
    }
  }

  const handleCopy = () => {
    navigator.clipboard.writeText(shortUrl)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000) 
  }

  return (
    <div className="app-container">
      <div className="card">
        
        {/* New Trimly Logo and Title */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '12px', marginBottom: '20px' }}>
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="6" cy="12" r="4.5" fill="#3B82F6" />
            <path d="M11.5 12H16" stroke="#93C5FD" strokeWidth="2.5" strokeLinecap="round" strokeDasharray="3 3" />
            <circle cx="19" cy="12" r="2.5" fill="#1D4ED8" />
          </svg>
          <h1 style={{ margin: 0, fontSize: '2rem', color: '#1e293b' }}>Trimly</h1>
        </div>
        
        <div className="tab-container">
          <button 
            className={`tab-btn ${activeTab === 'shorten' ? 'active' : ''}`}
            onClick={() => setActiveTab('shorten')}
          >
            Shorten Link
          </button>
          <button 
            className={`tab-btn ${activeTab === 'analytics' ? 'active' : ''}`}
            onClick={() => setActiveTab('analytics')}
          >
            Track Clicks
          </button>
        </div>
        
        {activeTab === 'shorten' ? (
          <>
            <p className="subtitle">Shorten your links quickly and securely.</p>
            <form onSubmit={handleShorten} className="url-form">
              <input
                type="url"
                value={originalUrl}
                onChange={(e) => setOriginalUrl(e.target.value)}
                placeholder="Paste long URL here..."
                required
                className="url-input"
              />
              <button type="submit" disabled={isLoading} className="shorten-btn">
                {isLoading ? 'Shortening...' : 'Shorten URL'}
              </button>
            </form>

            {shortUrl && (
              <div className="result-box">
                <p>Your shortened URL:</p>
                <div className="link-action-container">
                  <a href={shortUrl} target="_blank" rel="noopener noreferrer">{shortUrl}</a>
                  <button onClick={handleCopy} className="copy-btn">
                    {copied ? 'Copied!' : 'Copy'}
                  </button>
                </div>
                <div className="qr-container">
                  <QRCode value={shortUrl} size={120} />
                  <p className="qr-text">Scan to visit</p>
                </div>
              </div>
            )}
          </>
        ) : (
          <>
            <p className="subtitle">See how many people clicked your link.</p>
            <form onSubmit={handleTrack} className="url-form">
              <input
                type="text"
                value={trackUrl}
                onChange={(e) => setTrackUrl(e.target.value)}
                placeholder="Paste short link (e.g., https://trimly-backend-w8ge.onrender.com/AbCdEf)"
                required
                className="url-input"
              />
              <button type="submit" disabled={isTracking} className="shorten-btn track-btn">
                {isTracking ? 'Searching...' : 'Check Stats'}
              </button>
            </form>

            {trackError && <p className="error-text">{trackError}</p>}

            {stats && (
              <div className="stats-box">
                <div className="stat-item">
                  <span className="stat-label">Total Clicks</span>
                  <span className="stat-value">{stats.clicks}</span>
                </div>
                <div className="stat-item">
                  <span className="stat-label">Destinations</span>
                  <a href={stats.original_url} target="_blank" rel="noopener noreferrer" className="stat-url">
                    {stats.original_url.length > 40 ? stats.original_url.substring(0, 40) + '...' : stats.original_url}
                  </a>
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}

export default App