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
      </header>
    </div>
  );
}

export default App;
