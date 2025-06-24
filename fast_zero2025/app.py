from http import HTTPStatus
from fastapi import FastAPI
from fast_zero2025.schemas import Message
from fast_zero2025.schemas import Message, UserSchema
from fast_zero2025.schemas import Message, UserPublic, UserSchema
from fast_zero2025.schemas import Message, UserDB, UserPublic, UserSchema
from http import HTTPStatus
from fast_zero2025.schemas import Message, UserDB, UserList, UserPublic, UserSchema
from fastapi import FastAPI, HTTPException

app = FastAPI()
database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/')
def create_user():
    ...

# ...

@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    ...
    
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    ...
    
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)  

    database.append(user_with_id)

    return user_with_id

def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
    

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1: 


        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        ) 



    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id 



    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}