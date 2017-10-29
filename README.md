# rest-jwt-permission sample project

[Django Rest JWT Permission](https://github.com/chessbr/rest-jwt-permission) sample project.

The current sample project shows the usage through Django User Groups.

## Running
- Install the `requirements.txt` and run this project `python manage.py runserver`.
- Access the Django Admin and create a group and attach some user for it
- On Django Admin, access the `GroupScope`: `/admin/sample/groupscope/` and start adding the scopes for your group
- Authenticate to the API using some user of that group:

Using [**httpie**](https://httpie.org/):
```
http POST localhost:8000/api-token-auth/ username=admin password=pwd
```

Response:
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjoxLCJleHAiOjE1MDkzMDE1MjEsInNjb3BlcyI6WyJncm91cHZpZXdzZXQ6Y3JlYXRlOnBvc3QiLCJncm91cHZpZXdzZXQ6ZGVzdHJveTpkZWxldGUiLCJncm91cHZpZXdzZXQ6cmV0cmlldmU6Z2V0Il19.AmHRRmgdIyxTrqsJt7uScdJP0Awin734X-jvoutoyAk"
}

```

Use [jwt.io](https://jwt.io/) to check the JWT payload:
```
{
  "email": "admin@admin.com",
  "username": "admin",
  "user_id": 1,
  "exp": 1509301521,
  "scopes": [
    "groupviewset:create:post",
    "groupviewset:destroy:delete",
    "groupviewset:retrieve:get"
  ]
}
```

### Check the permissions are working:

* Create a group (we have `groupviewset:create:post` permission):
```
 http POST localhost:8000/group/ name="New Group" Authorization:"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjoxLCJleHAiOjE1MDkzMDE1MjEsInNjb3BlcyI6WyJncm91cHZpZXdzZXQ6Y3JlYXRlOnBvc3QiLCJncm91cHZpZXdzZXQ6ZGVzdHJveTpkZWxldGUiLCJncm91cHZpZXdzZXQ6cmV0cmlldmU6Z2V0Il19.AmHRRmgdIyxTrqsJt7uScdJP0Awin734X-jvoutoyAk"
```
Response
```
{
    "id": 2,
    "name": "New Group",
    "permissions": []
}
```

* Retrieve the group (we the permission `groupviewset:retrieve:get`):
```
http GET localhost:8000/group/2/ Authorization:"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjoxLCJleHAiOjE1MDkzMDE1MjEsInNjb3BlcyI6WyJncm91cHZpZXdzZXQ6Y3JlYXRlOnBvc3QiLCJncm91cHZpZXdzZXQ6ZGVzdHJveTpkZWxldGUiLCJncm91cHZpZXdzZXQ6cmV0cmlldmU6Z2V0Il19.AmHRRmgdIyxTrqsJt7uScdJP0Awin734X-jvoutoyAk"
```

Response:
```
{
    "id": 2,
    "name": "New Group",
    "permissions": []
}

```

* Patch the group (we have not the permission `groupviewset:partial_update:patch`):
```
http PATCH localhost:8000/group/2/ name="New Name" Authorization:"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX2lkIjoxLCJleHAiOjE1MDkzMDE1MjEsInNjb3BlcyI6WyJncm91cHZpZXdzZXQ6Y3JlYXRlOnBvc3QiLCJncm91cHZpZXdzZXQ6ZGVzdHJveTpkZWxldGUiLCJncm91cHZpZXdzZXQ6cmV0cmlldmU6Z2V0Il19.AmHRRmgdIyxTrqsJt7uScdJP0Awin734X-jvoutoyAk"
```

Response
```
{
    "detail": "You do not have permission to perform this action."
}
```

**Profit!**
