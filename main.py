from fastapi import FastAPI, HTTPException, Path as PathParam
import json
from pathlib import Path

app = FastAPI()

DATA_FILE = Path(__file__).parent / "patients.json"


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}


@app.get("/view")
def view():
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = PathParam(..., description="ID of the patient in the DB", examples=["P001"])
):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    return data[patient_id]