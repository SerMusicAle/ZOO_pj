class Animal:
    
    #INIT
    def __init__(self, name:str, species:str, age:int, height, width, preferred_habitat:str, health):
        
        #DEC
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1/age), 3)

        #BODY
        self.volume = self.height*self.width

class Fence:

    #INIT
    def __init__(self, area:float, temperature: float, habitat:str):
        
        self.area = area
        self. temperature = temperature
        self.habitat = habitat
        self.area_cleaned = area
        self.animals:list= []


class Zookeeper:
    
    #INIT
    def __init__(self, name:str, surname:str, id:str):
        self.name = name
        self.surname = surname
        self.id = id

    #BODY
    def add_animal(self, animal: Animal, fence:Fence):
        if fence.area_cleaned >= animal.volume and animal.preferred_habitat == fence.habitat:
            fence.animals.append(animal)
            fence.area_cleaned -= animal.volume

    def remove_animal(self, animal:Animal, fence:Fence):
        if self.has_animal(animal, fence):
            fence.animals.remove(animal)
            fence.area_cleaned += animal.volume

    def has_animal(self, animal:Animal, fence:Fence):
        return animal in fence.animals

    def clean(self, fence:Fence):
        
        #BODY
        if fence.area_cleaned == 0:
            return fence.area
        else:
            time_clean:float = (fence.area-fence.area_cleaned) /fence.area_cleaned
            return time_clean

    def feed(self, animal:Animal):

        #security backup dimension
        volume = animal.height * animal.width

        depvolume = volume
        volume *= 1.02

        for fence in Zoo.fences:

            for animal in fence.animals:
                if (fence.area_cleaned + depvolume)>= volume:
                    fence.area_cleaned -= volume
                    animal.health*=1.01
                else:
                    animal.volume = depvolume 


class Zoo:

    #INIT
    def __init__(self, fences=None, zoo_keepers=None ):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        zookeepers_info = "\n".join(f"{keeper.name} {keeper.surname}" for keeper in self.zoo_keepers)
        fences_info = "\n\n".join(f"Dimensione recinto: {fence.area}, Habitat: {fence.habitat}, con gli animali: {','.join(animal.name for animal in fence.animals)}" for fence in self.fences)

        description = f"lo Zoo è composto da: \n\n i seguenti guardiani: \n{zookeepers_info} \n\n che controllano i seguenti recinti: \n {fences_info}"

        print (description)
