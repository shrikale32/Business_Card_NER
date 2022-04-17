import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import List from './list';

import "../styles/infoCard.css"

InfoCard.propTypes = {

};

const serverUrl = "http://127.0.0.1:8000";

function InfoCard(props) {

    const onSubmit = () => {
        console.log("props123: ", props.cardDetails);

        fetch(serverUrl + "/cards", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                card_id: null,
                user_id: localStorage.getItem('user_sub'),
                user_names: null,
                telephone_numbers: props.cardDetails.phone ? [props.cardDetails.phone] : [''],
                email_addresses: props.cardDetails.email ? [props.cardDetails.email] : [''],
                company_name: props.cardDetails.name ? props.cardDetails.name : '',
                company_website: props.cardDetails.website ? props.cardDetails.website : '',
                company_address: props.cardDetails.address ? [props.cardDetails.address] : [''],
                image_storage: props.cardDetails.image_url
            })
        }).then(response => response.json())
        .then(res=>{
            console.log("res555", res)
        })
        .catch((error)=>{
            console.log(error)
        })
    }
    return (
        <div className="form">
            <div className="title">Business Card Details</div>
            <div className="input-container ic1">
                <input id="name" className="input" type="text" onChange={(event)=>props.handleChangeInput(event,'name')} value={props.cardDetails.name ? props.cardDetails.name : ''} placeholder=" " />
                <div className="cut"></div>
                <label htmlFor="name" className="placeholder">Name</label>
            </div>
            <div className="input-container ic2">
                <input id="phone" className="input" type="text" placeholder=" " onChange={(event)=>props.handleChangeInput(event,'phone')} value={props.cardDetails.phone ? props.cardDetails.phone : ''} />
                <div className="cut"></div>
                <label htmlFor="phone" className="placeholder">Phone</label>
            </div>
            <div className="input-container ic2">
                <input id="email" className="input" type="text" placeholder=" " onChange={(event)=>props.handleChangeInput(event,'email')} value={props.cardDetails.email ? props.cardDetails.email : ''}/>
                <div className="cut cut-short"></div>
                <label htmlFor="email" className="placeholder">Email</label>
            </div>
            <div className="input-container ic2">
                <input id="website" className="input" type="text" placeholder=" " onChange={(event)=>props.handleChangeInput(event,'website')} value={props.cardDetails.website ? props.cardDetails.website : ''} />
                <div className="cut cut-short"></div>
                <label htmlFor="website" className="placeholder">Website</label>
            </div>
            <div className="input-container ic2">
                <input id="address" className="input" type="text" placeholder=" " onChange={(event)=>props.handleChangeInput(event,'address')} value={props.cardDetails.address ? props.cardDetails.address : ''} />
                <div className="cut cut-short"></div>
                <label htmlFor="address" className="placeholder">Address</label>
            </div>
            <button type="text" className="submit" onClick={()=>onSubmit()}>submit</button>
        </div>
    );
}

export default InfoCard;