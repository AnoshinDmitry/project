from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.tokens import create_token
from models import schemas
from models.database import get_db

router = APIRouter()


# @router.post("", response_model=schemas.Token, status_code=201)
# def create_token(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
#     return create_token(db=db, user_data=user_data)

@router.post("/create_token", response_model=schemas.Token, status_code=201)
def create_access_token(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
    return create_token(db=db, user_data=user_data)
