# AirBnB Clone - The Console

## Description of the Project

This project is a streamlined clone of the AirBnB web application. The objective is to learn how a complete web application is constructed, beginning with a command-line interpreter and gradually incorporating components like storage, web static content, databases, APIs, and a comprehensive web framework.

This initial phase focuses on developing a command interpreter to manage AirBnB objects.

## Description of the Command Interpreter

The command interpreter is a command-line interface (CLI) designed to manage the objects of the AirBnB project. It enables users to create, update, destroy, and retrieve objects including users, places, cities, states, amenities, and reviews.

## How to Start It

The command interpreter is launched by executing the console.py file:

```bash
$ ./console.py
```

Or using Python:

```bash
$ python3 console.py
```

## How to Use It

After launching, you'll see the prompt `(hbnb)`. The interpreter supports these commands:

- `create <class_name>` - Creates a new instance of a class and prints its ID
- `show <class_name> <id>` - Shows the string representation of an instance
- `all [class_name]` - Shows all instances or all instances of a specific class
- `destroy <class_name> <id>` - Deletes an instance
- `update <class_name> <id> <attribute_name> "<attribute_value>"` - Updates an instance attribute
- `count <class_name>` - Counts the number of instances of a class
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
