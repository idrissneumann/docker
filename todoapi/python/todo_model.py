class TodoModelGenerator():
    db = None
    model = None

    def __init__(self, db):
        self.db = db

    def query(self):
        model = self.get_model()
        return model.query

    def get_model(self):
        if self.model is not None:
            return self.model

        class Todo(self.db.Model):
            __tablename__ = "todos"
            db = self.db
            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String(20))
            todo_description = db.Column(self.db.String(100))
            
            def create(self):
                self.db.session.add(self)
                self.db.session.commit()
                return self

            def __init__(self, title, todo_description):
                self.title = title
                self.todo_description = todo_description

            def __repr__(self):
                return f"{self.id}"
        
        self.model = Todo
        return self.model
