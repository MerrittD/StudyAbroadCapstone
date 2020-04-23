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
            <h5 className="my-0 mr-md-auto font-weight-bold td-none"> <a href="/">Study Abroad</a> </h5>
            <a className="btn" href="/">Search</a>
            <a className="btn" href="/contact-us">Contact Us</a>
            <a className="btn" href="/admin-dashboard">Admin</a>
            {/* Only display the logout tag in the navbar when an admin user is logged in */}
            {authState.isAuthenticated && <a style={{ "cursor": "pointer", "margin-left": "5px", "margin-right": "14px" }} onClick={logout}>Log Out</a>}
        </div>
    );
}

export default NavBar;
