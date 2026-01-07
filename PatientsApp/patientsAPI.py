from fastapi import FastAPI,Path
import json

app=FastAPI()

def getData():
    with open("patient.json","r") as f:
        data=json.load(f)
    return data
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
    
