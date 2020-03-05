import React, { Component } from 'react'


const regexp = RegExp(/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/)

const initState = {
    checked: true,
    email: '',
    password: '',
    emailError: '',
    passwordError: ''
}

class LoginForm extends Component {

    state = initState;

    handleEmailChange = e => {
        this.setState({
            email: e.target.value
        })
    }

    handlePasswordChange = e => {
        this.setState({
            password: e.target.value
        })
    }

    // Validate
    validate = () => {
        let inputError = false;
        const errors = {
            emailError: '',
            passwordError: ''
        }

        if (!this.state.email) {
            inputError = true;
            errors.emailError = 'Please enter a valid email'
        } else if (!this.state.email.match(regexp)) {
            inputError = true;
            errors.emailError = (
                <span style={{ color: 'red' }}>Your email address must be valid</span>
            )

        }

        if (this.state.password.length < 8) {
            inputError = true;
            errors.passwordError = "Your password must be between 8-16 characters"
        }

        this.setState({
            ...errors
        })

        return inputError;
    };

    onSubmit = e => {
        e.preventDefault()
        const err = this.validate();
        if (!err) {
            this.setState(initState);
        }
    }

    // Checkbox
    handlerCheckbox = e => {
        this.setState({
            checked: e.target.checked
        })
    }

    render() {
        return (
            /*<FormContainer>*/
            <div className="form-container">
                <form>
                    <h1>Sign In</h1>
                    <div className="input-container">
                        <input
                            className={this.state.emailError
                                ? 'input-error input-empty'
                                : 'input-empty'
                            }
                            type="email"
                            onChange={this.handleEmailChange}
                            value={this.state.email}
                            required />
                        <label>Email</label>
                        <span style={{ color: '#db7302' }}>{this.state.emailError}</span>
                    </div>
                    <div className="input-container">
                        <input
                            className={this.state.passwordError
                                ? 'input-error input-empty'
                                : 'input-empty'
                            }
                            type="password"
                            onChange={this.handlePasswordChange}
                            value={this.state.password}
                            required />
                        <label>Password</label>
                        <span style={{ color: '#db7302' }}>{this.state.passwordError}</span>
                    </div>
                    <div className="input-container">
                        <button type="submit" onClick={e => this.onSubmit(e)}>Sign In</button>
                    </div>
                    <label className="checkbox-container">
                        Remember me
                            <input type="checkbox"
                            defaultChecked={this.state.checked}
                            onChange={this.handleCheckbox} />
                        <span className="checkmark"></span>
                    </label>
                </form>
            </div>
            /*</FormContainer >*/
        )
    }
}

export default LoginForm;