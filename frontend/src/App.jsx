import { useState } from 'react'
import './App.css'
import JobInput from './components/JobInput'
import CVUpload from './components/CVUpload'
import Analysis from './components/Analysis'

function App() {
  const [step, setStep] = useState(1)
  const [jobData, setJobData] = useState(null)
  const [cvData, setCvData] = useState(null)
  const [analysisData, setAnalysisData] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleJobSubmit = (data) => {
    setJobData(data)
    setStep(2)
  }

  const handleCVSubmit = (data) => {
    setCvData(data)
    setStep(3)
  }

  const handleAnalysisComplete = (data) => {
    setAnalysisData(data)
  }

  const resetApp = () => {
    setStep(1)
    setJobData(null)
    setCvData(null)
    setAnalysisData(null)
    setLoading(false)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <h1 className="logo">Get Hired</h1>
          <p className="tagline">AI-powered CV analysis for your dream job</p>
        </div>
      </header>

      <main className="main-content">
        <div className="progress-bar">
          <div className={`progress-step ${step >= 1 ? 'active' : ''} ${step > 1 ? 'completed' : ''}`}>
            <div className="step-number">1</div>
            <div className="step-label">Job Details</div>
          </div>
          <div className={`progress-line ${step > 1 ? 'active' : ''}`}></div>
          <div className={`progress-step ${step >= 2 ? 'active' : ''} ${step > 2 ? 'completed' : ''}`}>
            <div className="step-number">2</div>
            <div className="step-label">Upload CV</div>
          </div>
          <div className={`progress-line ${step > 2 ? 'active' : ''}`}></div>
          <div className={`progress-step ${step >= 3 ? 'active' : ''}`}>
            <div className="step-number">3</div>
            <div className="step-label">Analysis</div>
          </div>
        </div>

        <div className="content-container">
          {step === 1 && <JobInput onSubmit={handleJobSubmit} />}
          {step === 2 && <CVUpload onSubmit={handleCVSubmit} onBack={() => setStep(1)} />}
          {step === 3 && (
            <Analysis
              jobData={jobData}
              cvData={cvData}
              onComplete={handleAnalysisComplete}
              onReset={resetApp}
            />
          )}
        </div>
      </main>

      <footer className="footer">
        <p>&copy; 2025 Get Hired. Powered by AI.</p>
      </footer>
    </div>
  )
}

export default App
