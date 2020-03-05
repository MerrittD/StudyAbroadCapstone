import React, { Component } from 'react'
import LoginForm from '../components/login/LoginForm'
import NavBar from '../components/NavBar'

class AdminLoginPage extends Component {
    render() {
        return (
            <div className="main-login-container">
                <NavBar />
                <LoginForm />
                <a href="/AdminDashboardPage">Temporary link to admin dashboard</a>
            </div>
        )
    }
}

export default AdminLoginPage;