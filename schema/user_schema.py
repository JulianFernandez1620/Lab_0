from pydantic import BaseModel
from typing import Optional

#Esquema para los datos que nos pasaran para ingresar a la base de datos
class user_schema(BaseModel):
    id: Optional[int]
    name: str
    phone: str