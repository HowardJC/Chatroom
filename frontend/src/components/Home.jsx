import React from "react";

function Home() {
    return (
        <React.Fragment>
            <div
                className="w3-container w3-center w3-blue"
                style={{ padding: "2rem" }}>
                <h1 className="w3-jumbo">Data, AI, ML Club</h1>
                <button
                    className="w3-button w3-pink"
                    style={{ marginRight: "1rem" }}>
                    Login
                </button>
                <button className="w3-button w3-pink">Register</button>
            </div>

            <div
                className="w3-container w3-blue"
                style={{ padding: "2rem", marginTop: "2rem" }}>
                <h2>Overall club activities</h2>
                <p>
                    Club info
                </p>
            </div>

            <div
                className="w3-container w3-blue"
                style={{ padding: "2rem", marginTop: "2rem" }}>
                <h2>Division info</h2>
                <p>
                    CLub info
                </p>
            </div>

            <div
                className="w3-container w3-blue"
                style={{ padding: "2rem", marginTop: "2rem" }}>
                <h2>Our weekly topic</h2>
                <p>
                    Club info
                </p>
            </div>
        </React.Fragment>
    );
}

export default Home;