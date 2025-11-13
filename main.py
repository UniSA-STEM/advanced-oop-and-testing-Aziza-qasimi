"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    # Create enclosures
    mammal_zone = Enclosure("Savannah Zone", "grassland", "mammal")
    bird_zone = Enclosure("Bird Paradise", "aviary", "bird")

    # Create animals
    lion = Mammal("Leo", "Lion", 5, ["meat"])
    penguin = Bird("Penny", "Penguin", 3, ["fish"])

    # Add animals to enclosures
    mammal_zone.add_animal(lion)
    bird_zone.add_animal(penguin)

    # Create staff
    keeper = Zookeeper("Alice", "Zookeeper")
    vet = Veterinarian("Dr. Bob", "Veterinarian")

    # Staff actions
    keeper.feed_animal(lion, "meat")
    keeper.clean_enclosure(mammal_zone)
    vet.health_check(penguin, "Wing check - all good")

    # Print reports
    print("\n=== Enclosure Reports ===")
    print(mammal_zone.status_report())
    print(bird_zone.status_report())

if __name__ == "__main__":
    main()