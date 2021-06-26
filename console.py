#!/usr/bin/python3
'''  This module contains the entry point of the command interpreter: '''
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    '''  '''
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User']


    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        sys.exit(0)

    def emptyline(self, arg):
        pass

    def do_EOF(self, arg):
        '''Quit command to exit the program
        '''
        sys.exit(0)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] in self.classes:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.(
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = '{}.{}'.format(args[0], args[1])
        objects = storage.all()
        if key in objects.keys():
            print(objects[key])
        else:
            print("** no instance found **")
            return       


    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id (save the change into the JSON file)'''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        key = '{}.{}'.format(args[0], args[1])
        objects = storage.all()
        if key in objects.keys():
            #1. actualizar __objects
            objects.pop(key)
            #3. serializar y guardar objects
            storage.save()
        else:
            print("** no instance found **")
            return 
    
    def do_all(self, arg):
        '''Prints all string representation of all instances based or not on the class name. '''
        args = arg.split()
        list_of_strings = []
        objects = storage.all()
        for key in objects.keys():
            value = objects.get(key)
            if args: # si nos pidieron objetos de una clase determinada
                if args[0] in self.classes: # si creamos ese tipo de objetos
                    if value.__class__.__name__ == args[0]: # si la clase del objeto coincide con la que nos piden
                        list_of_strings.append(value.__str__())
                else:
                    print("** class doesn't exist **")
                    return
            else:
                list_of_strings.append(objects[key].__str__())
        print(list_of_strings)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or 
        updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            object_name = '{}.{}'.format(args[0], args[1])
            dict_of_objects = storage.all()
            if object_name in dict_of_objects.keys():
                object = dict_of_objects.get(object_name)
                object.__setattr__(args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()