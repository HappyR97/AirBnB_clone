#!/usr/bin/python3

"""

This module defines the command interpreter

"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """commmand interpreter class"""
    prompt = '(hbnb) '

    class_dict = {'BaseModel': BaseModel}

    def do_EOF(self, line):
        """End of file command to exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit"""
        return True

    def emptyline(self):
        """Emply line entered in prompt"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        Class = self.class_dict[class_name]
        instance = Class()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Prints str representation of instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0:2]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj = storage.all()
        key = f"{class_name}.{instance_id}"
        instance = obj.get(key, None)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0:2]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in obj:
            print("** no instance found **")
            return
        del obj[key]
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
