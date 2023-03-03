# Django+NextJS

This project was developed to test the integration of NextJs with Django via REST. The application is extremely simple, where a user registers and has a contact list where new contacts can be added, edited, and deleted. The API architecture is developed on Clean Architecture, Clean code, and DRY concepts, where all layers and their functions are defined.

## Requirements
- Docker
- Python 3.7 >

## Technologies
- Django 3
- Django RestFramework
- JWT Auth
- NextJs
- Docker
- Redis
- Postgres

## Getting Started
Steps to set up the project with Docker:

1. `cd` into the project folder
2. `docker-compose up --build`

The SPA will be running on localhost:3000 and the API on localhost:8000.

## How to use the portal ?

- 1- Create a user in "Sign up". The password must be longer than 8 characters.
- 2- Log in with the created credentials.
- 3- In the top bar, click "New contact" and add the desired contact.
- 4- On the main page, you will have all registered contacts.
- 5- By clicking on a contact, you can update and delete it.

Note: If the contact list does not update after updating or deleting, wait for the cache to automatically clear after a few seconds or press CRTL + F5 to clear the browser cache.


## How to use the API ?

### Create User
Endpoint responsible for creating a user, the password must be more than 8 characters.

```
curl --request POST \
  --url http://localhost:8000/auth/user/create/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "example",
	"password": "Example@Password",
	"email": "example@example.com"
}'

```

Return -> Status 201

```
    {
    "email": "example@example.com",
    "username": "example" 
    }

```

### Login / Get Token
Endpoint responsible for logging in. The return will be the access and refresh tokens.

```
curl --request POST \
  --url http://localhost:8000/auth/token/obtain/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "example",
	"password": "Example@Password"
}'

```

Return -> Status 200

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "username": "example",
  "email": "Example@Password"
}


```


### Refresh Token
Endpoint responsible for revalidating the access token.

```
curl --request POST \
  --url http://localhost:8000/auth/token/refresh/ \
  --header 'Content-Type: application/json' \
  --data '{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDkxMzAzMywianRpIjoiMGI3ZmFiZDk0MzAxNDBmMGEyMmQ4ZTk0ZjcyNjJhZTMiLCJ1c2VyX2lkIjoxLCJpZ

```

Retorno -> Stauts 200

```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDQ4ODAxNywianRpIjoiODNhZjdlNmNiZGMyNGIxZDg5Y2U5YmIzMDM1MWE1MjIiLCJ1c2VyX2lkIjoxLCJpZCI6MX0.A00Ksh6ss-hvUUM3Ehg7fzCPwNFJugYCgaes3ONgJHQ",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxODk5NjE3LCJqdGkiOiJkZDhkMTU0ZmEwYmI0OWNhYWUxOGFkY2M0ODcyMTRjMSIsInVzZXJfaWQiOjEsImlkIjoxfQ.4-YEed5TrSUsV2nKDtIy9WW-HJGjv03dVOsc9kkwCOU",
}

```

### List Contacts
This endpoint is responsible for listing all contacts of a registered use

```
curl --request GET \
  --url http://localhost:8000/contacts \
  --header 'Authorization: JWT <ACCESS_TOKEN>'

```

Response -> Status 200

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

### Get Contact
This endpoint is responsible for retrieving a specific contact by ID.

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

### Create Contact
This endpoint is responsible for creating a new contact for the logged-in user.

```
curl --request POST \
  --url http://localhost:8000/contacts \
  --header 'Authorization: JWT <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "NewContact",
      "phoneNumber": "899999999"
}'

```

Response -> Status 201

```
{
  "msg": "Contact created",
  "contact": {
    "id": 10,
    "name": "NewContact",
    "phoneNumber": "899999999"
  }
}

```


### Update Contact
This endpoint is responsible for updating a contact by the ID passed.

```
curl --request PUT \
  --url http://localhost:8000/contacts/<ID>/update \
  --header 'Authorization: JWT <ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --data '{
      "name": "NewName",
      "phoneNumber": "8598989899"
  }

```

Retorno -> Stauts 200

```
{
  "msg": "Contact updated",
  "contact": {
    "id": <ID>,
    "name": "NewName",
    "phoneNumber": "8598989899"
  }
}

```

### Delete Contact
This endpoint is responsible for deleting a contact by the ID passed.

```
curl --request DELETE \
  --url http://localhost:8000/contacts/6/delete \
  --header 'Authorization: JWT <ACCESS_TOKEN>'

```

Retorno -> Stauts 200

```
"User with ID: 6 deleted"

```
