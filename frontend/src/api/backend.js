import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const uploadCV = async (file) => {
  const formData = new FormData()
  formData.append('cv', file)

  const response = await api.post('/api/cv/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data
}

export const analyzeCV = async (cvData, jobData) => {
  const response = await api.post('/api/cv/analyze', {
    cv: cvData,
    job: jobData,
  })

  return response.data
}

export const improveCV = async (cvData, analysisReport) => {
  const response = await api.post('/api/cv/improve', {
    cv: cvData,
    report: analysisReport,
  })

  return response.data
}

export const generateCoverLetter = async (cvData, jobData) => {
  const response = await api.post('/api/cover-letter/generate', {
    cv: cvData,
    job: jobData,
  })

  return response.data
}

export const scrapeJob = async (url) => {
  const response = await api.post('/api/job/scrape', {
    url,
  })

  return response.data
}

export default api
