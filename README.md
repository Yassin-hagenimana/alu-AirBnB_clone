
## Project Description
HBnB is a comprehensive web application that combines database storage, a back-end API, and front-end interface to replicate the functionality of AirBnB. As the initial phase in developing a full web application, this step involves creating a custom command-line interface for managing data and establishing the foundational classes for data storage.


## Description of the command interpreter:
The application's interface resembles the Bash shell but is limited to specific commands designed for the AirBnB website. This command-line interpreter acts as the front end of the web application, allowing users to interact with the backend, which is built using Python's object-oriented programming (OOP).


List of some commands:
- show
- create
- update
- destroy
- count

As part of implementing the command-line interpreter alongside the backend and file storage system, several actions can be carried out. These include creating new objects, such as a User or Place, retrieving objects from files or databases, performing operations on objects like counting or computing statistics, updating the attributes of an object, and deleting an object.

## How to start it
These steps will help you set up and run the project on your local Linux machine for development and testing.

## Installing

You will need to clone the project's repository from GitHub, which includes the simple shell program and all its dependencies.

```
git clone https://github.com/Yassin-hagenimana/alu-AirBnB_clone.git
```
Once cloned, you'll have a folder named AirBnB_clone containing various files necessary for the program to function. Key files include:

/console.py: The main executable and command interpreter of the project.
models/engine/file_storage.py: A class responsible for serializing instances to a JSON file and deserializing JSON files back to instances.
models/__ init __.py: Initializes a unique FileStorage instance for the application.
models/base_model.py: A class defining common attributes and methods for other classes.
models/user.py: A User class inheriting from BaseModel.
models/state.py: A State class inheriting from BaseModel.
models/city.py: A City class inheriting from BaseModel.
models/amenity.py: An Amenity class inheriting from BaseModel.
models/place.py: A Place class inheriting from BaseModel.
models/review.py: A Review class inheriting from BaseModel.
Usage
The program can operate in two modes: Interactive and Non-interactive.

## In Interactive mode,
 The console will display a prompt (hbnb), allowing the user to input and execute commands. After executing a command, the prompt reappears, waiting for the next command, continuing indefinitely until the user exits the program.

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
## In Non-interactive mode,
 The shell runs a command piped into it during execution. The command runs immediately upon startup, and no prompt appears for further input.

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
 ## Command Input Format
In Non-interactive mode, commands are piped through an echo. In Interactive mode, commands are typed via the keyboard when the prompt appears and are executed when the Enter key is pressed. If the command fails, an error message will be displayed. The console can be exited using CTRL + D, CTRL + C, or the commands quit or EOF.

## Arguments
Most commands accept multiple options or arguments. To ensure the shell recognizes these parameters, users should separate them with spaces.

Example:

```

user@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
user@ubuntu:~/AirBnB$ ./console.py

```

or

```
user@ubuntu:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
e37ebcd3-f8e1-4c1f-8095-7a019070b1fa
(hbnb)
user@ubuntu:~/AirBnB$ ./console.py
```

## Available commands and what they do

The recognizable commands by the interpreter are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Authors :
* **Yassin Hagenimana** <[Yassin-hagenimana](https://github.com/Yassin-hagenimana)> <y.hageniman@alustudent.com>