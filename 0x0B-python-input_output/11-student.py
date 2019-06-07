#!/usr/bin/python3
""" The 11-student method
"""


class Student:
    """ A Student class"""
    def __init__(self, first_name, last_name, age):
        """ class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionarry representation of a Student instance"""
        return self.__dict__
