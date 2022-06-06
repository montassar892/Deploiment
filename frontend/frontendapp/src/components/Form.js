import React, { useState } from 'react'
import { useLocation } from 'react-router-dom'
import "./Formulaire.css"
export default function Form(props) {
const {state : data} = useLocation();
 const Form = (props) => {

  const [name , setName] = useState('')
  const [lastname , setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [phonenum, setPhone_Num] = useState('')
  const [dateofbirth, setDateOfBirth] = useState('')
  const [contact , setContact] = useState('')
  const [profil , setProfil] = useState('')
  const [langues, setLangues] = useState('')
  const [formation, setFormation] = useState('')
  const [projets, setProjects] =useState('')
  const [experiences, setExperiences] = useState('')
  const [competences, setCompetences] =useState('')
  const [autres, setAutres] = useState('')
}
 const downloadTxtFile = () =>{
     const element = document.createElement("a");
     const file = new Blob([document.getElementById("form5Example1").value,
                            document.getElementById("form5Example2").value,
                            document.getElementById("form5Example3").value,
                            document.getElementById("form5Example4").value,
                            document.getElementById("form5Example5").value,
                            document.getElementById("form5Example6").value,
                            document.getElementById("form5Example7").value,
                            document.getElementById("form5Example8").value,
                            document.getElementById("form5Example9").value,
                            document.getElementById("form5Example10").value,
                            document.getElementById("form5Example11").value,
                            document.getElementById("form5Example12").value], {
       type:"text/plain;charset=utf-8",
     });
     element.href = URL.createObjectURL(file);
     element.download = "Doc.txt";
     document.body.appendChild(element);
     element.click();
 };

;
return (
  <div> 
      <form className='alpha' >
         <div className="form-outline mb-4">
            <label class="form-label" for="form5Example1">Name</label>
            <input type="text" id="form5Example1" className="form-control"  value={data.name} />
         </div>
         <div class="form-outline mb-4" >
          <label class="form-label" for="form5Example2" >Email</label>
          <input type="email" className="form-control" id="form5Example2" value={data.email}
        />
          
        </div>
        <div class="form-outline mb-4">
          <label class="form-label" for="form5Example2" >Phone Number</label>
          <input type="tel" className="form-control" id="form5Example3" value={data.phonenum}
          />
        </div>
        <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">Date of birth</label>
          <input type="date" id="form5Example4" class="form-control" value={data.dateofbirth}
        />   
        </div>
        <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">contact</label>
          <input type="text" id="form5Example5" class="form-control" value={data.contact} 
        /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">profil</label>
          <input type="text" id="form5Example6" class="form-control" value={data.profil}
         /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">langues</label>
          <input type="text" id="form5Example7" class="form-control" value={data.langues}
        /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">formation</label>
          <input type="text" id="form5Example8" class="form-control" value={data.formation}
       /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">projets</label>
          <input type="text" id="form5Example9" class="form-control" value={data.projets}
         /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">experiences</label>
          <input type="text" id="form5Example10" class="form-control" value={data.experiences}
       /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">competences</label>
          <input type="text" id="form5Example11" class="form-control" value={data.competences}
        /> 
       </div>
       <div className="form-outline mb-4">
          <label class="form-label" for="form5Example2">autres</label>
          <input type="text" id="form5Example12" class="form-control" value={data.autres}
         /> 
       </div>
       <button type="submit" value ="Submit" className="btn btn-primary" onClick={downloadTxtFile}> Submit </button>
      </form>
  </div>
);
  }
 
