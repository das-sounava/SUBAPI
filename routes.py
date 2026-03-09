from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

def get_current_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def require_premium(user: models.User = Depends(get_current_user)):
    if user.role != "Premium":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Premium subscription required"
        )
    return user

@router.post("/users/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = models.User(username=user.username, role="Free")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/users/{user_id}/upgrade", response_model=schemas.UserResponse)
def upgrade_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.role == "Premium":
        raise HTTPException(status_code=400, detail="User is already Premium")
    user.role = "Premium"
    db.commit()
    db.refresh(user)
    return user

@router.get("/content/free")
def read_free_content():
    return {"message": "Here is some free content for anyone to read."}

@router.get("/content/premium")
def read_premium_content(user: models.User = Depends(require_premium), db: Session = Depends(get_db)):
    new_log = models.ActivityLog(user_id=user.id, endpoint_accessed="/content/premium")
    db.add(new_log)
    db.commit()
    
    return {"message": f"Welcome, {user.username}! Here is your highly exclusive premium content."}


