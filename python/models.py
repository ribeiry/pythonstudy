import uuid
from typing import Optional
from pydantic import BaseModel,Field

class Encomenda(BaseModel):
    id: str=Field(default_factory=uuid.uuid4, alias="_id")
    endereco: str 
    complemento: str 
    rementente: str
    apto: str
    condominio: str
    destinatario: str
    status: str

    #class Config:
    #    allow_population_by_field_name= True
    #    schema_extra = {
    #        "example": {
    #            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
    #            "endereco": "Avenida Joao de Barros,500",
    #            "complemento": "Bloco A",
    #           "remente": "MercadoLibre",
    #            "apto": "84B",
    #            "status": "Recebido",
    #            "condominio": "vibe",
    #            "destinatario":"Augusto",
    #            "status":"Recebido"
    #        }
    #    }
        
class EncomendaUpdate(BaseModel):
    status: Optional[str]
    apto: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "status": "ENTREGUE",
                "apto": "84B"
            }
        }



class User(BaseModel):
    user: str