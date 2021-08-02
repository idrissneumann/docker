package io.comwork.todo.api.bootstrap;

import io.comwork.todo.api.model.Todo;
import io.comwork.todo.api.repositories.TodoRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class TodoLoader implements CommandLineRunner {
    public final TodoRepository todoRepository;

    public TodoLoader(TodoRepository todoRepository) {
        this.todoRepository = todoRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        loadTodos();
    }

    private void loadTodos() {
        if (todoRepository.count() == 0) {
            todoRepository.save(
                    Todo.builder()
                            .title("Go to market")
                            .todoDescription("Buy eggs from market")
                            .build()
            );
            todoRepository.save(
                    Todo.builder()
                            .title("Go to school")
                            .todoDescription("Complete assignments")
                            .build()
            );
            System.out.println("Sample Todos Loaded");
        }
    }
}
