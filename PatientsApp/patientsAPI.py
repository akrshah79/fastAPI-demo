from fastapi import FastAPI, HTTPException,Path
import json

from fastapi.responses import JSONResponse
from Patient import Patient
from PatientUpdate import PatientUpdate 

app=FastAPI()

def getData():
    with open("patient.json","r") as f:
        data=json.load(f)
    return data

def saveData(data):
    with open("patient.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

@app.get("/")
def hello():
    return {
        "message": "This is the patients data storage application."
    }

@app.get("/patients")
def getPatients():
    return getData()

@app.get("/patients/{patient_id}")
def getPatientById(patient_id: str=Path(..., description="The ID of the patient to retrieve", example="P001")):
#Path parameter is used to speciify that patient_id is part of the URL path
    data=getData()
    for patient in data:
        if patient["patient_id"]==str(patient_id):
            return patient
    return {
        "message": "Patient not found"
    }
    
@app.get("/about/")
def about():
    return {
        "message":"This API is developed to manage patients data."
    }
    
@app.post("/patients/")
def addPatient(patient:Patient):
    data=getData()
    for existing_patient in data:
        if existing_patient["patient_id"]==patient.patient_id:
            raise HTTPException(status_code=400,detail="Patient with this ID already exists.")
    data.append(patient.model_dump())
    saveData(data)
    return JSONResponse(status_code=201, content={"message":"Patient added"})


@app.put("/patients/{patient_id}")
def updatePatient(patient_id:str,patient:PatientUpdate):
    data=getData()
    f=0
    index=0
    for existing_patient in data:
        if existing_patient["patient_id"]==patient_id:
            f=1
            break
        index+=1
    if f==0:
        raise HTTPException(status_code=404,detail="Patient not found.")
    existing_patient_info=data[index]
    # Update the patient information
    updated_patient_info=patient.model_dump(exclude_unset=True)
    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value
    patient_pydantic=Patient(**existing_patient_info)
    data[index]=patient_pydantic.model_dump()
    saveData(data)
    return JSONResponse(status_code=200, content={"message":"Patient updated"})

