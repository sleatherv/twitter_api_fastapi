from typing import List


from fastapi import FastAPI
from fastapi import status

from models import User, Tweet

app = FastAPI()

# path oprations

## Users

### Register a user
@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["Users"]
)
def signup():
    """
    This path operation register a user in the app

    Parameters:
        -Request body parameter
            - user: UserRegister
    
    Return a json with the basic user information:
        - user_id: UUID
        - email: Emailstr
        - last_name: str
        - birth_date: str
    """
    pass


# Login a user
@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["Users"]
)
def login():
    pass

# Show all users


@app.get(
    path='/user',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass

# Show a user


@app.get(
    path='/user/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass

# Delete a user


@app.delete(
    path='/user/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["Users"]
)
def delete_a_user():
    pass

# Update a user


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
### Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter API": "Working"}


### Post a tweet
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass


### Show a tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass


### Delete a tweet
@app.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass


### Delete a tweet
@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass