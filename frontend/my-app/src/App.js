import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const sendData = () => {
    const data = { message: "Hello from React!" };

    axios.post("https://sample-fastapi-4z53.onrender.com/api/endpoint", data, {
      headers: { 'Content-Type': 'application/json' },
      // 必要に応じてwithCredentialsを有効にする
      // withCredentials: true
    })
    .then(response => {
      console.log("Data sent successfully:", response.data);
      alert("Data sent successfully!");
    })
    .catch(error => {
      console.error("Error sending data:", error);
      alert("Error sending data");
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={sendData}>Send Data</button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;