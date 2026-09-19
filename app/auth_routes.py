from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session  
from datetime import date

from database import SessionLocal
from models import User

from schemas import (
    LoginRequest, Token, UserResponse, UserCreate, UserUpdate
)

from auth import verify_password, get_password_hash, create_access_token

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_active_user(db: Session = Depends(get_db)):
    # Временная заглушка: возвращает первого пользователя из базы
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=401, detail="Не авторизован")
    return user

async def get_admin_user(current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Доступно только для admin")
    return current_user


#1.1
@app.post("/login", response_model=Token)
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.username).first()
    
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Неверный username или password"
        )
    
    token_data = {"sub": user.email, "role": user.role}
    access_token = create_access_token(data=token_data)
    
    return {"access_token": access_token, "token_type": "bearer"}


#1.2
@app.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


#1.3
@app.put("/users/me/password")
async def change_password(
    password_data: dict,  
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    if not verify_password(password_data.get("old_password"), current_user.password_hash):
        raise HTTPException(status_code=400, detail="Старый пароль неверный")
    
    current_user.password_hash = get_password_hash(password_data.get("new_password"))
    db.commit()
    return {"message": "Пароль успешно изменен"}


#1.4
@app.patch("/users/{user_id}/deactivate")
async def deactivate_user(
    user_id: int,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    user.is_active = False
    db.commit()            
    return {"message": f"Пользователь {user_id} деактивирован"}


#1.5
@app.post("/users", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    
    user_dict = user_data.model_dump()
    plain_password = user_dict.pop("password")
    
    new_user = User(
        **user_dict,
        password_hash=get_password_hash(plain_password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return new_user