import React, { Component } from 'react';
import ExampleComponent from './components/ExampleComponent'
import ResultHeader from './components/ResultHeader'
import Result from './components/Result'
import SearchBar from './components/SearchBar'
import './App.css';
import './css/bootstrap.min.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="header-comp">
          <ExampleComponent />
        </div>
        <div className="result-category-comp">
          <SearchBar />
          <ResultHeader />
          <Result />

        </div>
      </div>
    );
  }
}

export default App;
