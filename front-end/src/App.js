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

const OKTA_DOMAIN = 'dev-228327.okta.com';
const CLIENT_ID = '0oa5ecwl6wmPJFY0l4x6';
const CALLBACK_PATH = '/implicit/callback';

const ISSUER = `https://${OKTA_DOMAIN}/oauth2/default`;
const HOST = window.location.host;
const REDIRECT_URI = `http://${HOST}${CALLBACK_PATH}`;
const SCOPES = 'openid profile email';

const config = {
  issuer: ISSUER,
  clientId: CLIENT_ID,
  redirectUri: REDIRECT_URI,
  scope: SCOPES.split(/\s+/),
}

/* Main component which holds the routing to each page */
class App extends Component {
  render() {
    return (
      <Router>
        <Security {...config}>
          <NavBar />
          <div className="container">
            <Route exact path="/" component={Home} />
            <Route path="/ResultPage" component={ResultPage} />
            <Route path="/how-to" component={HowTo} />
            <Route path="/contact-us" component={ContactUs} />
            <Route path='/implicit/callback' component={ImplicitCallback} />
            <SecureRoute exact path="/admin-dashboard" component={AdminDashboard} />
          </div>
        </Security>
      </Router>
    );
  }
}

export default App;
