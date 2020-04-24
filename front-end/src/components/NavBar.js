import React from 'react';
import { useOktaAuth } from '@okta/okta-react';

/* A basic navbar with tabs Browse, How To, Contact Us, Admin, and Log Out (only if admin user is logged in */
const NavBar = () => {

    /* Variable to store information on whether user is logged in or not
       Uses Okta's provided useOktaAuth method to determine this  */
    const { authState, authService } = useOktaAuth();
    /* Whenever the const logout is invoked, we will log the user out by calling the function authService.logout()
      e.g. When the user clicks 'Log out', we will invoke authService.logout() function provided by Okta  */
    const logout = async () => authService.logout('/');

    return (
        <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
            <a href="/" className="my-0 mr-md-auto align-self-start img-fluid"><img src={window.location.origin + '/img/su-logo.png'} /></a>
            <a className="btn" href="/">Search</a>
            <a className="btn" href="https://www.southwestern.edu/study-abroad/contact-us/" target="_blank">Contact Us</a>
            <a className="btn" href="/admin-dashboard">Admin</a>
            {/* Only display the logout tag in the navbar when an admin user is logged in */}
            {authState.isAuthenticated && <button style={{ "cursor": "pointer", "marginLeft": "5px", "marginRight": "14px", "color": "#212529" }} onClick={logout}>Log Out</button>}
        </div>
    );
}

export default NavBar;
