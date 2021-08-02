# Todo API

Une api restful permettant de remplir une TODO List écrite en plusieurs langages.

* [Version Java](./java)
* [Version Python](./python)

## Table des matières

[[_TOC_]]

## Lancez la base de données

```shell
docker-compose up -d todo_db
docker exec -it todo_db psql -U todo todo -c "\i /install.sql"
```

## Les endpoints

### Enregistrer une entrée via l'api

```shell
unit_tests/todoapi$ curl -X POST http://127.0.0.1:5000/api/v1/todo -H "Content-Type: application/json" -d '{"title":"une tâche", "todo_description":"une description de la tâche"}'
{"todo":{"id":1.0,"title":"une t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

### Modifier l'enregistrement via l'api

```shell
unit_tests/todoapi$ curl -X PUT http://127.0.0.1:5000/api/v1/todo/1 -H "Content-Type: application/json" -d '{"title":"la tâche"}'
{"todo":{"id":1.0,"title":"la t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

### Récupérer l'enregistrement via l'API

```shell
unit_tests/todoapi$ curl -X GET http://127.0.0.1:5000/api/v1/todo/1
{"todo":{"id":1.0,"title":"la t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

### Supprimer l'enregistrement via l'API

```shell
unit_tests/todoapi$ curl -X DELETE http://127.0.0.1:5000/api/v1/todo/1
```

### Récupérer tout les enregistements

```shell
unit_tests/todoapi$ curl -X GET http://127.0.0.1:5000/api/v1/todo
{"todos":[{"id":2.0,"title":"une t\u00e2che","todo_description":"une description de la t\u00e2che"},{"id":3.0,"title":"une autre t\u00e2che","todo_description":"une description de la t\u00e2che"}]}
```
