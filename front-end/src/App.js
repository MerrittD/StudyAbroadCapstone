import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, useHistory } from 'react-router-dom'
import { Security, SecureRoute, ImplicitCallback } from '@okta/okta-react'
import './App.css';
import './css/bootstrap.min.css';
import Home from './pages/Home';
import HowTo from './pages/HowTo';
import ContactUs from './pages/ContactUs';
import AdminDashboard from './pages/AdminDashboard';
import ResultPage from './pages/ResultPage';
import NavBar from './components/NavBar'
import Login from './pages/Login';


function onAuthRequired({ history }) {
  history.push('/login');
}


/* Main component which holds the routing to each page */
class App extends Component {
  render() {
    return (
      <Router>
        <Security issuer='https://dev-228327.okta.com/oauth2/default'
          clientId='0oa5ecwl6wmPJFY0l4x6'
          redirectUri={window.location.origin + '/implicit/callback'}
          onAuthRequired={onAuthRequired}
          pkce={true} >
          <NavBar />
          <div className="container">
            <Route exact path="/" component={Home} />
            <Route path="/ResultPage" component={ResultPage} />
            <Route path="/how-to" component={HowTo} />
            <Route path="/contact-us" component={ContactUs} />
            <Route path='/login' render={() => <Login baseUrl='https://dev-228327.okta.com' />} />
            <Route path='/implicit/callback' component={ImplicitCallback} />
            <SecureRoute exact path="/admin-dashboard" component={AdminDashboard} />
          </div>
        </Security>
      </Router>
    );
  }
}

export default App;
