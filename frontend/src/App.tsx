import { useState } from 'react'
import './App.css'
import DataInput from './DataInput'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="app-container">

      <div className="header">
        <div className="header">
          <h1 className="brand-title">ReadMe Generator</h1>
        </div>
      </div>
      

      <DataInput />
    </div>
  )
}


export default App
