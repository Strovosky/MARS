from pydantic import BaseModel, Field, EmailStr, AnyUrl # To create the model / To validate info.
from typing import Optional
from datetime import date

class MemberModel(BaseModel):
    first_name : str = Field(..., max_length=50)
    last_name : str = Field(..., max_length=60)
    middle_initial : Optional[str] = Field(None, max_length=3)
    date_of_birth : Optional[date] = Field(None)
    email : Optional[EmailStr] = Field(None)
    phone : Optional[int] = Field(None)
    cellphone : Optional[int] = Field(None)
    address : str = Field(..., max_length=200)
    is_active_member : bool = Field(...)
    membership_price_paid : int = Field(...)
    page : Optional[AnyUrl] = Field(None)


class MemberModelUpdate(BaseModel):
    first_name : str = Field(None, max_length=50)
    last_name : str = Field(None, max_length=60)
    middle_initial : Optional[str] = Field(None, max_length=3)
    date_of_birth : Optional[date] = Field(None)
    email : Optional[EmailStr] = Field(None)
    phone : Optional[int] = Field(None)
    cellphone : Optional[int] = Field(None)
    address : str = Field(None, max_length=200)
    is_active_member : bool = Field(None)
    membership_price_paid : int = Field(None)
    page : Optional[AnyUrl] = Field(None)
