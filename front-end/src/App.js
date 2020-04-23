import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import { Security, SecureRoute, LoginCallback } from '@okta/okta-react'
import './App.css';
import './css/bootstrap.min.css';
import Home from './pages/Home';
import AdminDashboard from './pages/AdminDashboard';
import NavBar from './components/NavBar'

/* Variables used by Okta for authentication */
const OKTA_DOMAIN = 'dev-228327.okta.com';
const CLIENT_ID = '0oa5ecwl6wmPJFY0l4x6';
const CALLBACK_PATH = '/implicit/callback';
const ISSUER = `https://${OKTA_DOMAIN}/oauth2/default`;
const HOST = window.location.host;
const REDIRECT_URI = `http://${HOST}${CALLBACK_PATH}`;
const SCOPES = 'openid profile email';
/* Our config variable that stores information to be used by the Security tag, courtesy of Okta */
const config = {
  issuer: ISSUER,
  clientId: CLIENT_ID,
  redirectUri: REDIRECT_URI,
  scope: SCOPES.split(/\s+/),
}

/* Main component which holds the routing to each page 
  Our routes are wrapped in a Security tag, which is necessary for authentication 
  We also have a SecureRoute that signifies the user must be authenticated before viewing or accessing that page*/
class App extends Component {
  render() {
    return (
      <Router>
        <Security {...config}>
          <NavBar />
          <div className="container">
            <Route exact path="/" component={Home} />
            <Route path='/implicit/callback' component={LoginCallback} />
            <SecureRoute exact path="/admin-dashboard" component={AdminDashboard} />
          </div>
        </Security>
      </Router>
    );
  }
}

export default App;
