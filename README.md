# Equipe:
1. Audemário Alves Monteiro Filho
(e só)

# API do Projeto de Voluntariado

API para permanencia de dados da aplicação android VoluntariadoSuper, esta API é responsável por gerenciar toda a lógica de negócio, autenticação de usuários, perfis e a funcionalidade de busca geoespacial.

## Tecnologias Utilizadas

O backend foi construído com um conjunto das seguintes tecnologias>

- **Python 3**:
- **FastAPI**: Framework web da APIs. foi utilizado para definir todas as rotas (endpoints), gerenciar as requisições e respostas, e validar os dados de entrada e saída usando modelos Pydantic.
- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional.
- **PostGIS**: Uma extensão para o PostgreSQL que adiciona suporte para objetos geográficos, permitindo a execução de consultas espaciais. É a tecnologia central que possibilita a busca por voluntários e organizações em um determinado raio geográfico no APP, como alternativa a usar a API do Google MAPS.
- **SQLAlchemy**: ORM para integrar o código da API FAST com o Banco de Dados PostGreSQL
- **Alembic**: Ferramenta de migração de banco de dados, serve para comparar os modelos com o estado atual do banco de dados e verificar mudanças e atualizações, gera scripts de migração de forma automática.
- **Uvicorn**: Servidor ASGI do FastAPI.





## Estrutura do Banco de Dados e Tipos de Usuários

A arquitetura de dados foi projetada para ser flexível e separar as informações de autenticação das informações de perfil.

### Tabela `users`

Esta é a tabela central de autenticação. Ela armazena as informações essenciais para o login e controle de acesso de qualquer usuário, independentemente do seu tipo.
- `id`: Identificador único.
- `email`: Usado para o login (deve ser único).
- `hashed_password`: A senha do usuário, armazenada de forma segura.
- `user_type`: Um campo crucial do tipo `Enum` que define se o usuário é um **'volunteer'** ou uma **'organization'**.

### Tabelas principais de Perfil

Para cada usuário na tabela `users`, existe um perfil correspondente em uma de duas tabelas, ligado pelo `user_id`.

1.  **Tabela `volunteer_profiles`**:
    - Armazena informações específicas de um voluntário, como `full_name`, `education` (escolaridade) e uma breve `description`.
    - Contém a coluna `location` do tipo `geometry(POINT)`, que armazena a latitude e longitude do voluntário, essencial para a busca.

2.  **Tabela `organization_profiles`**:
    - Armazena informações específicas de uma organização, como `org_name`, `area` de atuação, `vacancies` (vagas), `volunteer_days` e `volunteer_hours`.
    - Também possui uma coluna `location` do tipo `geometry(POINT)` para sua localização geográfica.

Essa estrutura permite que um usuário seja autenticado de forma unificada, enquanto seus dados de perfil são mantidos em tabelas separadas e especializadas, evitando colunas nulas e mantendo o modelo de dados limpo.

![capturadetela](https://github.com/Pizzade42queijos/PDM_IFPE_API_PRJ/blob/main/API.png)

A API foi gerada para abrir no endereço local padrão `http://127.0.0.1:8000`, e a documentação interativa em `http://127.0.0.1:8000/docs`. Sendo preciso os comandos padrão apenas para execução de API FAST
