from fastapi import FastAPI, HTTPException, Query, Path, status
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

from .schemas import ProjetoCreate, ProjetoUpdate, Projeto


app = FastAPI(
    title = "API de Gerenciamento de Projetos",
    description = "Projeto desenvolvido para a avaliação de TEP/IFPÌ/2025.1, Turma 366, aluna Ângela Chantal ",
    version = "0.1.0"
)

bd_projetos ={}

@app.get("/projects", response_model = List[Projeto], status_code=status.HTTP_200_OK)
def list_projetos(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0, le=100)):
    projetos = list(bd_projetos.values())
    return projetos[skip:skip + limit]

@app.get("/projects/{project_id}", response_model=Projeto, status_code=status.HTTP_200_OK)
def get_projeto(project_id: str = Path(...)):
    projeto = bd_projetos.get(project_id)
    if not projeto:
        raise HTTPException(status_code=404, detail = "Projeto não encontrado")
    return projeto

@app.post("/projects", response_model=Projeto, status_code=status.HTTP_201_CREATED)
def create_projeto(projeto: ProjetoCreate):
    project_id = str(uuid4())
    new_projeto = Projeto(id=project_id, criado_em=datetime.now(),  **projeto.model_dump()) 
    bd_projetos[project_id] = new_projeto
    return new_projeto

@app.put("/projects/{project_id}", response_model = Projeto, status_code=status.HTTP_200_OK)
def update_projeto(project_id: str, projeto: ProjetoCreate):
    stored_projeto = bd_projetos.get(project_id)
    if not stored_projeto:
        raise HTTPException(status_code=404, detail = "Projeto não encontrado")
    updated_projeto = Projeto(id=project_id, criado_em=stored_projeto.criado_em,**projeto.model_dump())
    bd_projetos[project_id] = updated_projeto
    return updated_projeto

@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_projeto(project_id: str):
    stored_projeto = bd_projetos.get(project_id)
    if project_id in bd_projetos:
        del bd_projetos[project_id]
    else:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")