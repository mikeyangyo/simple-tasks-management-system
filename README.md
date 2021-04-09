# tasks-management-system
a tasks management system build with python Flask, mysql, docker

## APIs
### List tasks
List tasks in db

### Retrieve task
Retrieve task with given id

### Create task
Create a task with given name

### Update task
Update a task with given name or status
- if resource not found, will return 404

### Delete task
Delete a task
- if resource not found, will return 404

## Commands
### run-migrations
used for run all migration files
- migration filename pattern: `<serial_number>.<date>.<description>.sql`

## Test
just run `pytest`
or run `pytest --cov=. --cov-report term-missing` to generate coverage report

## Development
you can use envs listed below
- devcontainer
- gitpod
- docker
