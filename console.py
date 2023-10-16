#!/usr/bin/python3
"""Console file"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Main class"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
