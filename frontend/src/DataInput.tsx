import { useState } from 'react'

function DataInput() {
    const [repoUrl, setRepoUrl] = useState('')
    const [notes, setNotes] = useState('')

    return (
        

        <div className="form-container">
            <div className="input-group">
                <label>Enter Repo URL:</label>
                <input 
                    type="text" 
                    placeholder="Repo URL" 
                />
            </div>

            <div className="input-group">
                <label>Additional Notes:</label>
                <textarea 
                    rows={4} 
                    placeholder="Notes to consider while generating README"
                />
            </div>

        </div>
    )

}

export default DataInput