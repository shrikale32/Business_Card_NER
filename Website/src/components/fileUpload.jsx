import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import InfoCard from './infoCard';
import '../styles/fileUpload.css';

FileUpload.propTypes = {

};

function FileUpload(props) {
    const [image, setImage] = useState(null);
    const [imageUrl, setImageUrl] = useState(null);

    useEffect(() => {
        if(image){
            setImageUrl(URL.createObjectURL(image));
        }
    },[image])



    function handleOnImageChange(e){
        // console.log("event",e, e.target.files[0])
        setImage(e.target.files[0]);
    }
    console.log("image",image,"imageUrl",imageUrl)
    return (
        <div className="body">
            <div className="container">
                <input id="file" name="file" className="inputfile" type="file" accept="image/*" onChange={handleOnImageChange}></input>
                <label htmlFor="file">Upload an image </label>
                <br/>
            </div>
            <div className="mainContainer">
                {
                imageUrl &&
                <React.Fragment>
                    <div className="imageStyle">
                        <img src={imageUrl} width="600px" height="400px"/>
                    </div>
                    <div className="infoContainer">
                        <InfoCard/>
                    </div>
                </React.Fragment>
                }
            </div>
        </div>
    );
}

export default FileUpload;