import json

from db_connection import DbConnection
from todo_repository import TodoRepository
from todo_model import TodoModelGenerator
from todo_schema import TodoSchemaGenerator

from unittest import TestCase
from unittest.mock import Mock, patch

class Query():
    def all(self):
        return None

    def get(self, id):
        return None

class Schema():
    def dump(self, obj):
        return json.dump(obj)

class Session():
    def commit(self):
        return None

    def add(self, data):
        return None

    def delete(self, data):
        return None

class Todo():
    id = None
    title = None
    todo_description = None

    def __init__(self, id = None, title = None, todo_description = None):
        self.id = id
        self.title = title
        self.todo_description = todo_description

    def __eq__(self, other):
        if isinstance(other, Todo):
            return self.id == other.id and self.title == other.title and self.todo_description == other.todo_description
        return False

class TestRepository(TestCase):
    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    def test_create_all(self, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            # Given
            repository = TodoRepository(None)

            # When
            repository.create_all()

            # Then
            self.assertTrue(db_mock.create_all.called) # test that the sqlalchemy mock has been invoked
            self.assertEqual(1, db_mock.create_all.call_count) # test exactly once invocation

    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch('tests.test_todo_repository.Query', autospec = True)
    @patch('tests.test_todo_repository.Schema', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    @patch.object(TodoModelGenerator, 'get_model', lambda x: None)
    def test_get_all(self, schema_mock, query_mock, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'query', lambda x: query_mock):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, many: schema_mock):
                    # Given
                    payload = {"todos": [{"id": 1, "title": "test", "todo_description": "desc"}]}
                    dump_method_mock = Mock()
                    all_method_mock = Mock(return_value = payload)
                    schema_mock.dump = dump_method_mock
                    query_mock.all = all_method_mock
                    repository = TodoRepository(None)

                    # When
                    repository.get_all()

                    # Then
                    self.assertTrue(query_mock.all.called)
                    self.assertTrue(schema_mock.dump.called)
                    all_method_mock.assert_called_once() # another way to ensure that the method all has been invoked exactly once
                    dump_method_mock.assert_called_once_with(payload) # ensure that the payload is passed as an arg to the schema.dump

    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch('tests.test_todo_repository.Query', autospec = True)
    @patch('tests.test_todo_repository.Schema', autospec = True)
    @patch('tests.test_todo_repository.Session', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    @patch.object(TodoModelGenerator, 'get_model', lambda x: None)
    def test_update_only_title(self, session_mock, schema_mock, query_mock, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'query', lambda x: query_mock):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, only: schema_mock):
                    # Given
                    id = 1
                    payload = Todo(id=id, title="test", todo_description="desc")
                    expected_payload = Todo(id=id, title="newtitle", todo_description="desc")
                    patched_payload = json.loads('{"title": "newtitle"}')
                    dump_method_mock = Mock()
                    add_method_mock = Mock()
                    get_method_mock = Mock(return_value = payload)
                    db_mock.session = session_mock
                    query_mock.get = get_method_mock
                    schema_mock.dump = dump_method_mock
                    session_mock.add = add_method_mock
                    repository = TodoRepository(None)

                    # When
                    repository.update(id, patched_payload)

                    # Then
                    get_method_mock.assert_called_once_with(id)
                    self.assertTrue(session_mock.commit.called)
                    add_method_mock.assert_called_once_with(expected_payload)
                    dump_method_mock.assert_called_once_with(expected_payload)

    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch('tests.test_todo_repository.Query', autospec = True)
    @patch('tests.test_todo_repository.Schema', autospec = True)
    @patch('tests.test_todo_repository.Session', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    @patch.object(TodoModelGenerator, 'get_model', lambda x: None)
    def test_update_only_description(self, session_mock, schema_mock, query_mock, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'query', lambda x: query_mock):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, only: schema_mock):
                    # Given
                    id = 1
                    payload = Todo(id=id, title="test", todo_description="desc")
                    expected_payload = Todo(id=id, title="test", todo_description="new desc")
                    patched_payload = json.loads('{"todo_description": "new desc"}')
                    dump_method_mock = Mock()
                    add_method_mock = Mock()
                    get_method_mock = Mock(return_value = payload)
                    db_mock.session = session_mock
                    query_mock.get = get_method_mock
                    schema_mock.dump = dump_method_mock
                    session_mock.add = add_method_mock
                    repository = TodoRepository(None)

                    # When
                    repository.update(id, patched_payload)

                    # Then
                    get_method_mock.assert_called_once_with(id)
                    self.assertTrue(session_mock.commit.called)
                    add_method_mock.assert_called_once_with(expected_payload)
                    dump_method_mock.assert_called_once_with(expected_payload)

    @patch('flask_sqlalchemy.SQLAlchemy', autospec = True)
    @patch('tests.test_todo_repository.Query', autospec = True)
    @patch('tests.test_todo_repository.Schema', autospec = True)
    @patch('tests.test_todo_repository.Session', autospec = True)
    @patch.object(DbConnection, '__init__', lambda x, y: None)
    @patch.object(TodoModelGenerator, 'get_model', lambda x: None)
    def test_update_title_and_description(self, session_mock, schema_mock, query_mock, db_mock):
        with patch.object(DbConnection, 'get_db', lambda x: db_mock):
            with patch.object(TodoModelGenerator, 'query', lambda x: query_mock):
                with patch.object(TodoSchemaGenerator, 'get_schema', lambda x, only: schema_mock):
                    # Given
                    id = 1
                    payload = Todo(id=id, title="test", todo_description="desc")
                    expected_payload = Todo(id=id, title="newtitle", todo_description="new desc")
                    patched_payload = json.loads('{"todo_description": "new desc", "title": "newtitle"}')
                    dump_method_mock = Mock()
                    add_method_mock = Mock()
                    get_method_mock = Mock(return_value = payload)
                    db_mock.session = session_mock
                    query_mock.get = get_method_mock
                    schema_mock.dump = dump_method_mock
                    session_mock.add = add_method_mock
                    repository = TodoRepository(None)

                    # When
                    repository.update(id, patched_payload)

                    # Then
                    get_method_mock.assert_called_once_with(id)
                    self.assertTrue(session_mock.commit.called)
                    add_method_mock.assert_called_once_with(expected_payload)
                    dump_method_mock.assert_called_once_with(expected_payload)
