package io.comwork.todo.api.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;

@Entity
@Table(name = "todos")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@SequenceGenerator(name = "todos_seq_generator", sequenceName = "todos_id_seq", allocationSize = 1)
public class Todo {
    @Id
    @Column
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "todos_seq_generator")
    Long id;

    @Column
    String title;

    @JsonProperty("todo_description")
    @Column(name = "todo_description")
    String todoDescription;
}
