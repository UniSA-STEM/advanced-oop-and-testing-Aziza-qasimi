"""
File: test_zoo.py
Description: Unit tests for the Zoo Management System.
Author: Aziza Qasimi
ID: 110462000
This is my own work as defined by the University's Academic Integrity Policy.
"""

import unittest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord

class TestZooSystem(unittest.TestCase):

    def setUp(self):
        # Animals
        self.lion = Mammal("Leo", "Lion", 5, ["meat"])
        self.penguin = Bird("Penny", "Penguin", 3, ["fish"])
        self.snake = Reptile("Sly", "Snake", 2, ["mice"])

        # Enclosures
        self.mammal_zone = Enclosure("Savannah Zone", "grassland", "mammal")
        self.bird_zone = Enclosure("Bird Paradise", "aviary", "bird")

        # Staff
        self.keeper = Zookeeper("Alice", "Zookeeper")
        self.vet = Veterinarian("Dr. Bob", "Veterinarian")

    def test_add_animal_to_enclosure(self):
        self.mammal_zone.add_animal(self.lion)
        self.assertIn(self.lion._name, self.mammal_zone.list_animals())
        with self.assertRaises(ValueError):
            self.mammal_zone.add_animal(self.penguin)  # Wrong type

    def test_feeding_animal(self):
        self.keeper.feed_animal(self.lion, "meat")
        self.keeper.feed_animal(self.lion, "vegetables")  # Should refuse

    def test_clean_enclosure(self):
        self.mammal_zone._cleanliness = 50
        self.keeper.clean_enclosure(self.mammal_zone)
        self.assertEqual(self.mammal_zone._cleanliness, 100)

    def test_health_record_addition(self):
        injury = HealthRecord("Broken wing", 4)
        self.penguin.add_health_record(injury)
        self.assertEqual(len(self.penguin.list_health_records()), 1)
        self.assertTrue(len(self.penguin.active_health_issues()) > 0)

        injury.add_treatment("Applied bandage")
        injury.close_record()
        # After closing, there should be no active health issues
        self.assertEqual(len(self.penguin.active_health_issues()), 0)

    def test_animal_actions(self):
        self.lion.eat("meat")
        self.lion.eat("grass")  # Should refuse
        self.lion.sleep()
        self.lion.make_sound()

        self.penguin.eat("fish")
        self.penguin.make_sound()

        self.snake.make_sound()
        self.snake.sleep()

if __name__ == "__main__":
    unittest.main()
