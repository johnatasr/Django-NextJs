# ContactListTop

Projeto desenvolvido para avaliação do processo seletivo da Horus Aeronaves. A aplicação é extremamente simples onde um usuário se cadastra e possue uma lista de contatos
onde é possível cadastrar novos contatos, editar e exluir. A arquitetura da API é desenvolvida sobre conceitos do Clean Architecture, Clean code e DRY, onde são definidas todas 
camadas e suas funções.

## Requisitos
Docker
Python 3.7 >

## Tecnologias
Django
Django RestFramework
JWT Auth
NextJs
Docker
Redis
Black
Postgres

## Iniciando
Passos para configurar o projeto com docker:

1. `cd` na pasta do projeto
2. `docker-compose up --build`

O SPA estará rodando em 'localhost:3000' e a API em localhost:8000


## Como usar ?

### Create User 
Endpoint responsável por criar um usuário, a senha deve ser maior que 8 digitos.

```
curl --request POST \
  --url http://localhost:8000/auth/user/create/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "exemplo",
	"password": "Exemplo@Senh@",
	"email": "exemplo@exemplo.com"
}'

```

Retorno -> Stauts 201

```
    {
    "email": "exemplo@exemplo.com",
    "username": "exemplo" 
    }

```

### Login / Obter Token 
Endpoint responsável por fazer login, o retorno será os tokens de acesso e refresh.

```
curl --request POST \
  --url http://localhost:8000/auth/token/obtain/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "exemplo",
	"password": "Exemplo@Senh@"
}'

```

Retorno -> Stauts 200

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDQ4ODAxNywianRpIjoiODNhZjdlNmNiZGMyNGIxZDg5Y2U5YmIzMDM1MWE1MjIiLCJ1c2VyX2lkIjoxLCJpZCI6MX0.A00Ksh6ss-hvUUM3Ehg7fzCPwNFJugYCgaes3ONgJHQ",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxODk5NjE3LCJqdGkiOiJkZDhkMTU0ZmEwYmI0OWNhYWUxOGFkY2M0ODcyMTRjMSIsInVzZXJfaWQiOjEsImlkIjoxfQ.4-YEed5TrSUsV2nKDtIy9WW-HJGjv03dVOsc9kkwCOU",
  "username": "exemplo",
  "email": "Exemplo@Senh@"
}

```