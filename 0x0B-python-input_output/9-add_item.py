#!/usr/bin/python3
""" The 9-add_item module """

from os import path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if path.isfile("add_item.json"):
    lista = load_from_json_file("add_item.json")
else:
    lista = []
for idx in range(1, len(argv)):
    lista.append(argv[idx])
save_to_json_file(lista, "add_item.json")
