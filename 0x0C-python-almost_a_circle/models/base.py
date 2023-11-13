#!/usr/bin/python3
"""
This class will be the “base” of all other classes
in this project. The goal of it is to manage id attribute
in all your future classes and to avoid duplicating the
same code (by extension, same bugs).
"""
import json
import csv


class Base:
    """
    This class is used to manage id attribute of
    all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method is a class constructor that gets called
        for every instance.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Used to convert a python3 dictionary
        to a JSON string.
        """
        if (list_dictionaries is None):
            return ("{}".format([]))
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON string to file.
        """
        js = []
        if (list_objs is not None):
            for list_dict in list_objs:
                js.append(Base.to_json_string(list_dict.to_dictionary()))

        # creating the json file
        file_name = cls.__name__ + ".json"
        if (list_objs is not None):
            with open(file_name, mode="w", encoding="utf-8") as a_file:
                a_file.write("[")
                for i in range(len(js)):
                    a_file.write(js[i])
                    if ((i + 1) < len(js)):
                        a_file.write(", ")
                a_file.write("]")
        elif list_objs is None:
            with open(file_name, mode="w", encoding="utf-8") as a_file:
                a_file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        JSON string to dictionary.
        """
        if ((json_string is None) or (len(json_string) == 0)):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Dictionary to Instance.
        """
        # creating a dummy instance so i
        # can make use of the update function.
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        File to instances.
        """
        a_str = ""
        a_list = []
        cls_inst = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as a_file:
                a_str = a_file.read()
        except FileNotFoundError:
            return (a_list)

        dummy_class = cls(1, 2)
        for inst in cls.from_json_string(a_str):
            cls_inst.append(dummy_class.create(**inst))
        return (cls_inst)

    @staticmethod
    def to_csv_list(list_dictionary):
        """
        Used to add each class instance to a
        list.
        """
        csv_list = []
        if (list_dictionary is None):
            return (csv_list)
        # adding each class instance to a list
        for i in range(len(list_dictionary)):
            csv_list.append(list_dictionary[i])
        return (csv_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        List dictionary to  csv file.
        """
        csv_list = Base.to_csv_list(list_objs)
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, mode="w") as a_file:
                a_file = csv.writer(a_file, delimiter=",")
                for inst in csv_list:
                    row = [
                            getattr(inst, "id"),
                            getattr(inst, "width"),
                            getattr(inst, "height"),
                            getattr(inst, "x"),
                            getattr(inst, "y")
                          ]
                    a_file.writerow(row)
        except FileNotFoundError:
            return (csv_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        CSV file to instances.
        """
        file_name = cls.__name__ + ".csv"
        a_list = []
        cls_dict = {}
        cls_inst = []
        try:
            with open(file_name, mode="r") as a_file:
                a_file = csv.reader(a_file)
                for a_line in a_file:
                    a_list.append(a_line)
        except FileNotFoundError:
            return (a_list)
        # creating the instances from the
        # csv file
        dummy_class = cls(1, 2)
        for inst in a_list:
            cls_dict["id"] = int(inst[0])
            cls_dict["width"] = int(inst[1])
            cls_dict["height"] = int(inst[2])
            cls_dict["x"] = int(inst[3])
            cls_dict["y"] = int(inst[4])
            cls_inst.append(dummy_class.create(**cls_dict))
        return (cls_inst)

