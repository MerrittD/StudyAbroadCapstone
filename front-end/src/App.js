import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import './App.css';
import './css/bootstrap.min.css';
import Home from './pages/Home';
import HowTo from './pages/HowTo';
import ContactUs from './pages/ContactUs';
import AdminLogin from './pages/AdminLogin';
import AdminDashboard from './pages/AdminDashboard';
import ResultPage from './pages/ResultPage';

/* Main component which holds the routing to each page */
class App extends Component {
  render() {
    return (
      <div className="App">

        <BrowserRouter basename='/'>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/ResultPage" component={ResultPage} />
            <Route path="/how-to" component={HowTo} />
            <Route path="/contact-us" component={ContactUs} />
            <Route path="/admin-login" component={AdminLogin} />
            <Route path="/admin-dashboard" component={AdminDashboard} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
