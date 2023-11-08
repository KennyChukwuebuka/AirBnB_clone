#!/usr/bin/python3
"""Console Interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class command"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
