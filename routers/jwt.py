from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "super-duper-secret"
ALGORITHM = "HS256"


def get_current_user(token: str = Depends(oauth2_scheme)):  # 🔹 FastAPI сам извлекает токен
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/me/")
async def me(user=Depends(get_current_user)):  # 🔹 Получаем пользователя из токена
    return {"user": user}
