zoo = ("Melba", "Cormac", "Bear", "Shadowfax", "Joe Exotic's Favorite Tiger", "Unicorn", "Narwhal", "Elephant", "Telephant", "I dunno")

# print(zoo.index("Joe Exotic's Favorite Tiger"))

# animal_to_find = "Cormac"
# if animal_to_find in zoo:
#     print(f'{animal_to_find} is in zoo')
# else:
#     print('Animal is not in zoo')

(first_animal, second_animal, thrid_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

# for animal in zoo:
#     print(animal)

zoo_list = list(zoo)

zoo_list.extend(["Another Animal", "And Another Animal", "Yet Another Animal"])

zoo_tuple = tuple(zoo_list)