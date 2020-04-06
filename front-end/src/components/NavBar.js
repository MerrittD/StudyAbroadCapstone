import React from 'react';
import { useOktaAuth } from '@okta/okta-react';

/* A basic navbar with tabs Browse, How To, Contact Us, Admin, and Log Out (only if admin user is logged in */
const NavBar = () => {

    /* Variable to store information on whether user is logged in or not
       Uses Okta's provided useOktaAuth method to determine this  */
    const { authState, authService } = useOktaAuth();
    /* This is essentially the function that we perform to signify the user should be logged out
      e.g. When the user clicks 'Log out', we will invoke this  */
    const logout = async () => authService.logout('/');

    return (
        <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
            <h5 className="my-0 mr-md-auto font-weight-bold"> <a href="/">Study Abroad</a> </h5>
            <a className="btn" href="/">BROWSE</a>
            <a className="btn" href="/how-to">HOW TO</a>
            <a className="btn" href="/contact-us">CONTACT US</a>
            <a className="btn" href="/admin-dashboard">ADMIN</a>

            {authState.isAuthenticated && <a className="btn" onClick={logout}>LOG OUT</a>}
        </div>
    );
}

export default NavBar;
