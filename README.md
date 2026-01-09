# LiftGrid API - Workout Management 🏋️‍♂️

Este projeto é uma API de gerenciamento de competições de Crossfit, desenvolvida durante o bootcamp **Python AI Backend Developer** da **Digital Innovation One (DIO)**. A API permite o cadastro de atletas, centros de treinamento e categorias, utilizando as melhores práticas de desenvolvimento assíncrono com Python.

## 🚀 Sobre o Desafio
O objetivo principal foi construir uma API REST robusta utilizando o framework **FastAPI**. Além do CRUD básico ensinado nas aulas, implementei funcionalidades avançadas para atender aos critérios de avaliação e melhorar a experiência de uso da aplicação.

### 🛠 Tecnologias Utilizadas
- **Python 3.11+**
- **FastAPI** (Framework web moderno e rápido)
- **SQLAlchemy** (ORM para persistência de dados assíncrona)
- **Pydantic** (Validação de dados e criação de Schemas)
- **Alembic** (Gerenciamento de migrações de banco de dados)
- **SQLite** (Banco de dados local para desenvolvimento)
- **Fastapi-pagination** (Biblioteca para paginação de resultados)

## 🌟 Funcionalidades Extras (Diferenciais)
Para este projeto, foram implementadas as seguintes melhorias solicitadas no desafio:

1.  **Filtros Customizados:** * Adicionados filtros por `nome` e `cpf` no endpoint de consulta de todos os atletas (`GET /atletas`).
2.  **Tratamento de Exceções de Integridade:**
    * Implementado tratamento para `sqlalchemy.exc.IntegrityError`. Caso tente-se cadastrar um atleta com um CPF já existente, a API retorna uma mensagem personalizada: *"Já existe um atleta cadastrado com o cpf: x"* com o status code `303 See Other`.
3.  **Paginação Profissional:**
    * Integração com a biblioteca `fastapi-pagination`.
    * Implementação de paginação utilizando `limit` e `offset` para otimizar o carregamento de grandes volumes de dados.
4.  **Schemas de Resposta Customizados:**
    * Criação do `AtletaCustomOut` para garantir que a listagem geral de atletas exiba apenas `nome`, `categoria` e `centro_treinamento`, conforme boas práticas de design de API.

## 🏁 Como Executar o Projeto

### Pré-requisitos
* Python instalado
* Ambiente virtual (venv) configurado

### Instalação
1.  Clone o repositório:
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd liftgridapi
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute as migrações do banco de dados:
    ```bash
    alembic upgrade head
    ```

### Executando a API
```bash
uvicorn liftgridapi.main:app --reload
