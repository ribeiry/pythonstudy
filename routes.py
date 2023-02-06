from fastapi import APIRouter, Body, Request,Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Encomenda

router = APIRouter()

@router.post("/", response_description = "Create a new package", status_code=status.HTTP_201_CREATED, response_model= Encomenda)
def create_package(request: Request, encomenda: Encomenda = Body(...)):
    encomenda = jsonable_encoder(encomenda)
    new_package = request.app.database["encomenda"].insert_one(encomenda)
    create_package = request.app.database["encomenda"].find_one(
        {"_id": new_package.inserted_id}
    )

    return create_package

@router.get ("/", response_description= "List all packages of the build", response_model = List[Encomenda])
def list_packages(resquest: Request):
    encomenda = list(request.app.database["encomenda"].find(limit=1000))
    return encomenda

@router.get ("/{id}", response_description= "List all packages of the build", response_model = List[Encomenda])
def list_packages(id:str, resquest: Request):
    if(encomenda := request.app.database["encomenda"].find_one({"_id": id})) is not None:
        return encomenda
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Package with ID {id} not found")


@router.put("/{id}", response_description= "Update a package", response_model = Encomenda)
def update_package(id: str, request: Request, encomenda: EncomendaUpdate = Body(...)):
    encomenda = {k: v for v in encomenda.dict().items() if v is not None}
    if len(encomenda) >= 1:
        update_result = request.app.database["encomenda"].update_one(
            {"_id": id}, {"$set": encomeda.apto}
        )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID not found")
    
    if( existing_package := request.app.database["encomenda"].find_one({"_id": id})) is not None:
        return existing_package

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with {id} not found")
