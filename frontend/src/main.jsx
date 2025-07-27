import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styling/index/index.css'
import Index from './components/index/Index.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Index />
  </StrictMode>,
)
