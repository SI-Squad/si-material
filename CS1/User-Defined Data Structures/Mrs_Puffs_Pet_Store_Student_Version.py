"""
Mrs. Puff owns a pet store and has many pets inside of her store. Every once in awhile some of her pets get out,
so she's trying to keep good count of the animals she has over the displays in her store. She keeps pets in the window
(W), front of the store (F), back of the store (B), and on the shelves (S). Help Mrs. Puff take inventory of her store!

First, Mrs. Puff wants to treat the pets in different locations of the store separately. Write code that will create a
data structure for an individual species and then put each species into a list. Then, find and print the top 3
species, regardless of location.

Secondly, Mrs. Puff wants to treat the pets in different locations of the store together. Write code that will put each
species into a dictionary. Then, find and print the most popular species.

The solution version for Mrs_Puffs_Pet_Store
Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
from dataclasses import dataclass
from operator import attrgetter

# TODO: Make the dataclass that will best fit Mrs.Puff's needs for her Pet Store!


"""
Reads the file and puts species into the dataclass and a list (for number 1). For example, entries for Dogs located at 
the window shouldn't be included with entires for Dogs located at the back of the store.
"""
def readfile_separate(filename):
    with open(filename) as f:
        pets = []
        # TODO: Iterate through the file and put the information into the list!
        # Hint: Make sure you use the dataclass you created!
        return pets


"""
Finds the top 3 pets regardless of location in the store
"""
def top3(pets):
    pets = sorted(pets, key=attrgetter("count"), reverse=True)
    return pets[0], pets[1], pets[2]


"""
Reads the file and puts the elements in a dictionary (for number 2). The dictionary has the format where 
<K,V> = <Species, Total Count>
"""
def readfile_together(filename):
    with open(filename) as f:
        pets = {}
        # TODO: Iterate through the file and put the information in a dictionary
        # Hint: Make sure to check whether or not the species is already in the dictionary!
        return pets


"""
Finds the species that Mrs. Puff has the most of and returns the name of the species and how many there are
"""
def find_most_pet(dic):
    most_pet = 0
    pet_name = ""
    for pet in dic:
        if dic[pet] > most_pet:
            most_pet = dic[pet]
            pet_name = pet
    return most_pet, pet_name


def main():
    filename = "store_inventory.txt"
    pets_locations = readfile_separate(filename)
    pet1, pet2, pet3 = top3(pets_locations)
    print("The top 3 pets regardless of location are " + pet1.name + ", " + pet2.name + ", and " + pet3.name)
    pets_together = readfile_together(filename)
    species_num, species_name = find_most_pet(pets_together)
    print("The species that Mrs. Puff has the most of is " + species_name + " with " + str(species_num) + " animals")


main()