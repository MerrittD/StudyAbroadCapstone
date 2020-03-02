import React, { Component } from 'react';

class NavBar extends Component {
    render() {
        return (
            <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
                <h5 className="my-0 mr-md-auto font-weight-bold"> <a href="/">Study Abroad</a> </h5>
                <nav className="my-2 my-md-0 mr-md-3">
                    <a className="btn btn-outline-secondary" href="/">BROWSE</a>
                    <a className="btn " href="/HowToPage">HOW TO</a>
                    <a className="btn " href="/ContactUsPage">CONTACT US</a>
                    <a className="btn " href="/AdminLoginPage">ADMIN LOGIN</a>
                </nav>
            </div>
        );
    }
}

export default NavBar;