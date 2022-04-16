import React, { useState } from "react";
import { CognitoUser, AuthenticationDetails } from "amazon-cognito-identity-js";
import UserPool from "../userPool";

function Login(props) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const onSubmit = (event) => {
        event.preventDefault();

        const user = new CognitoUser({
            Username: email,
            Pool: UserPool,
        });

        const authDetails = new AuthenticationDetails({
            Username: email,
            Password: password,
        });

        user.authenticateUser(authDetails, {
            onSuccess: (data) => {
                console.log("onSuccess: ", data);
                localStorage.setItem('jwt_access_token', data.accessToken.jwtToken);
                localStorage.setItem('user_sub', data.accessToken.payload.sub);
                window.location = '/dashboard';
            },
            onFailure: (err) => {
            console.error("onFailure: ", err);
            },
            newPasswordRequired: (data) => {
            console.log("newPasswordRequired: ", data);
            },
        });
    };
    return (
        <div>
            Login Page <br></br>
            <form onSubmit={onSubmit}>
                <label htmlFor="email">Email</label>
                <input
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                ></input>
                <label htmlFor="password">Password</label>
                <input
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                ></input>

                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;