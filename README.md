# tasks-management-system
> a tasks management system apis to manage todo list

![Python Version](https://img.shields.io/badge/python-3.7-blue)
![Repo L](https://img.shields.io/github/license/mikeyangyo/tasks-management-system)

A tasks management system apis to management todo list.
Build with Flask, Mysql, Docker

## Usage example
1. Use below command to start api application.
```sh
docker-compose up -d --build
```
2. run migration commands to create table in MySQL database
```sh
FLASK_APP=app.py flask run-migrations
```

3. visit following api endpoints to interacte with system.
    - List tasks
      ```
      GET /tasks
      ```
    - Retrieve task
      ```
      Get /tasks/:id
      ```
    - Create task
      ```
      POST /tasks
      ```
    - Update task
      ```
      PUT /tasks/:id
      ```
    - Delete task
      ```
      DELETE /tasks/:id
      ```

## Development setup
you can use envs listed below to setup a dev env easily.
- devcontainer
- gitpod
- docker

Or install module dependencies with 
1. pip
```sh
pip install -r requirements
```
2. [Poetry](https://python-poetry.org/)
```sh
poetry install
```

- Hints:
    - Create new migration need to follow the filename pattern (`<serial_number>.<date>.<description>.sql`)

## Meta

MikeYang – [@mikeyangyo](https://twitter.com/mikeyangyo) – perryvm06vm06@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/mikeyangyo/](https://github.com/mikeyangyo/)

## Contributing

1. Fork it (<https://github.com/mikeyangyo/tasks-management-system/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
4. Commit your changes (`git commit -am 'Add some fooBar'`)
5. Run test before pushing (`pytest`)
6. Push to the branch (`git push origin feature/fooBar`)
7. Create a new Pull Request
