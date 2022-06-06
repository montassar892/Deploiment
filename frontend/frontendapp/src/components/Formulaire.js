import React, { useCallback } from "react";
import { useState } from "react";
import axios from 'axios';
import "./Formulaire.css"
import Form from './Form'
import { NavLink } from "react-router-dom";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const Formulaire = (props) => {

const [name, setName] = useState('')
const [lastname , setLastName] = useState('')
const [email, setEmail] = useState('')
const [phonenum, setPhone_Num] = useState('')
const [dateofbirth, setDateOfBirth] = useState('')
const [cv,  setCV] = useState('')
const navigate= useNavigate()



 const handleSubmit = useCallback((e) =>{ 
  
    e.preventDefault();
      // Simple POST request with a JSON body using fetch
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            name: name,
            lastname: lastname,
            email: email,
            phonenum: phonenum,
            dateofbirth: dateofbirth,
            cv: cv })
    };

    const uploadData = new FormData();
    uploadData.append('name', name);
    uploadData.append('lastname', lastname);
    uploadData.append('email', email);
    uploadData.append('phonenum', phonenum);
    uploadData.append('dateofbirth', dateofbirth);
    uploadData.append('cv', cv , cv.name);
    
   

   for (var key of uploadData.entries()) {
    console.log(key[0] + ', ' + key[1]);
  }  


  //  fetch('http://127.0.0.1:8000/Candidatureapi', {
  //     headers : { 
  //       'Content-Type': 'application/json',
  //       'Accept': 'application/json'
  //      },
  //     method: 'POST',
  //     body: uploadData
  //   }).then(response => response.json()).then((data) => console.log(data));
    
  
 axios({
      method: "POST",
      url: "http://127.0.0.1:8000/Candidatureapi",
      data: uploadData,
      headers: { "Content-Type": "multipart/form-data" },
    }).then(function (response) {
        //handle success
        console.log(response.data);
        navigate("/form",{state: response.data});
      }).catch(function (response) {
        //handle error
        console.log(response);
      });
    
    e.preventDefault();

});



return (
  <div> <h1> Register Today  </h1> 
        {/* 
    <div class="image"></div> */}
    <form  className='alpha' onSubmit={handleSubmit}>
    <p> Fill in the data below </p>
        <div className="form-outline mb-4" >
            <label class="form-label" for="form5Example1">Name</label>
            <input type="text" id="form5Example1" className="form-control" 
            onChange={ (e) => setName(e.target.value)}/>
            
       </div>
       <div class="form-outline mb-4" >
            <label >Last Name</label>
            <input type="text" id="form5Example2" class="form-control" 
            onChange={ (e) => setLastName(e.target.value)}/>
            
       </div>
       <div class="form-outline mb-4" >
            <label class="form-label" for="form5Example2" >Email</label>
            <input type="email" className="form-control" id="form5Example3"
            onChange={ (e) => setEmail(e.target.value)}/>
            
       </div>
       <div class="form-outline mb-4">
            <label class="form-label" for="form5Example2" >Phone Number</label>
            <input type="tel" className="form-control" id="form5Example4"
             onChange={ (e) => setPhone_Num(e.target.value)}/>
        </div>
        <div className="form-outline mb-4">
            <label class="form-label" for="form5Example2">Date of birth</label>
            <input type="date" id="form5Example5" class="form-control" 
            onChange={ (e) => setDateOfBirth(e.target.value)}/> 
        </div>
        <div className="form-outline mb-4">
            <label class="form-label" for="form5Example2">Resume</label>
            <input type="file"  id="form5Example5"  accept=".pdf,.doc,.txt"
              className="form-control" 
            onChange={ (e) => setCV(e.target.files[0])}/> 
        </div>   
       {/* <div class="form-check d-flex justify-content-center mb-4">
           <input class="form-check-input me-2" type="checkbox" value="" id="form5Example3" checked />
           <label class="form-check-label" for="form5Example3">
           I have read and agree to the terms
           </label>
       </div>  */}
  
    <Link to = {{ pathname : "/form" , state : "test"}} >
        <button type="submit" value ="Submit" onClick={handleSubmit} className="btn btn-primary"> Submit </button> </Link>
    </form>
 {/*    <section class="extFooter cid-rUEteHRfHV" id="extFooter1-62">
      <div class="container">
        <div class="media-container-row content mbr-white">
            <div class="col-md-3 col-sm-12">
                <div class="mb-3 img-logo">
                    <a href="#top">
                        <img src="assets/images/logo-enginov-194x194.png" alt="Mobirise" title="">
                    </a>
                </div>
                <p class="mb-3 mbr-fonts-style foot-title display-5">Nos offres</p>
                <p class="mbr-text mbr-fonts-style display-7"><strong></strong><strong><a href="transformation_digitale_by_enginov.html#info1-33" class="text-white">Transformation Digitale&nbsp;</a><br><a href="ingenerie_industrielle_by_enginov.html#info1-6d" class="text-white">Ingénierie Industrielle&nbsp;</a><br><a href="digital_factory.html#info1-7v" class="text-white">Digital Factory</a></strong><br><strong><a href="talents.html" class="text-white">Talents<br></a><br></strong></p>
            </div>
            <div class="col-md-4 col-sm-12">
                <p class="mb-4 foot-title mbr-fonts-style display-5">
                    Nos implantations</p>
                <p class="mbr-text mbr-fonts-style display-7">Enginov.Digital<br>La Grande Arche<br>1, parvis de la Défense<br>Paris La Défense Cedex (92044 ) - France<br><br>Enginov.Factory<br>173, Avenue Marcel DASSAUT<br>Beauvais (60000) - France<br><br>Enginov.Indus<br>17, rue Pousse Penil<br>Issoudun (36100) - France<br><br>Enginov.Offshore<br>Batiment Alpha Engineering<br>Route Z4, ZI Saint Gobain <br>Tunis / Saint Gobain (2014) - Tunisie</p>
            </div>
       </div> 
     </div>
    </section>
    
    <section once="footers" class="cid-rRBLG9qwdJ" id="footer1-1e">
        <div class="container">
          <div class="row">
            <div class="media-container-row mbr-white col-lg-12">
              <div class="row-copirayt col-sm-12 col-md-12 col-lg-6">
                <p class="mbr-text mb-0 mbr-fonts-style mbr-white align-left display-7">
                    2022 © ENGINEERING INNOVATION ASSOCIATES sas&nbsp;- All Rights Reserved
                </p>
              </div>
              <div class="row-links col-md-12 col-lg-6">
                <ul class="foot-menu">
                  <li class="foot-menu-item mbr-fonts-style display-7">
                    :: before 
                    <a class="text-white" href="#top">About Us</a>
                  </li></ul>
              </div>
            </div>
          </div>
         </div>
    </section>
  */}
  </div>
    );};

    export default Formulaire;

