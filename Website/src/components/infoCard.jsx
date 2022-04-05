import React from 'react';
import PropTypes from 'prop-types';
import List from './list';

import "../styles/infoCard.css"

InfoCard.propTypes = {

};

function InfoCard(props) {

    return (
        <div className="form">
            <div className="title">Business Card Details</div>
            <div className="input-container ic1">
                <input id="name" className="input" type="text" placeholder=" " />
                <div className="cut"></div>
                <label htmlFor="name" className="placeholder">Name</label>
            </div>
            <div className="input-container ic2">
                <input id="phone" className="input" type="text" placeholder=" " />
                <div className="cut"></div>
                <label htmlFor="phone" className="placeholder">Phone</label>
            </div>
            <div className="input-container ic2">
                <input id="email" className="input" type="text" placeholder=" " />
                <div className="cut cut-short"></div>
                <label htmlFor="email" className="placeholder">Email</label>
            </div>
            <div className="input-container ic2">
                <input id="website" className="input" type="text" placeholder=" " />
                <div className="cut cut-short"></div>
                <label htmlFor="website" className="placeholder">Website</label>
            </div>
            <div className="input-container ic2">
                <input id="address" className="input" type="text" placeholder=" " />
                <div className="cut cut-short"></div>
                <label htmlFor="address" className="placeholder">Address</label>
            </div>
            <button type="text" className="submit">submit</button>
        </div>
    );
}

export default InfoCard;