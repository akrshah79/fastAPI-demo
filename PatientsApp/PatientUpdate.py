from pydantic import BaseModel, Field, field_validator

from typing import Optional

class PatientUpdate(BaseModel):
    name: Optional[str] = Field(default=None,description="Changed name of the patient")
    age: Optional[int] = Field(default=None,description="Changed age of the patient in years", example=28)
    weight_kg: Optional[float] = Field(default=None,description="Changed weight of the patient in kilograms", example=70.0)
    height_cm: Optional[float] = Field(default=None,description="Changed height of the patient in centimeters", example=165.0)

    @field_validator('age')
    @classmethod
    def validate_age(cls,v):
        if v is not None and v < 0:
            raise ValueError("Age must be positive")
        return v
    @field_validator('weight_kg')
    @classmethod
    def validate_weight(cls,v):
        if v is not None and v < 0:
            raise ValueError("Weight must be positive")
        return v
    @field_validator('height_cm')
    @classmethod
    def validate_height(cls,v):
        if v is not None and v < 0:
            raise ValueError("Height must be positive")
        return v
    @field_validator('name')
    @classmethod
    def validate_name(cls,v):
        if v is not None and (len(v)<2 or len(v)>50):
            raise ValueError("Name must be between 2 and 50 characters")
        return v
    