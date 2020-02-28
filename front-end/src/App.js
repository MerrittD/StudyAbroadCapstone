import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import ExampleComponent from './components/ExampleComponent'
import ResultHeader from './components/ResultHeader'
import Result from './components/Result'
import SearchBar from './components/SearchBar'
import './App.css';
import './css/bootstrap.min.css';
import Homepage from './pages/Homepage';
import ResultList from './pages/ResultList';

class App extends Component {
  render() {
    return (
      <div className="App">

        <BrowserRouter basename='/'>
          <Switch>
            <Route exact path="/" component={Homepage} />
            <Route path="/ResultList" component={ResultList} />
          </Switch>
        </BrowserRouter>



      </div>
    );
  }
}

export default App;
