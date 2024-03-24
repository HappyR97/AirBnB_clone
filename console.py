#!/usr/bin/python3

"""

This module defines the command interpreter

"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """commmand interpreter class"""
    prompt = '(hbnb) '

    class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Emply line entered in prompt"""
        pass

    def do_create(self, line):
        """Creates new instance"""
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
        """Show command Prints the string representation"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj = storage.all()
        key = f"{class_name}.{instance_id}"
        instance = obj.get(key, None)

        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy command Deletes an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj = storage.all()
        key = f"{class_name}.{instance_id}"
        if key not in obj:
            print("** no instance found **")
            return
        del obj[key]
        storage.save()

    def do_all(self, line):
        """all command Prints all string representation"""
        args = line.split()
        objs = storage.all()
        if len(args) < 1:
            for key, obj in objs.items():
                print(f"{str(obj)}")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
        else:
            for key, obj in objs.items():
                if type(obj).__name__ == args[0]:
                    print(str(obj))

    def do_count(self, class_name):
        """Count command counts all instances"""
        count = 0
        for key in storage.all().keys():
            if key.startswith(f"{class_name}."):
                count += 1
        print(count)

    def do_update(self, line):
        """Update command reloads an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        instance_id = args[1].strip('"')
        attr_name = args[2].strip("'\"")
        attr_value = args[3].strip("'\"")
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            attr_value = attr_type(attr_value)

        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, line):
        """Default behavior if command not found in do_..."""
        if '.' in line:
            args = line.split('.')
            class_name = args[0]
            command = args[1]

            if class_name in self.class_dict:
                if 'destroy' in command:
                    instance_id = command.split(
                            '(')[1].split(')')[0].replace('"', '')
                    if not instance_id:
                        print("** instance id missing **")
                    else:
                        self.do_destroy(f"{class_name} {instance_id}")
                elif 'show' in command:
                    instance_id = command.split(
                            '(')[1].split(')')[0].replace('"', '')
                    if not instance_id:
                        print("** instance id missing **")
                    else:
                        self.do_show(f"{class_name} {instance_id}")
                elif command.endswith('()'):
                    action = command[:-2]
                    if action == "all":
                        self.do_all(class_name)
                    elif action == "count":
                        self.do_count(class_name)
                    elif action == "destroy":
                        self.destroy(class_name)
                    else:
                        print(f"** Unknown method: {command} **")
                elif 'update' in command:
                    update_args = command.split('(')[1].split(')')[0] \
                            .split(', ')
                    if len(update_args) < 3:
                        print("** Incorrect number of arguments for update **")
                        return

                    instance_id = update_args[0].strip('"')
                    attr_name = update_args[1].strip().replace('"', '')
                    attr_value = update_args[2].strip().replace('"', '')
                    update_line = f"{class_name} {instance_id} \
                            {attr_name} {attr_value}"
                    self.do_update(update_line)
                else:
                    print(f"** Unknown command: {command} **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
