import React from "react";

const HeroFour: React.FC = () => {
    return (
        <>
        <div className="human-one">
            <img src="assets/ceo1.svg" alt="" />
            <h1>Surename one</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <p className="ceo">CEO Building One</p>
        </div>

        <div className="human-two">
        <img src="assets/ceo2.svg" alt="" />
        <h1>Surename two</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <p className="ceo">CEO Building One</p>
        </div>
        <div className="human-three">
        <img src="assets/ceo3.svg" alt="" />
        <h1>Surename three</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <p className="ceo">CEO Building One</p>
        </div>
        </>
    )
}

export default HeroFour;