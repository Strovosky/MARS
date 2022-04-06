from fastapi import APIRouter, Query
from schemas.table_model import local_session, MemberModelTable
from typing import Optional
from pydantic import EmailStr


app_get = APIRouter()


@app_get.get("/find_all_members")
def find_all_members():
    all_members = local_session.query(MemberModelTable).all()
    return all_members

@app_get.get("/find_member_by")
def find_member_by(
    first_name: Optional[str] = Query(None, max_length=50, example="Marta"),
    last_name: Optional[str] = Query(None, max_length=60, example="Garcia"),
    email: Optional[EmailStr] = Query(None, example="none@bjs.com"),
    phone: Optional[int] = Query(None, gt=999999, lt=10000000, example=2348998),
    cellphone: Optional[int] = Query(None, gt=999999999, lt=10000000000, example=3102348998)):

    all_members = local_session.query(MemberModelTable).all()

    found_members = set()

    for member in all_members:
        if first_name == member.first_name and first_name != None:
            found_members.add(member)
        elif last_name == member.last_name and last_name != None:
            found_members.add(member)
        elif email == member.email and email != None:
            found_members.add(member)
        elif phone == member.phone and phone != None:
            found_members.add(member)
        elif cellphone == member.cellphone and cellphone != None:
            found_members.add(member)
    
    if len(found_members) == 0:
        return {"message": "No member found."}
    else: 
        return found_members
