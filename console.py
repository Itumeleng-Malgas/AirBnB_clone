#!/usr/bin/python3
"""
This modules defines HBNBCommand class, it extends the built-in cmd
module and uses its cmdloop to create the interactive command prompt

"""

# User defined modules
import models

# Built-in modules
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class implementation, extends Cmd module """
    prompt = "> "

    def do_quit(self, args):
        """Exit the application."""
        return True

    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Take no action"""
        pass


# Inintialize HBNBCommanf class
console = HBNBCommand()

if __name__ == "__main__":
    if not sys.stdin.isatty():

        # Read commands from stdin (pipe)
        for line in sys.stdin:
            console.onecmd(line.strip())

    else:
        # Start the interactive cmdloop
        console.cmdloop()
