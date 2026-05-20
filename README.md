# Mini Projeto 3: Consumo de APIs (Fatec Rio Claro)

Este repositório contém a implementação do terceiro mini projeto da disciplina, focado no desenvolvimento de um servidor de APIs e um cliente para consumo de dados.
O objetivo principal é demonstrar a comunicação padronizada entre sistemas distintos, facilitando a integração de modelos e serviços de forma escalável.

## Estrutura do Projeto
A organização das pastas segue a recomendação oficial do projeto:

Mini-Projeto-3---FastApi/\
├── README.md\
├── requirements.txt       # Dependências do Python (FastAPI, Uvicorn, Requests)\
├── server/                # Backend (Servidor da API)\
│   ├── app/\
│   │   ├── __init__.py\
│   │   └── main.py        # Ponto de entrada do FastAPI\
│   └── .env.example       # Exemplo de variáveis de ambiente do servidor\
└── client/                # Consumo da API (Cliente)\
    ├── main.py            # Script principal de consumo\
    └── .env.example       # Exemplo de variáveis de ambiente do cliente

    
## Tecnologias Utilizadas
Python 3.x\
FastAPI: Framework web moderno e de alta performance.\
Uvicorn: Servidor ASGI de produção.\
Requests: Biblioteca para realizar requisições HTTP no lado do cliente.

## Como Executar o Projeto

1. Preparação do AmbienteRecomendamos a criação de um ambiente virtual:
   
       python -m venv venv
       source venv/bin/activate  # No Windows: venv\Scripts\activate
       pip install -r requirements.txt
   
2. Executar o Servidor\
(Backend) Entre na pasta do servidor e inicie o serviço:

        cd server/app
        uvicorn main:app --reload

      A API estará disponível por padrão em http://127.0.0.1:8000.
   
      _Você pode aceder à documentação interativa em /docs._

4. Executar o Cliente
(Consumo) Em um novo terminal, execute o cliente para consumir os dados da API:

        cd client
        python main.py
   
## Integrantes e Contribuições
Este projeto foi desenvolvido em dupla\
As contribuições individuais podem ser verificadas através do histórico de Pull Requests deste repositório, conforme solicitado no roteiro.

## Integrante 1:
__Brendol Alves__ / [[GitHub](https://github.com/brendolalves)]
## Integrante 2:
__Gabriel Nascimento__ / [[GitHub](https://github.com/Gabriel-nascimento31)]
