import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import InfoCard from './infoCard';
import '../styles/fileUpload.css';

FileUpload.propTypes = {

};

const serverUrl = "http://127.0.0.1:8000";

function FileUpload(props) {

    const [image, setImage] = useState(null);
    const [imageUrl, setImageUrl] = useState(null);
    const [cardDetails, setCardDetails] = useState({
        name: '',
        phone: '',
        email: '',
        address: '',
        website: '',
        image_url: '',
    });

    const handleChangeInput = (event,key) => {
        console.log("event", event.target.value, key)
        // cardData[key] = event.target.value
        // setCardData(cardData)
        // props.cardDetails[key] = event.target.value;
        setCardDetails({ ...cardDetails, [key]: event.target.value });

    }

    useEffect(() => {
        if(image){
            setImageUrl(URL.createObjectURL(image));

        }
    },[image])

    useEffect(()=>{
        let jwtAccessToken = localStorage.getItem('jwt_access_token');
        if(!jwtAccessToken){
            window.location = '/login';
        }
    })

    const convertToBase64 = (file) => {
        return new Promise((resolve, reject) => {
          const fileReader = new FileReader();
          fileReader.readAsDataURL(file);
          fileReader.onload = () => {
            resolve(fileReader.result);
          };
          fileReader.onerror = (error) => {
            reject(error);
          };
        });
      };

    async function handleOnImageChange(e){
        setImage(e.target.files[0]);
        // const base64 = await convertToBase64(e.target.files[0]);
        let file = e.target.files[0];
        let converter = new Promise(function(resolve, reject) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => resolve(reader.result
                .toString().replace(/^data:(.*,)?/, ''));
            reader.onerror = (error) => reject(error);
        });
        let encodedString = await converter;

        console.log("here")
        fetch(serverUrl + "/images", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({filename: e.target.files[0].name, filebytes: encodedString})
        }).then(response => response.json())
        .then(result=>{
            console.log("res333", result);
            let fileId = result.fileId;
            let fileUrl = result.fileUrl;

            fetch(serverUrl + "/images/"+fileId+"/recognize_entities", {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: {}
            }).then(response => response.json())
            .then(res=>{
                console.log("res444", res);

                setCardDetails({
                    name: res.name && res.name[0],
                    address: res.address && res.address[0],
                    phone: res.phone && res.phone[0],
                    website: res.url && res.url[0],
                    email: res.email && res.email[0],
                    image_url: fileUrl
                })
            })



        })
        .catch((error)=>{
            console.log(error)
        })
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
                        <InfoCard
                            cardDetails={cardDetails}
                            handleChangeInput={handleChangeInput}
                        />
                    </div>
                </React.Fragment>
                }
            </div>
        </div>
    );
}

export default FileUpload;