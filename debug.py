from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
a1 = Animal( 'Lion', 75, 'Luke', z1 )
z2 = Zoo("Batimore Zoo", "Druid Hill")
a2 = Animal('Dog', 35, 'Shosti', z1)
a3 = Animal('Dog', 30, 'Momo', z1 )
a4 = Animal('Dog', 5, 'Fenway', z2)

print(z1.animals)
print(Zoo.all)
print(z1.animal_species)
print(z1.find_by_species("Dog"))
print(z1.find_by_species("Lion"))
print(z1.find_by_species("Seal"))
print(z2.find_by_species("Dog"))
print(z1.animal_nicknames)
print(Zoo.find_by_location("Druid Hill"))
print(Animal.all)
print(Animal.find_by_species("Dog"))


# ipdb allows us to stop our code & test stuff
# import ipdb; ipdb.set_trace()
# print( 'Thanks for visiting the zoo!' )