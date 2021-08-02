package io.comwork.todo.api.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;
import java.sql.Timestamp;

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

    @Column(name = "todo_description")
    String todoDescription;
}
