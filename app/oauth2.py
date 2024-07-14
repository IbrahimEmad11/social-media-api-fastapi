from datetime import datetime, timedelta
from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from . import schemas, models, database
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

access_token_expires=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
algorithm = os.getenv("ALGORITHM")
secret_key = os.getenv("SECRET_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "login")

def create_jwt_token(data: dict):
    encoded_data = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=int(access_token_expires))
    encoded_data.update({"exp": expire_time})

    access_token = jwt.encode(encoded_data, secret_key, algorithm=algorithm)

    return access_token

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=algorithm)
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    
    return user

