#!/usr/bin/python3
"""
6-load_from_json_file module

This module contains the load_from_json_file() function

"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
