import { useState, useEffect } from 'react'
import './Analysis.css'

function Analysis({ jobData, cvData, onComplete, onReset }) {
  const [stage, setStage] = useState('analyzing')
  const [analysis, setAnalysis] = useState(null)
  const [showImprove, setShowImprove] = useState(false)
  const [improvedCV, setImprovedCV] = useState(null)
  const [coverLetter, setCoverLetter] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    analyzeCV()
  }, [])

  const analyzeCV = async () => {
    try {
      setStage('analyzing')
      await new Promise(resolve => setTimeout(resolve, 2000))

      const mockAnalysis = {
        score: 75,
        compatible: true,
        strengths: [
          'Strong technical skills matching job requirements',
          'Relevant work experience in similar roles',
          'Clear and well-structured formatting'
        ],
        weaknesses: [
          'Missing some key industry-specific keywords',
          'Could expand on leadership experience',
          'Certifications section needs more detail'
        ],
        recommendations: [
          'Add specific metrics and achievements to quantify your impact',
          'Include more keywords related to the job description',
          'Expand your skills section to include mentioned technologies',
          'Consider adding a professional summary at the top'
        ]
      }

      setAnalysis(mockAnalysis)
      setStage('results')
      onComplete(mockAnalysis)
    } catch (err) {
      setError('Failed to analyze CV. Please try again.')
      setStage('error')
    }
  }

  const handleImproveCV = async () => {
    try {
      setStage('improving')
      await new Promise(resolve => setTimeout(resolve, 2000))

      setImprovedCV('Your improved CV content will appear here...')
      setStage('improved')
    } catch (err) {
      setError('Failed to improve CV. Please try again.')
      setStage('error')
    }
  }

  const handleGenerateCoverLetter = async () => {
    try {
      setStage('generating-cover')
      await new Promise(resolve => setTimeout(resolve, 2000))

      setCoverLetter('Your tailored cover letter will appear here...')
      setStage('complete')
    } catch (err) {
      setError('Failed to generate cover letter. Please try again.')
      setStage('error')
    }
  }

  const downloadFile = (content, filename) => {
    const blob = new Blob([content], { type: 'text/markdown' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = filename
    a.click()
    URL.revokeObjectURL(url)
  }

  if (stage === 'analyzing') {
    return (
      <div className="analysis-loading">
        <div className="spinner"></div>
        <h3>Analyzing your CV...</h3>
        <p>Our AI is comparing your CV against the job requirements</p>
      </div>
    )
  }

  if (stage === 'improving') {
    return (
      <div className="analysis-loading">
        <div className="spinner"></div>
        <h3>Improving your CV...</h3>
        <p>Applying recommended changes to enhance your CV</p>
      </div>
    )
  }

  if (stage === 'generating-cover') {
    return (
      <div className="analysis-loading">
        <div className="spinner"></div>
        <h3>Generating cover letter...</h3>
        <p>Creating a tailored cover letter for this position</p>
      </div>
    )
  }

  if (stage === 'error') {
    return (
      <div className="analysis-error">
        <svg className="error-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3>Something went wrong</h3>
        <p>{error}</p>
        <button onClick={onReset} className="reset-btn">Start Over</button>
      </div>
    )
  }

  return (
    <div className="analysis-results">
      <div className="score-card">
        <h2>ATS Compatibility Score</h2>
        <div className="score-circle">
          <svg className="score-progress" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="90" fill="none" stroke="#e5e7eb" strokeWidth="20" />
            <circle
              cx="100"
              cy="100"
              r="90"
              fill="none"
              stroke={analysis?.score >= 70 ? '#10b981' : analysis?.score >= 50 ? '#f59e0b' : '#ef4444'}
              strokeWidth="20"
              strokeDasharray={`${(analysis?.score / 100) * 565} 565`}
              strokeLinecap="round"
              transform="rotate(-90 100 100)"
            />
          </svg>
          <div className="score-text">
            <span className="score-number">{analysis?.score}</span>
            <span className="score-label">/ 100</span>
          </div>
        </div>
        <p className={`compatibility ${analysis?.compatible ? 'compatible' : 'not-compatible'}`}>
          {analysis?.compatible ? 'You are compatible for this job!' : 'More improvements needed'}
        </p>
      </div>

      <div className="analysis-sections">
        <div className="analysis-section strengths">
          <h3>What's Great</h3>
          <ul>
            {analysis?.strengths.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="analysis-section weaknesses">
          <h3>What's Lacking</h3>
          <ul>
            {analysis?.weaknesses.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

        <div className="analysis-section recommendations">
          <h3>Recommended Actions</h3>
          <ul>
            {analysis?.recommendations.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      </div>

      {!improvedCV && (
        <div className="action-card">
          <h3>Would you like us to improve your CV automatically?</h3>
          <div className="action-buttons">
            <button onClick={handleImproveCV} className="primary-btn">
              Yes, Improve My CV
            </button>
            <button onClick={handleGenerateCoverLetter} className="secondary-btn">
              Skip to Cover Letter
            </button>
          </div>
        </div>
      )}

      {improvedCV && !coverLetter && stage === 'improved' && (
        <div className="result-card">
          <h3>Your Improved CV</h3>
          <div className="result-preview">
            <pre>{improvedCV}</pre>
          </div>
          <div className="action-buttons">
            <button onClick={() => downloadFile(improvedCV, 'improved_cv.md')} className="download-btn">
              Download CV
            </button>
            <button onClick={handleGenerateCoverLetter} className="primary-btn">
              Generate Cover Letter
            </button>
          </div>
        </div>
      )}

      {coverLetter && stage === 'complete' && (
        <div className="result-card">
          <h3>Your Cover Letter</h3>
          <div className="result-preview">
            <pre>{coverLetter}</pre>
          </div>
          <div className="action-buttons">
            <button onClick={() => downloadFile(coverLetter, 'cover_letter.md')} className="download-btn">
              Download Cover Letter
            </button>
            <button onClick={onReset} className="primary-btn">
              Start New Analysis
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default Analysis
