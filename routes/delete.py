from fastapi import APIRouter, Path
from schemas.table_model import local_session, MemberModelTable

app_delete = APIRouter()

@app_delete.delete("/delete_member/{id}")
def delete_member(id: int = Path(..., gt=0)):
    member_to_delete = local_session.query(MemberModelTable).filter(MemberModelTable.membership_id == id).first()

    local_session.delete(member_to_delete)
    local_session.commit()

    return f"Member {id} was deleted successfully."
