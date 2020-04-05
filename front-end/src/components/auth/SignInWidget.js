import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import OktaSignIn from '@okta/okta-signin-widget';


class SignInWidget extends Component {
    componentDidMount() {
        const el = ReactDOM.findDOMNode(this);
        this.widget = new OktaSignIn({
            baseUrl: this.props.baseUrl,
            authParams: {
                pkce: true
            }
        });
        this.widget.renderEl({ el }, this.props.onSuccess, this.props.onError);
    }

    componentWillUnmount() {
        this.widget.remove();
    }

    render() {
        return <div />;
    }
};

export default SignInWidget;