from fastapi import APIRouter, Body, Request,Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import logging
from models import Encomenda,EncomendaUpdate,User

logging.config.fileConfig('logging.conf',disable_existing_loggers=False)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_description = "Create a new package", status_code=status.HTTP_201_CREATED)
def create_package(request: Request, encomenda: Encomenda ):
    logger.info("create package method")
    encomenda = jsonable_encoder(encomenda)
    logger.info('routes.py.create_package')
    new_package = request.app.database["encomenda"].insert_one(encomenda)
    create_package = request.app.database["encomenda"].find_one(
        {"_id": new_package.inserted_id}
    )
    logger.info('The package id is' + new_package.inserted_id)

    return create_package

@router.get ("/", response_description= "List all packages of the build", response_model = List[Encomenda])
def list_packages(resquest: Request):
    encomenda = list(resquest.app.database["encomenda"].find(limit=1000))
    logger.info('routes.py.list_packages')
    return encomenda

@router.get ("/{id}", response_description= "List all packages of the build", response_model = Encomenda)
def list_packages(id:str, request: Request):
    logger.info('routes.py.list_packages.id' + id )
    if(encomenda := request.app.database["encomenda"].find_one({"_id": id})) is not None:
        logger.info('routes.py.list_packages.id' + id )
        return encomenda
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Package with ID {id} not found")


@router.put("/{id}", response_description= "Update a package", response_model = EncomendaUpdate)
def update_package(id: str, request: Request, encomenda: EncomendaUpdate):
    encomenda = {k: v for k, v in encomenda.dict().items() if v is not None}
    logger.info('routes.py.update_package.id' + id )
    if len(encomenda) >= 1:
        update_result = request.app.database["encomenda"].update_one(
            {"_id": id}, {"$set": encomenda}
        )
    logger.info('routes.py.update_package.apto')
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with ID not found")
    
    if( existing_package := request.app.database["encomenda"].find_one({"_id": id})) is not None:
        return existing_package

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Package with {id} not found")


@router.get ("/building/{condominio}", response_description= "List all packages of the build", response_model = List[Encomenda])
def list_packages_build(condominio:str,request: Request):
    logger.info("Condominio Name:" + condominio)
    if(encomenda := list(request.app.database["encomenda"].find({"condominio": condominio}))) is not None:
        logger.info('routes.py.list_packages_build')
        return encomenda
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f"Package with Condominio {condominio} not found")

@router.get ("/building/{condominio}/apto/{apto}", response_description= "List all packages of the build", response_model = List[Encomenda])
def list_packages_build_apartment(condominio:str,apto:str,request: Request):
    logger.info("Condominio Name:" + condominio)
    logger.info("Apto:" + apto)
    if(encomenda := list(request.app.database["encomenda"].find({"condominio": condominio, "apto": apto}))) is not None:
        logger.info('routes.py.list_packages_build_apartament')
        return encomenda
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail =f"Package with Condominio {condominio} not found")