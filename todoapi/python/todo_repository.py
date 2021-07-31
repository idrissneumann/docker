from todo_schema import TodoSchemaGenerator
from todo_model import TodoModelGenerator
from db_connection import DbConnection

class TodoRepository():
    app = None
    db = None
    schema = None

    def __init__(self, app):
        self.app = app
        db_connection = DbConnection(app)
        self.db = db_connection.get_db()
        self.model = TodoModelGenerator(self.db)
        self.schema = TodoSchemaGenerator(self.db, self.model)

    def create_all(self):
        self.db.create_all()

    def get_all(self):
        get_todos = self.model.query().all()
        todo_schema = self.schema.get_schema(many=True)
        return todo_schema.dump(get_todos)

    def get(self, id):
        get_todo = self.model.query().get(id)
        todo_schema = self.schema.get_schema()
        return todo_schema.dump(get_todo)

    def update(self, id, data):
        get_todo = self.model.query().get(id)
        if data.get('title'):
            get_todo.title = data['title']
        if data.get('todo_description'):
            get_todo.todo_description = data['todo_description']
        self.db.session.add(get_todo)
        self.db.session.commit()
        todo_schema = self.schema.get_schema(only=['id', 'title', 'todo_description'])
        return todo_schema.dump(get_todo)

    def delete(self, id):
        get_todo = self.model.query().get(id)
        self.db.session.delete(get_todo)
        self.db.session.commit()

    def insert(self, data):
        todo_schema = self.schema.get_schema()
        todo = todo_schema.load(data)
        return todo_schema.dump(todo.create())
