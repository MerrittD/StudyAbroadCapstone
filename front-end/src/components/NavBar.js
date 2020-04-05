import React, { Component } from 'react';


class NavBar extends Component {

    render() {
        return (
            <div id="nav" className="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 border-bottom shadow-sm">
                <h5 className="my-0 mr-md-auto font-weight-bold"> <a href="/">Study Abroad</a> </h5>
                <a className="btn" href="/">BROWSE</a>
                <a className="btn" href="/how-to">HOW TO</a>
                <a className="btn" href="/contact-us">CONTACT US</a>
                <a className="btn" href="/admin-dashboard">ADMIN</a>
            </div>
        );
    }
}

export default NavBar;
