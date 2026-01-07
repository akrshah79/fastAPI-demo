from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field, model_validator
from typing import Optional

class Item(BaseModel):
    id:int
    name:str
    email:EmailStr
    description:Optional[str]=None
    price:float
    
    @field_validator('email')
    @classmethod
    def validate_email(cls,v):
        validEmails=["gmail.com","yahoo.com","hotmail.com"]
        domain=v.split("@")[-1]
        if domain not in validEmails:
            raise ValueError("Invalid email domain")
        return v
        
    @field_validator('id')
    @classmethod
    def validate_id(cls,v):
        if v<0:
            raise ValueError("ID must be positive")
        return v
    
    @field_validator('price')
    @classmethod
    def validate_price(cls,v):
        if v<0:
            raise ValueError("Price must be positive")
        return v
    
    @field_validator('name')
    @classmethod
    def validate_name(cls,v):
        if len(v)<2 or len(v)>20:
            raise ValueError("Name must be between 2 and 20 characters")
        return v
    
    #Computed Field application 
    @computed_field
    @property
    def discount(self)->float:
        if(self.price>500):
            return self.price*0.1
        else:
            return self.price*0.05
        
    #model_validator application
    @model_validator(mode="after")
    @classmethod
    def check_description_price(cls,model):
        if model.description and model.price<100:
            raise ValueError("Description provided for low price item")
        return model
    
        