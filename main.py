from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()
# Specific pyndatic model
class post(BaseModel): # Extends base model
    title:str
    content:str
    published:bool= True  # can also run without defining oin body of jdon with value true.
    rating:Optional[int]=None

my_post=[{"title":"title of post 1","content":"content od post 1","id":1},{"title":"favourite food","content":" I like pizza","id":2}]


def find_post(id):
    for p in my_post:
        if p["id"]==id:
            return p


def find_index(id):
    for i,p in enumerate(my_post):
        if p["id"]==id:
            return i








#                                   get()

@app.get("/")
def root():
    return {"message": "Python family py "}
#First one   is prefered if same methods
@app.get("/posts")
def get_post():
    return {"data":my_post}

#                                   post()

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def creatre_post(post:post): # implements pyndamic model describe above
    # print(post.rating)
    # print(post)
    # print(post.dict())
    post_dict=post.dict()
    post_dict["id"]=randrange(1,10000)
    my_post.append(post_dict)
    return {"data":post_dict}
#   return {"message": "Succesfully created post "}

#                                   Order matters
'''
@app.get("/posts/latest")
def get_latest_post():
    post=my_post[len(my_post)-1]
    return {"detail":post }
'''
@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    # print(id,type(id))
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} wad not found" )
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id {id} wad not found"}
    # print(post)
    
    return {"post_Detail":post}

#                   Delete post
# 
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
     # find the index of the array that has required ID
     # my_post.pop(index)
     index=find_index(id)

     my_post.pop(index)
     return {"message":"post was successfully deleted"}