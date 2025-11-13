"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from enclosure import Enclosure

class Staff:
    def __init__(self, name: str, role: str):
        self._name = name
        self._role = role

    def __str__(self):
        return f"{self._role}: {self._name}"

class Zookeeper(Staff):
    def feed_animal(self, animal: Animal, food: str):
        print(f"{self._name} is feeding {animal._name}.")
        animal.eat(food)

    def clean_enclosure(self, enclosure: Enclosure):
        print(f"{self._name} is cleaning {enclosure._name}.")
        enclosure.clean()

class Veterinarian(Staff):
    def health_check(self, animal: Animal, issue: str):
        print(f"{self._name} performs a health check on {animal._name}: {issue}.")