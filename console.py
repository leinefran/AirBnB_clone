#!/usr/bin/python3
"""Method Command Interpreter"""

import inspect
import cmd
import sys
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_dict = {"BaseModel": BaseModel}

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
        else:
            for key, value in HBNBCommand.class_dict.items():
                if args == key:
                    new_creation = value()
                    models.storage.save()
                    print(new_creation.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of a specific instance
        Usage: show <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                print(models.storage.all()[key_value])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance
        Usage: destroy <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                del models.storage.all()[key_value]
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: destroy <class name> <id>
        """
        print(models.storage.all())

    def do_update(self, args):
        """Update an instance.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

    def do_quit(self, args):
        """Quits the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file condition
        """
        return True

    def do_help(self, args):
        """Get help on commands
        'help' or '?' with no arguments prints a list of commands for which
        help is available
        'help <command>' or '? <command>' gives help on <command>
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """Doesn't execute anything when user enter an empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
