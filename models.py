import uuid
from typing import Optional
from pydantic import BaseModel,Field

class Encomenda(BaseModel):
    id: str=Field(default_factory=uuid.uuid4, alias="_id")
    endereco: str = Field(...)
    complemento: str = Field(...)
    rementente: str= Field(...)
    apto: str=Field(...)
    condominio: str=Field(...)
    destinatario: str=Field(...)

    class Config:
        allow_population_by_field_name= True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "endereco": "Avenida Joao de Barros,500",
                "complemento": "Bloco A",
                "remente": "MercadoLibre",
                "apto": "84B",
                "condominio": "vibe",
                "destinatario":"Augusto"
            }
        }



