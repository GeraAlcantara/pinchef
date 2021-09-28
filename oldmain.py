import uvicorn
from fastapi import FastAPI, Path, Query
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class BaseItem(BaseModel):
    description: str
    type: str
class Item(BaseModel):
    name: str
    description: str

class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str) -> str:
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved!  .not really  ", user_in_db)
    return user_in_db

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.post("/user/", response_model=UserOut)
def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


@app.get("/items/", response_model=List[Item])
async def read_item():
    return items


@app.get('/')
async def root():
    return {"message": "Que onda BANDA!"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str = Field(..., example="Documentacion Chingona")
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300, example="una cosa chida descrita aqui"
    )
    price: float = Field(..., example=10.3)
    tax: Optional[float] = Field(None, title="el impuesto para mantener a papa gobierno", gt=0, example=1.23)
    tags: Set[str] = Field(set(), title="un set osea unico de etiquetas", example={"jamon", "huevos"})
    images: Optional[List[Image]] = Field(None, title="A list of images", example=[{"url": "http://foo.bar/image.png", "name": "Foo"}])
   

class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    item: List[Item]

@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer

@app.post('/images/multiple/')
async def create_multiple_images(images: List[Image]):
    for image in images:
        image.url
    return images

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item ):
    results = {"item_id": item_id, "item": item}
    return results

# Query Parameters and String Validations
@app.get("/items/")
async def read_item(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {'item_id': item_id, **item.dict()} # descomprime el diccionario
    if q:
        result.update({'q': q})
    return result

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    
    return item_dict

# fake db
fake_items_db = [{"item_name": "uno"}, {"item_name": "dos"}, {"item_name": "tres"}]
# Multiple path and query parameters

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id:str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})    
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
    


# Optional parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# Query Parameters


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# Path parameters containing paths

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# create a Enum Class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# simple route

@app.get("/")
async def root():
    return {'saludo': 'Que ondita banda!'}

# dinamic route

# @app.get('/items/{items_id}')
# async def read_item(items_id: int):
#     return {'items_id': items_id}

# order matters

@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}



app = FastAPI()

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# @app.get("/")
# def read_root():
#     return {"Saludo 👋": "Que onda banda como andan 🤩"}


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return { "username": username }


@app.post("/files/")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
    ):
    return {
        "file_sizes": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app.post("/uploadfiles/")
async def create_upload_file(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}