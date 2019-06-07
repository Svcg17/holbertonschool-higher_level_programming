#!/usr/bin/python3
""" The 13-student module
"""


class Student:
    """ A Student class"""
    def __init__(self, first_name, last_name, age):
        """ class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionarry representation of a Student instance"""
        newd = {}
        if attrs is None:
            return self.__dict__
        else:
            for item in self.__dict__:
                if item in attrs:
                    newd[item] = self.__dict__[item]
            return newd

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for elem in self.__dict__:
            if elem in json:
                self.__dict__[elem] = json[elem]
