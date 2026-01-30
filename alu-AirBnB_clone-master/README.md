# AirBnB Clone - The Console

## Description of the Project

This project is a simplified clone of the AirBnB web application. The goal is to understand how a full web application is built, starting from a command-line interpreter and progressively adding components such as storage, web static content, databases, APIs, and a full web framework.

This first stage focuses on building a command interpreter that manages AirBnB objects.

## Description of the Command Interpreter

The command interpreter is a command-line interface (CLI) used to manage the objects of the AirBnB project. It allows users to create, update, destroy, and retrieve objects such as users, places, cities, states, amenities, and reviews.

## How to Start It

The command interpreter is started by running the console.py file:

```bash
$ ./console.py
```

Or using Python:

```bash
$ python3 console.py
```

## How to Use It

Once started, you'll see the prompt `(hbnb)`. The interpreter supports the following commands:

- `create <class>` - Creates a new instance of a class and prints its ID
- `show <class> <id>` - Shows the string representation of an instance
- `all [<class>]` - Shows all instances or all instances of a specific class
- `destroy <class> <id>` - Deletes an instance
- `update <class> <id> <attribute> "<value>"` - Updates an instance attribute
- `count <class>` - Counts the number of instances of a class
- `quit` or `EOF` - Exits the interpreter

## Examples

```bash
(hbnb) create BaseModel
49faff00-8d10-4817-a6c3-1c8d8c8d8c8d
(hbnb) show BaseModel 49faff00-8d10-4817-a6c3-1c8d8c8d8c8d
[BaseModel] (49faff00-8d10-4817-a6c3-1c8d8c8d8c8d) {'id': '49faff00-8d10-4817-a6c3-1c8d8c8d8c8d', 'created_at': datetime.datetime(2026, 1, 11, 7, 0, 0), 'updated_at': datetime.datetime(2026, 1, 11, 7, 0, 0)}
(hbnb) all BaseModel
[[BaseModel] (49faff00-8d10-4817-a6c3-1c8d8c8d8c8d) {...}]
(hbnb) update BaseModel 49faff00-8d10-4817-a6c3-1c8d8c8d8c8d name "My first model"
(hbnb) show BaseModel 49faff00-8d10-4817-a6c3-1c8d8c8d8c8d
[BaseModel] (49faff00-8d10-4817-a6c3-1c8d8c8d8c8d) {'id': '49faff00-8d10-4817-a6c3-1c8d8c8d8c8d', 'name': 'My first model', ...}
(hbnb) destroy BaseModel 49faff00-8d10-4817-a6c3-1c8d8c8d8c8d
(hbnb) show BaseModel 49faff00-8d10-4817-a6c3-1c8d8c8d8c8d
** no instance found **
(hbnb) quit
```

