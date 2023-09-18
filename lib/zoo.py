class Zoo:
    all = []
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)
        self.animals = []
        self.animal_species = set(())
        self.animal_nicknames = []

    def find_by_species(self, target):
        return_list = []
        for animal in self.animals:
            # print(animal)
            # print(animal.species)
            if animal.species == target:
                return_list.append(animal)
        return return_list
    
    def add_animal(self, animal):
        self.animals.append(animal)
        self.animal_species.add(animal.species)
        self.animal_nicknames.append(animal.nickname)

    @classmethod
    def find_by_location(cls, target):
        return_list = []
        for zoo in Zoo.all:
            if zoo.location == target:
                return_list.append(zoo)
        return return_list

    def __repr__(self):
        return repr(f"{self.name} at {self.location}")