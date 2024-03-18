#!/usr/bin/python3

"""

This module defines the command interpreter

"""

import cmd


class HBNBCommand(cmd.Cmd):
    """commmand interpreter class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of file command to exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit"""
        return True

    def emptyline(self):
        """Emply line entered in prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
