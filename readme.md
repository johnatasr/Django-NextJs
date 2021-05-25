# ContactListTop

Projeto desenvolvido para avaliação do processo seletivo da Horus Aeronaves. A aplicação é extremamente simples onde um usuário se cadastra e possue uma lista de contatos
onde é possível cadastrar novos contatos, editar e exluir. A arquitetura da API é desenvolvida sobre conceitos do Clean Architecture, Clean code e DRY, onde são definidas todas 
camadas e suas funções.

## Requisitos
Docker
Python 3.7 >

## Tecnologias
- Django
- Django RestFramework
- JWT Auth
- NextJs
- Docker
- Redis
- Black
- Postgres

## Iniciando
Passos para configurar o projeto com docker:

1. `cd` na pasta do projeto
2. `docker-compose up --build`

O SPA estará rodando em 'localhost:3000' e a API em localhost:8000

## Como usar o Portal ?

1- Crie um usuário em "Sing up", senha deve conter mais de 8 dígitos.
2- Faça o login com as credencias criadas.
3- Na barra superior clique em "Novo contato" e adiocione o contato desejado
4- Na página principal você terá todos contatos cadastrados
5- Clicando em um contato você poderá atualizar e deletar o contato

PS- Caso a lista de contatos não atualize após atualizar ou deletar, aguarde o cache limpar automaticamente após alguns segundos ou, 
pressione CRTL + F5 para limpar o cache do navegador.


## Como usar a API ?

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


### Refresh Token 
Endpoint responsável revalidar o token de acesso.

```
curl --request POST \
  --url http://localhost:8000/auth/token/refresh/ \
  --header 'Content-Type: application/json' \
  --data '{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDkxMzAzMywianRpIjoiMGI3ZmFiZDk0MzAxNDBmMGEyMmQ4ZTk0ZjcyNjJhZTMiLCJ1c2VyX2lkIjoxLCJpZCI6MX0.arVXagDeyYD_9IUquHVRzAN3V0dggJlTM72BAeLef0I"
}
	'
```

Retorno -> Stauts 200

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDQ4ODAxNywianRpIjoiODNhZjdlNmNiZGMyNGIxZDg5Y2U5YmIzMDM1MWE1MjIiLCJ1c2VyX2lkIjoxLCJpZCI6MX0.A00Ksh6ss-hvUUM3Ehg7fzCPwNFJugYCgaes3ONgJHQ",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxODk5NjE3LCJqdGkiOiJkZDhkMTU0ZmEwYmI0OWNhYWUxOGFkY2M0ODcyMTRjMSIsInVzZXJfaWQiOjEsImlkIjoxfQ.4-YEed5TrSUsV2nKDtIy9WW-HJGjv03dVOsc9kkwCOU",
}

```

### Listar Contatos 
Endpoint responsável por listar todos contatos de um usuário cadastrado.

```
curl --request GET \
  --url http://localhost:8000/contacts \
  --header 'Authorization: JWT <ACCESS_TOKEN>'

```

Retorno -> Stauts 200

```
{
  "contacts": [
    {
      "id": 10,
      "name": "Id10",
      "phoneNumber": "899999999"
    },
    {
      "id": 9,
      "name": "Id9",
      "phoneNumber": "899999999"
    },
  ]
}

```

### Obter contato
Endpoint responsável por recuperar um contato específico pelo ID.

```
curl --request GET \
  --url http://localhost:8000/contacts/<ID>/search \
  --header 'Authorization: JWT <ACCESS_TOKEN>'

```

Retorno -> Stauts 200

```
{
  "msg": "",
  "user": {
    "id": 8,
    "name": "Id8",
    "phoneNumber": "899999999"
  }
}

```

### Criar contato
Endpoint responsável por criar um novo contato para o usuário logado.

```
curl --request POST \
  --url http://localhost:8000/contacts \
  --header 'Authorization: JWT <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "NovoContato",
      "phoneNumber": "899999999"
}'

```

Retorno -> Stauts 201

```
{
  "msg": "Contact created",
  "contact": {
    "id": 10,
    "name": "NovoContato",
    "phoneNumber": "899999999"
  }
}
```


### Atualizar contato
Endpoint responsável por atualizar um contato pelo ID passado.

```
curl --request PUT \
  --url http://localhost:8000/contacts/<ID>/update \
  --header 'Authorization: JWT <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "NovoNome",
      "phoneNumber": "8598989899"
  }
'

```

Retorno -> Stauts 200

```
{
  "msg": "Contact updated",
  "contact": {
    "id": <ID>,
    "name": "NovoNome",
    "phoneNumber": "8598989899"
  }
}

```

### Deleter contato
Endpoint responsável por deletar um contato pelo ID passado.

```
curl --request DELETE \
  --url http://localhost:8000/contacts/6/delete \
  --header 'Authorization: JWT <ACCESS_TOKEN>'

```

Retorno -> Stauts 200

```
"User with ID: 6 deleted"

```