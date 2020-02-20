import React, { Component} from "react";
import "./App.css";
import imag from './perfil.jpg';

class App extends Component{
  render(){
    return(
      <div className="App">
        <h1> Hello, World! Juan Dolci Flores</h1>
        <img src={imag} />
      </div>
    );
  }
}

export default App;