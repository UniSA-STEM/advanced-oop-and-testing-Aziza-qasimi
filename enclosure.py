"""
File: enclosure.py
Description: Class for zoo enclosures.
Author: Aziza Qasimi
ID: 110462000
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Enclosure:
    """Represents an enclosure housing animals of one category."""

    def __init__(self, name: str, environment: str, allowed_type: str):
        self._name = name
        self._environment = environment
        self._allowed_type = allowed_type.lower()
        self._animals: list[Animal] = []
        self._cleanliness = 100  # 100 = perfectly clean

    def add_animal(self, animal: Animal):
        if animal.__class__.__name__.lower() != self._allowed_type:
            raise ValueError(f"This enclosure is for {self._allowed_type}s only!")
        self._animals.append(animal)
        print(f"{animal._name} has been added to {self._name} enclosure.")

    def clean(self):
        self._cleanliness = 100
        print(f"{self._name} is now clean!")

    def list_animals(self):
        return [a._name for a in self._animals]

    def status_report(self):
        return {
            "name": self._name,
            "environment": self._environment,
            "cleanliness": self._cleanliness,
            "animals": self.list_animals()
        }
