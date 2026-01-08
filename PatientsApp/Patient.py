from pydantic import BaseModel, Field, computed_field, field_validator


class Patient(BaseModel):
    patient_id: str=Field(...,description="Unique identification for the patient", example="P001")
    name: str=Field(..., description="Full name of the patient", example="John Doe")
    age: int=Field(...,description="Age of the patient in years", example=30)
    weight_kg: float=Field(...,description="Weight of the patient in kilograms",example=70.5)
    height_cm: float=Field(...,description="Height of the patient in centimeters", example=175.0)

    @computed_field
    @property
    def bmi(self)->float:
        return self.weight_kg/((self.height_cm/100)**2)
    
    @computed_field
    @property
    def notes(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal BMI"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        elif 30 <= self.bmi < 35:
            return "Obese (requires follow-up)"
        else:
            return "Severe Obesity"

    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v
    
    @field_validator('weight_kg')
    @classmethod
    def validate_weight(cls,v):
        if v<0:
            raise ValueError("Weight must be positive")
        return v
    
    @field_validator('height_cm')
    @classmethod
    def validate_height(cls,v):
        if v<0:
            raise ValueError("Height must be positive")
        return v
    
    @field_validator('name')
    @classmethod
    def validate_name(cls,v):
        if len(v)<2 or len(v)>50:
            raise ValueError("Name must be between 2 and 50 characters")
        return v
    
