"""
File: animal.py
Description: Base class and subclasses for animals in the zoo with health tracking.
Author: Aziza Qasimi
ID: 110462000
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC, abstractmethod
from typing import List
from health_record import HealthRecord

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
        self._health_records: List[HealthRecord] = []

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

    # --- Health Record Methods ---
    def add_health_record(self, record: HealthRecord):
        """Attach a health record to this animal."""
        self._health_records.append(record)
        print(f"Health record added for {self._name}: {record.description}")

    def list_health_records(self):
        """Return all health records for reporting."""
        return [r.summary() for r in self._health_records]

    def active_health_issues(self):
        """Return only open/active health records."""
        return [r.summary() for r in self._health_records if r.is_open]

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
