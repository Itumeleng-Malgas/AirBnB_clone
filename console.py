#!/usr/bin/python3
"""
This modules defines HBNBCommand class, it extends the built-in cmd
module and uses its cmdloop to create the interactive command prompt

"""

# User defined modules
from models.base_model import BaseModel
from models import storage

# Built-in modules
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class implementation, extends Cmd module """
    prompt = "(hbnb) "

    classes = BaseModel.__subclasses__()
    classes.append(BaseModel)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Take no action"""
        pass

    def do_print(self, arg):
        print(self.classes)

    def do_create(self, arg):
        """ Creates a new instance """
        if not arg:
            print("** class name missing **")
        else:
            try:
                if arg in [cls.__name__ for cls in self.classes]:
                    t = next(cls for cls in self.classes if cls.__name__ == arg)
                    new_instance = t()
                    new_instance.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")
            except StopIteration:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in [cls.__name__ for cls in self.classes]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in [cls.__name__ for cls in self.classes]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""

        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg not in [cls.__name__ for cls in self.classes]:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in storage.all().items()
                   if key.startswith(arg + '.')])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in [cls.__name__ for cls in self.classes]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[key]
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(obj, attribute_name, attribute_value)
                obj.save()


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
