from typing import Annotated
from liftgridapi.contrib.schemas import BaseSchema
from pydantic import UUID4, Field


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='rua x, Q02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Marco', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]