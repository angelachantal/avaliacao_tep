from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
import uuid

class ProjetoCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: Optional[Literal[1,2,3]] 
    status: Optional[Literal['Planejado', 'Em andamento', 'Concluído', 'Cancelado']]

class Projeto(ProjetoCreate):
    id: uuid.UUID
    criado_em: datetime

class ProjetoUpdate(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    prioridade: Optional[Literal[1,2,3]] 
    status: Optional[Literal['Planejado', 'Em andamento', 'Concluído', 'Cancelado']]