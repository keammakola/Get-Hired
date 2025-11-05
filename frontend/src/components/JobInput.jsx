import { useState } from 'react'
import './JobInput.css'

function JobInput({ onSubmit }) {
  const [inputMethod, setInputMethod] = useState('link')
  const [jobLink, setJobLink] = useState('')
  const [jobText, setJobText] = useState('')
  const [companyName, setCompanyName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      if (inputMethod === 'link') {
        if (!jobLink.trim()) {
          setError('Please enter a job link')
          setLoading(false)
          return
        }
        onSubmit({ method: 'link', link: jobLink })
      } else {
        if (!companyName.trim() || !jobText.trim()) {
          setError('Please fill in all fields')
          setLoading(false)
          return
        }
        onSubmit({ method: 'text', companyName, text: jobText })
      }
    } catch (err) {
      setError('An error occurred. Please try again.')
      setLoading(false)
    }
  }

  return (
    <div className="job-input">
      <h2 className="section-title">Tell us about the job</h2>
      <p className="section-description">
        Provide the job details by pasting a link or entering the information manually
      </p>

      <div className="input-method-selector">
        <button
          className={`method-btn ${inputMethod === 'link' ? 'active' : ''}`}
          onClick={() => setInputMethod('link')}
          type="button"
        >
          Job Link
        </button>
        <button
          className={`method-btn ${inputMethod === 'text' ? 'active' : ''}`}
          onClick={() => setInputMethod('text')}
          type="button"
        >
          Manual Entry
        </button>
      </div>

      <form onSubmit={handleSubmit} className="job-form">
        {inputMethod === 'link' ? (
          <div className="form-group">
            <label htmlFor="jobLink">Job Posting URL</label>
            <input
              id="jobLink"
              type="url"
              value={jobLink}
              onChange={(e) => setJobLink(e.target.value)}
              placeholder="https://linkedin.com/jobs/..."
              className="input-field"
              disabled={loading}
            />
            <p className="input-hint">LinkedIn, Indeed, and most job boards supported</p>
          </div>
        ) : (
          <>
            <div className="form-group">
              <label htmlFor="companyName">Company Name</label>
              <input
                id="companyName"
                type="text"
                value={companyName}
                onChange={(e) => setCompanyName(e.target.value)}
                placeholder="e.g., Google"
                className="input-field"
                disabled={loading}
              />
            </div>
            <div className="form-group">
              <label htmlFor="jobText">Job Description</label>
              <textarea
                id="jobText"
                value={jobText}
                onChange={(e) => setJobText(e.target.value)}
                placeholder="Paste the complete job description here..."
                className="textarea-field"
                rows="10"
                disabled={loading}
              />
            </div>
          </>
        )}

        {error && <div className="error-message">{error}</div>}

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Processing...' : 'Continue'}
        </button>
      </form>
    </div>
  )
}

export default JobInput
