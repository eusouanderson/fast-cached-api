fast-cached-api/
│
├── src/                     # Código fonte da aplicação
│   ├── main.py              # Arquivo principal onde o FastAPI é inicializado
│   ├── routers/             # Contém os módulos de roteamento
│   │   ├── users.py         # Roteador de usuários
│   │   └── products.py      # Roteador de produtos
│   ├── models/              # Modelos de dados (MongoDB)
│   └── auth.py              # Arquivo de autenticação
│   └── schemas.py           # Arquivo de esquemas
│
├── .env                     # Variáveis de ambiente
├── docker-compose.yml       # Arquivo de configuração do Docker
├── Dockerfile               # Arquivo Dockerfile para construção da imagem
├── pyproject.toml           # Configurações do Poetry
└── README.md                # Documentação do projeto





### Descrição Detalhada dos Diretórios e Arquivos

- **`src/`**: Contém todo o código da aplicação.
  - **`main.py`**: Ponto de entrada da aplicação. Configura e inicializa o FastAPI, incluindo as rotas e dependências principais.
  - **`routers/`**: Contém os módulos de roteamento da API, onde as rotas de cada recurso são definidas.
    - **`users.py`**: Roteador responsável por endpoints de usuários, como login, registro, e gestão de dados de usuários.
    - **`products.py`**: Roteador para endpoints de produtos, incluindo a criação, leitura, atualização e exclusão (CRUD) dos produtos.
  - **`models/`**: Contém os modelos de dados que representam as coleções do MongoDB.
    - **`user_model.py`**: Define o modelo de dados do usuário para ser utilizado no MongoDB.
    - **`product_model.py`**: Define o modelo de dados de produtos, incluindo a estrutura do documento para o MongoDB.
  - **`auth.py`**: Implementa a lógica de autenticação da aplicação, como login, registro e validação de tokens JWT.
  - **`schemas.py`**: Contém esquemas Pydantic para validação de dados de entrada e saída da API, garantindo a integridade e formato adequado.
  - **`dependencies.py`**: Arquivo com dependências e funções reutilizáveis para configuração de banco de dados, cache Redis, e outros componentes compartilhados.

- **`docker-compose.yml`**: Arquivo de configuração do Docker Compose, que permite orquestrar os serviços de contêineres, incluindo o MongoDB, Redis e a aplicação FastAPI.

- **`Dockerfile`**: Define as instruções para construir a imagem Docker para a aplicação. Inclui dependências e etapas de configuração do ambiente da aplicação.

- **`.env`**: Arquivo onde as variáveis de ambiente sensíveis e de configuração são armazenadas, como URIs de conexão com o banco de dados, a chave secreta para JWT, etc.

- **`pyproject.toml`**: Arquivo de configuração do Poetry, onde são definidas as dependências do projeto, além das configurações do ambiente virtual, como o Python versionado e pacotes específicos.

- **`README.md`**: Documentação principal do projeto, onde são explicadas as funcionalidades da API, como rodar a aplicação, pré-requisitos, instalação e contribuições.

- **`.gitignore`**: Arquivo que contém a lista de arquivos e diretórios que não devem ser versionados no repositório Git, como dependências instaladas, arquivos temporários e arquivos sensíveis.


