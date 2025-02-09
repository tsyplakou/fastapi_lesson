from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from routers import users, tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   await delete_tables()
   print("База очищена")


app = FastAPI(title="Task Manager API", lifespan=lifespan)

# Подключение маршрутов
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}






if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
