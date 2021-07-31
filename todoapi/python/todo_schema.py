from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class TodoSchemaGenerator():
    db = None
    model = None

    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get_schema(self, many = False, only = None):
        class TodoSchema(ModelSchema):
            class Meta(ModelSchema.Meta):
                model = self.model.get_model()
                sqla_session = self.db.session

            id = fields.Number(dump_only=True)
            title = fields.String(required=True)
            todo_description = fields.String(required=True)
        return TodoSchema(many = many, only = only)
