import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';

// read the host from environment variables
const host = process.env.REACT_APP_API_HOST || 'localhost:5000';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const submitForm = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('image', file);
    
    const response = await fetch(`http://${host}/upload`, {
      method: 'POST',
      body: formData,
    });

    const data = await response.text();
    setResult(data);

    // Clear the file input
    setFile(null);
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  return (
    <div>
    <div className="App d-flex justify-content-center align-items-center">

      <div className="App-header p2 alight-items-center">
        <h1>Image Upload</h1>
        <h2>ID card classifier</h2>
      </div>
    </div>
    <div className='d-flex justify-content-center align-items-center'>
      <div class="form-group">
        <form onSubmit={submitForm}>
          <input type="file" onChange={handleFileChange} />
          <Button type="submit">Upload</Button>
        </form>
      </div>

      {result && (
        <div>
          <p>Result: {result}</p>
        </div>
      )}

    </div>
    </div>
  );
}

export default App;