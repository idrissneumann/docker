import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export class ToDoELt {
  id: number;
  title: string;
  todo_description: string;
}
export class ToDoList {
  todos: ToDoELt[];
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title: string = 'TO DO LIST';
  displayedColumns: string[] = ['id', 'title', 'todo_description', 'delete'];
  dataSource: ToDoList = new ToDoList();
  basic_url: string = "http://127.0.0.1:5000/api/v1/todo";
  httpOptions = {
    headers: new HttpHeaders({ 
      'Content-Type': 'application/json;charset=UTF-8',
      'Accept': 'application/json;charset=utf-8',
      'Access-Control-Allow-Origin': '*',
      'Cross-Domain': 'true'
    }),
    withCredentials: false,
    mode: 'no-cors'
  };
  form: ToDoELt = new ToDoELt();

  /**
   * Constructor
   * @param http: HttpClient
   */
  constructor(private http: HttpClient) {
    this.getAll().then(list => {this.dataSource = list});
  }

  /**
   * get data of path
   */
  public getAll(): Promise<ToDoList> {
    return this.http.get(this.basic_url, this.httpOptions).toPromise().then(response => response as ToDoList);
  }

  /**
   * Create a new TODO
   */
  public create(){
    var newToDo:ToDoELt = new ToDoELt();
    newToDo.id = this.form.id;
    newToDo.title = this.form.title;
    newToDo.todo_description = this.form.todo_description;
    this.dataSource.todos.push(newToDo);
    this.form = new ToDoELt();
    this.http.post(this.basic_url, newToDo, this.httpOptions).toPromise().then(response => response as ToDoELt).then(resp => {this.dataSource.todos.push(resp); window.location.reload();});
  }

  /**
   * remove an element
   * @param id 
   */
  public delete(elt:ToDoELt){
    const url = `${this.basic_url}/${elt.id}`;
    this.http.delete(url, this.httpOptions).toPromise().then(resp => {this.dataSource.todos.splice(this.dataSource.todos.indexOf(elt), 1); window.location.reload();});
  }
}
