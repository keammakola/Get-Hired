import { useState } from 'react'
import { useDropzone } from 'react-dropzone'
import './CVUpload.css'

function CVUpload({ onSubmit, onBack }) {
  const [uploadMethod, setUploadMethod] = useState('file')
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const onDrop = (acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      const selectedFile = acceptedFiles[0]
      if (selectedFile.type === 'application/pdf' ||
          selectedFile.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') {
        setFile(selectedFile)
        setError('')
      } else {
        setError('Please upload a PDF or DOCX file')
      }
    }
  }

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx']
    },
    multiple: false
  })

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      if (uploadMethod === 'file') {
        if (!file) {
          setError('Please upload a CV file')
          setLoading(false)
          return
        }
        const reader = new FileReader()
        reader.onload = (e) => {
          onSubmit({ method: 'file', file, content: e.target.result })
        }
        reader.readAsArrayBuffer(file)
      } else {
        onSubmit({ method: 'create' })
      }
    } catch (err) {
      setError('An error occurred. Please try again.')
      setLoading(false)
    }
  }

  return (
    <div className="cv-upload">
      <h2 className="section-title">Upload your CV</h2>
      <p className="section-description">
        Upload your existing CV or create a new one from scratch
      </p>

      <div className="input-method-selector">
        <button
          className={`method-btn ${uploadMethod === 'file' ? 'active' : ''}`}
          onClick={() => setUploadMethod('file')}
          type="button"
        >
          Upload File
        </button>
        <button
          className={`method-btn ${uploadMethod === 'create' ? 'active' : ''}`}
          onClick={() => setUploadMethod('create')}
          type="button"
        >
          Create New
        </button>
      </div>

      <form onSubmit={handleSubmit} className="cv-form">
        {uploadMethod === 'file' ? (
          <div className="form-group">
            <div
              {...getRootProps()}
              className={`dropzone ${isDragActive ? 'active' : ''} ${file ? 'has-file' : ''}`}
            >
              <input {...getInputProps()} />
              {file ? (
                <div className="file-info">
                  <svg className="file-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <p className="file-name">{file.name}</p>
                  <p className="file-size">{(file.size / 1024).toFixed(2)} KB</p>
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation()
                      setFile(null)
                    }}
                    className="remove-file-btn"
                  >
                    Remove
                  </button>
                </div>
              ) : (
                <div className="dropzone-content">
                  <svg className="upload-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                  <p className="dropzone-text">
                    {isDragActive ? 'Drop your CV here' : 'Drag and drop your CV, or click to browse'}
                  </p>
                  <p className="dropzone-hint">Supports PDF and DOCX files</p>
                </div>
              )}
            </div>
          </div>
        ) : (
          <div className="create-cv-info">
            <svg className="info-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p>You'll be guided through a step-by-step process to create your CV from scratch.</p>
          </div>
        )}

        {error && <div className="error-message">{error}</div>}

        <div className="button-group">
          <button type="button" onClick={onBack} className="back-btn">
            Back
          </button>
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? 'Processing...' : 'Continue'}
          </button>
        </div>
      </form>
    </div>
  )
}

export default CVUpload
