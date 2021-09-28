from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! La 💩 {exc.name} hizo algo. Ahy te va un arcoiris...🌈"
        }
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(
            status_code=418, detail="Nope!😒 No me gusta el numero 3")
    return {"item_id": item_id}


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    """
# Un regalo Magico 
Si pides un 🦄 en la ruta del get
optienes un arcoiris 
 """
    if name == "🦄":
        raise UnicornException(name)
    return {"unicorn": name}

items = {"foo": "the foo fighters"}

error = {
    'en': 'Item not found 💥',
    'es': 'Cosa no encontrada 🕵️‍♀️',
    '👾': 'X-Error',
}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     """
#     This function is used to get the item from the items dictionary.
#     # Manejo de Errores
#     - HTTPException
#      """
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail=error,
#             headers={"X-Error": "There goes my error "},
#         )
#     return {"item": items[item_id]}
