<?php

use Illuminate\Http\Response;

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->get('/api/v1/todo', function () use ($router) {
    $result = array (
        'todo' => []
    );

    $lines = app('db')->select("SELECT id, title, todo_description FROM todos LIMIT 1000");
    foreach ($lines as $line) {
        array_push($result['todo'], array(
            'id' => $line->id,
            'title' => $line->title,
            'todo_description' => $line->todo_description
        ));
    }

    return json_encode($result, true);
});

$router->get('/api/v1/todo/{id}', function ($id) use ($router) {
    $lines = app('db')->select("SELECT id, title, todo_description FROM todos WHERE id = ?", [$id]);
    $result = array();

    foreach ($lines as $line) {
        $result = array(
            'id' => $line->id,
            'title' => $line->title,
            'todo_description' => $line->todo_description
        );
        return json_encode($result, true);
    }

    return (new Response($result, 404))->header('Content-Type', 'application/json');
});