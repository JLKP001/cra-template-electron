import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Built using CRA electron-builder Template.</p>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>public/electron.js</code> or <code>src/App.js</code> and
          save to reload.
        </p>
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
