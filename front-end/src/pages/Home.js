import { useOktaAuth } from '@okta/okta-react';
import React, { useState, useEffect } from 'react';
import { Button, Header } from 'semantic-ui-react';

const Home = () => {
    const { authState, authService } = useOktaAuth();
    const [userInfo, setUserInfo] = useState(null);

    useEffect(() => {
        if (!authState.isAuthenticated) {
            // When user isn't authenticated, forget any user info
            setUserInfo(null);
        } else {
            authService.getUser().then((info) => {
                setUserInfo(info);
            });
        }
    }, [authState, authService]); // Update if authState changes

    const login = async () => {
        authService.login('/admin-dashboard');
    };
    const logout = async () => authService.logout('/');
    /* Maybe not need
        const resourceServerExamples = [
            {
                label: 'Node/Express Resource Server Example',
                url: 'https://github.com/okta/samples-nodejs-express-4/tree/master/resource-server',
            },
            {
                label: 'Java/Spring MVC Resource Server Example',
                url: 'https://github.com/okta/samples-java-spring-mvc/tree/master/resource-server',
            },
        ];*/

    if (authState.isPending) {
        return (
            <div>Loading...</div>
        );
    }

    return (
        <div>
            <div>
                <Header as="h1">PKCE Flow w/ Okta Hosted Login Page</Header>

                {authState.isAuthenticated && !userInfo
                    && <div>Loading user information...</div>}

                {authState.isAuthenticated && userInfo
                    && (
                        <div>

                            <Button id="logout-button" primary onClick={logout}>Logout</Button>
                        </div>
                    )}

                {!authState.isAuthenticated
                    && (
                        <div>

                            {authState.isAuthenticated && <Button id="logout-button" primary onClick={logout}>Logout</Button>}

                        </div>
                    )}

            </div>
        </div>
    );
};
export default Home;