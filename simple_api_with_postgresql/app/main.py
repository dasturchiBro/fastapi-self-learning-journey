from fastapi import FastAPI
from .db import engine
from sqlmodel import SQLModel
from .routers import post, user, auth



app = FastAPI()


@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get('/')
async def root():
	return {'message': "Hello World!!!"}

# 07.09.2025 -> https://youtu.be/0sOvCWFmrtA?si=Pv8gYQPFeNF35OHC&t=31140

