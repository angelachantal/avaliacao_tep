### Instalação do UV
``` powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" ```

Após a instalação, reiniciar a máquina.

### Criar diretórios e arquivos da estrutura exemplo do FastAPI 

```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

### Iniciando o projeto
`uv init --app` ou `uv init`

### Adicionar FastAPI como dependência:
```uv add fastapi --extra standard```

### Importar FastAPI:
No arquivo main.py:
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": Hello, World!"}
``` 
### Executar o projeto
```uv run fastapi dev```

### Inicializar o ambiente virtual
```.venv\Scripts\activate```

### Instalação de pacotes
`uv pip install fastapi uvicorn pydantic`

### Endpoints da API (main.py)

Método  | URL               | Descrição                                         | Status Code
------- | ----------------  | ------------------                                | -----------
GET     |/projects          | Retorna a lista de todos os projetos cadastrados  | 200 (Sucesso) ; 422 (Unprocessable Entity)
GET     |/projects/{id}     | Retorna os detalhes de um livro pela Id           | 200 (Sucesso) ; 404 (Not found) ; 422 (Unprocessable Entity)
POST    |/projects          | Cadastra um novo projeto                          | 201 (Created) ; 422 (Unprocessable Entity)
PUT     |/projects/{id}     | Atualiza as informações de um projeto existente   | 200 (Sucesso) ; 404 (Not found) ; 422 (Unprocessable Entity)
DELETE  |/projects/{id}     | Exclui um projeto existente                       | 204 (No Content) ; 404 (Not found) ; 422 (Unprocessable Entity)

### Arquivo Schemas
Neste arquivo definimos os modelos Pydantic (requisições e respostas).
```
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
```

- `class ProjetoCreate(BaseModel)`: Criar projetos. Contém os campos principais: título, descrição, prioridade e status. A prioridade é validada para estar entre 1 e 3, e o status precisa ser um dos quatro válidos (Planejado, Em andamento, Concluído, Cancelado).
- ProjetoUpdate: todos os campos opcionais, para permitir atualização parcial.
- `class Projeto(ProjetoCreate)`: modelo final que inclui id e criado_em, os campos gerados automaticamente.