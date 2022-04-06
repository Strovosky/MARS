from fastapi import APIRouter, Body, Path
from schemas.member_model import MemberModelUpdate
from schemas.table_model import MemberModelTable
from schemas.table_model import local_session

app_update = APIRouter()

@app_update.post("/update_member/{id}")
def member_update(id: int = Path(..., gt=0), member_to_update : MemberModelUpdate = Body(...)):
    member_to_update_table = local_session.query(MemberModelTable).filter(MemberModelTable.membership_id == id).first()

    if member_to_update.address != None:
        member_to_update_table.address = member_to_update.address
    if member_to_update.cellphone != None:
        member_to_update_table.cellphone = member_to_update.cellphone
    if member_to_update.date_of_birth != None:
        member_to_update_table.date_of_birth = member_to_update.date_of_birth
    if member_to_update.email != None:
        member_to_update_table.email = member_to_update.email
    if member_to_update.is_active_member != None:
        member_to_update_table.is_active_member = member_to_update.is_active_member
    if member_to_update.first_name != None:
        member_to_update_table.first_name = member_to_update.first_name
    if member_to_update.last_name != None:
        member_to_update_table.last_name = member_to_update.last_name
    if member_to_update.middle_initial != None:
        member_to_update_table.middle_initial = member_to_update.middle_initial
    if member_to_update.phone != None:
        member_to_update_table.phone = member_to_update.phone
    if member_to_update.page != None:
        member_to_update_table.page = member_to_update.page
    if member_to_update.membership_price_paid != None:
        member_to_update_table.membership_price_paid = member_to_update.membership_price_paid

    return {"message": f"Member {id} was updated."}
