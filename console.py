#!/usr/bin/python3
"""HBNBCommand module for the command interpreter."""


import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print(" ")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel, saves it 
        to JSON file, prints ID"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of instance based on
        name and class id. """
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        try:
            class_obj = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        key = args[0] + "." + args[1]
        key = f"{class_name}.{instance_id}"
        all_objects = storage.all()

        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")
 
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        if arg:
            try:
                eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        obj_list = []
        for obj_id in storage.all():
            obj = storage.all()[obj_id]
            if not arg or arg == obj.__class__.__name__:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
