import React, { Component } from "react";
import axios from "axios";
import Alert from "./Alert";

class Register extends Component {
    state = { err: "" };

    register = (e) => {
        e.preventDefault();
        console.log("Submitting Register")
        axios
            .post("http://localhost:5000/api/register", {
                Email: document.getElementById("email").value,
                Username: document.getElementById("username").value,
                Password: document.getElementById("password").value,
            })
            .then((res) => {
                console.log(res)
                if (res.data.error) {
                    this.setState({ err: res.data.error });
                } else {
                    this.setState({ register: true });
                }
            });
    };

    render() {
        return (
            <div className="w3-card-4" style={{ margin: "2rem" }}>
                <div className="w3-container w3-blue w3-center w3-xlarge">
                    REGISTER
                </div>
                <div className="w3-container">
                    {this.state.err.length > 0 && (
                        <Alert
                            message={`Check your form and try again! (${this.state.err})`}
                        />
                    )}
                    <form onSubmit={this.register}>
                        <p>
                            <label htmlFor="email">Email</label>
                            <input
                                type="email"
                                class="w3-input w3-border"
                                id="email"
                            />
                        </p>
                        <p>
                            <label htmlFor="username">Username</label>
                            <input
                                type="text"
                                class="w3-input w3-border"
                                id="username"
                            />
                        </p>
                        <p>
                            <label htmlFor="password">Password</label>
                            <input
                                type="password"
                                class="w3-input w3-border"
                                id="password"
                            />
                        </p>
                        <p>
                            <button type="submit" class="w3-button w3-blue">
                                Register
                            </button>
                            {this.state.register && <p>You're registered!</p>}
                        </p>
                    </form>
                </div>
            </div>
        );
    }
}

export default Register;