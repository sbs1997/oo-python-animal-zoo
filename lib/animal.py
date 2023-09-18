class Animal:
    all = []
    def __init__(self, species, weight, nickname, zoo):
        self.nickname = nickname
        self.weight = weight
        self.species = species
        self.zoo = zoo
        Animal.all.append(self)
        zoo.add_animal(self)

    @classmethod
    def find_by_species(cls, target):
        return_list = []
        for animal in Animal.all:
            if animal.species == target:
                return_list.append(animal)
        return return_list

    def __repr__(self):
        return repr(f"{self.nickname} the {self.species}")