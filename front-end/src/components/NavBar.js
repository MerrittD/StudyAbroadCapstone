import React, { Component } from 'react';
import { useAuth0 } from "../react-auth0-spa";

const NavBar = () => {

    const { isAuthenticated, loginWithRedirect, logout } = useAuth0();

    return (
        <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
            <h5 className="my-0 mr-md-auto font-weight-bold"> <a href="/">Study Abroad</a> </h5>

            <a className="btn btn-outline-secondary" href="/">BROWSE</a>
            <a className="btn " href="/how-to">HOW TO</a>
            <a className="btn " href="/contact-us">CONTACT US</a>
            <div>
                {!isAuthenticated && (
                    <button onClick={() => loginWithRedirect({})}>ADMIN LOGIN</button>
                )}

                {isAuthenticated && <button onClick={() => logout()}>LOG OUT</button>}
            </div>

        </div>
    );
};

export default NavBar;
