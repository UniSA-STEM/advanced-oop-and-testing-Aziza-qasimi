"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    """Base class for all animals."""

    def __init__(self, name: str, species: str, age: int, diet: List[str]):
        if not name:
            raise ValueError("Animal name cannot be empty.")
        if age < 0:
            raise ValueError("Age must be non-negative.")
        if not isinstance(diet, list):
            raise ValueError("Diet must be a list of food strings.")
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._health_records = []

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self, food: str):
        if food in self._diet:
            print(f"{self._name} is happily eating {food}.")
        else:
            print(f"{self._name} refuses to eat {food}.")

    def sleep(self):
        print(f"{self._name} is sleeping peacefully.")

    def add_health_record(self, record):
        self._health_records.append(record)
        print(f"Added health record for {self._name}.")

# Subclasses
class Mammal(Animal):
    def make_sound(self):
        print(f"{self._name} the {self._species} roars or growls!")

class Bird(Animal):
    def make_sound(self):
        print(f"{self._name} the {self._species} chirps or squawks!")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self._name} the {self._species} hisses!")