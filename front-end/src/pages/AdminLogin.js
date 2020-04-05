import React, { Component } from 'react'
import LoginForm from '../components/login/LoginForm'
import NavBar from '../components/NavBar'

class AdminLogin extends Component {
    render() {
        return (
            <div className="main-login-container">
                <LoginForm />
                <a href="/admin-dashboard">Temporary link to admin dashboard</a>
            </div>
        )
    }
}

export default AdminLogin;