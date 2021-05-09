import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";

function App() {
  const [dice, setDice] = useState(1);

  const handleClick = async () => {
    const result = await window.api.rollDice();
    setDice(result);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Built using CRA electron-builder-fastapi-python Template.</p>
        <img src={logo} className="App-logo" alt="logo" />
        <button className="Roll-btn" onClick={handleClick}>
          Roll Dice
        </button>
        <p>Dice value from Python: {dice}</p>
        <p>
          Edit <code>public/electron.js</code> or <code>src/App.js</code> and
          save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
