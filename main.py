from typing import List


from fastapi import FastAPI
from fastapi import status

from models import User

app = FastAPI()

# path oprations


@app.get(path="/")
def home():
    return {"Twitter API": "Working"}

# Users


@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
)
def signup():
    pass


@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)
def login():
    pass


@app.get(
    path='/user',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass


@app.get(
    path='/user/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass


@app.delete(
    path='/user/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass


@app.put(
    path='/user/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["Users"]
)
def update_a_user():
    pass
# Tweets
