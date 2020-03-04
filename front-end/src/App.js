import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './App.css';
import './css/bootstrap.min.css';
import Browse from './pages/Browse';
import HowToPage from './pages/HowToPage';
import ContactUsPage from './pages/ContactUsPage';
import AdminLoginPage from './pages/AdminLoginPage';
import AdminDashboardPage from './pages/AdminDashboardPage';
import ResultPage from './pages/ResultPage';

/* Main component which holds the routing to each page */
class App extends Component {
  render() {
    return (
      <div className="App">

        <BrowserRouter basename='/'>
          <Switch>
            <Route exact path="/" component={Browse} />
            <Route path="/ResultPage" component={ResultPage} />
            <Route path="/HowToPage" component={HowToPage} />
            <Route path="/ContactUsPage" component={ContactUsPage} />
            <Route path="/AdminLoginPage" component={AdminLoginPage} />
            <Route path="/AdminDashboardPage" component={AdminDashboardPage} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
