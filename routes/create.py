from fastapi import APIRouter # To create the app router.
from schemas.table_model import MemberModelTable, local_session # To bring the table member model.
from fastapi import Body # To specify the api member model will come as a body paramether, not query.
from schemas.member_model import MemberModel # To bring the api member model.

app_create = APIRouter()


@app_create.put("/new_member")
# We'll get the info from the api member model and put it into the table model and then commit it.
def create_member(new_member : MemberModel = Body(...)):
    new_member_table = MemberModelTable(first_name=new_member.first_name, 
        last_name=new_member.last_name,
        middle_initial=new_member.middle_initial,
        date_of_birth=new_member.date_of_birth,
        email=new_member.email,
        phone=new_member.phone,
        cellphone=new_member.cellphone,
        address=new_member.address,
        membership_price_paid=new_member.membership_price_paid,
        page=new_member.page
    )
    local_session.add(new_member_table)
    local_session.commit()

    return {"message": "Member was created."}
