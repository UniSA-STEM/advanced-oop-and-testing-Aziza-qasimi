"""
File: main.py
Description: Demonstration of the zoo system.
Author: Aziza Qasimi
ID: 110462000
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Mammal, Bird
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord

def main():
    # --- Create Enclosures ---
    mammal_zone = Enclosure("Savannah Zone", "grassland", "mammal")
    bird_zone = Enclosure("Bird Paradise", "aviary", "bird")

    # --- Create Animals ---
    lion = Mammal("Leo", "Lion", 5, ["meat"])
    penguin = Bird("Penny", "Penguin", 3, ["fish"])

    mammal_zone.add_animal(lion)
    bird_zone.add_animal(penguin)

    # --- Staff ---
    keeper = Zookeeper("Alice", "Zookeeper")
    vet = Veterinarian("Dr. Bob", "Veterinarian")

    # --- Health Records ---
    wing_injury = HealthRecord("Broken wing", 4)
    penguin.add_health_record(wing_injury)
    vet.health_check(penguin, "Applied splint")
    wing_injury.add_treatment("Applied bandage")
    wing_injury.close_record()

    # --- Feeding & Cleaning ---
    keeper.feed_animal(lion, "meat")
    keeper.clean_enclosure(mammal_zone)

    # --- Reports ---
    print("\n=== Enclosure Reports ===")
    print(mammal_zone.status_report())
    print(bird_zone.status_report())

    print("\n=== Penguin Health Records ===")
    for record in penguin.list_health_records():
        print(record)

if __name__ == "__main__":
    main()
