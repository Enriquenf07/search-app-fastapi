from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class User(BaseModel):
    name: str
    id: str

enrique = User(name='Enrique', id='@Enrique')
enzo = User(name='Enzo', id='@Enzo')
bia = User(name='Bia', id='@Bia')
marcia = User(name='Marcia', id='@Marcia')
alex = User(name='Alex', id='@Alex')
messi = User(name='Messi', id='@Messi')

fake_users_db = [
    enrique,
    enzo,
    bia,
    marcia,
    alex,
    messi
]

@app.get("/users/{name}")
async def search_users(name):
    searched_users = []
    for i in fake_users_db:
        if name.lower() in i.name.lower():
            searched_users.append(i)
    return {'users': searched_users}
