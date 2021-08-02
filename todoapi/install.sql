DROP TABLE IF EXISTS todos CASCADE;

CREATE TABLE todos (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(254), 
    todo_description VARCHAR(254)
);
