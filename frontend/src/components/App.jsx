import React from "react";
import Home from "./Home";
import Navbar from "./Navbar";
import Login from "./Login";
import Register from "./Register";
import Chat from "./Chat"
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
    return (
        <React.Fragment>
            <Navbar />
            <Router>
                <Route path="/" exact component={Home} />
                <Route path="/login" exact component={Login} />
                <Route path="/register" exact component={Register} />
                <Route path="/chat" exact component = {Chat} />
            </Router>
        </React.Fragment>
    );
}

export default App;