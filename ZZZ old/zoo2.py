"""
    ENTRO LE 23.59 del 16 05 2024
    
    ZOO
    
    RECINTI
    OK area float, 
    OK temperatura float
    OK habitat stringa
    lista di animali che puo contenere
    -- describe_zoo come __str__ 
    OK    stampa tutti gli zookeeper, 
    OK    stampa caratteristiche di ogni recinto, con animali
    OK habitat è una stringa

    ANIMALE
    OK animale ha caratteristiche, habitat preferito, stato salute
       finire alla terza cifra per la salute
        
    GUARDIANI
    OK nome, surname, id, 
    OK ID è una stringa
    OK nutrire:
        salute incrementa di 1% ad ogni nutrimento
        dimensioni dell'animale incrementano del 2% ad ogni nutrimento. 
        verifica se lo spazio è sufficiente a farlo mangiara 
    OK pulire
        torna un float come tempo necessario a pulire
        l'area occupata / area rimasta
    OK remove_animal. se sta nel recinto. si ripristina l'area rimasta
    OK add_animal inserisce un animale nel recinto che rispetta l'habitat e le necessità come le dimensioni
    OKlo spazio deve esser sufficiente

    CONSEGNA
    file zip (nome e cognome), contenente il file zoo.py
    compilare come con code runner, senza dati in input
    describe zoo è l'unico print. gli altri sono tutti controlli
"""

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


# create objects
zookeeper1 = Zookeeper(name="Mario", surname="Rossi", id="ZK001")
zookeeper2 = Zookeeper(name="Luigi", surname="Verdi", id="ZK002")

recinto1 = Fence(area=100.0, temperature=25.0, habitat="foresta")
recinto2 = Fence(area=150.0, temperature=20.0, habitat="deserto")
recinto3 = Fence(area=150.0, temperature=20.0, habitat="deserto")

animale1 = Animal(name="Scimmia", species="Capuchin", age=5, height=0.5, width=0.5, preferred_habitat="foresta", health=100)
animale2 = Animal(name="Leone", species="Panthera leo", age=8, height=1.2, width=2.0, preferred_habitat="deserto", health=100)
animale3 = Animal(name="Paguro", species="Crostaceo", age=8, height=1.2, width=2.0, preferred_habitat="deserto", health=100)

zoo = Zoo(fences=[recinto1, recinto2, recinto3], zoo_keepers=[zookeeper1, zookeeper2])

# add animal to fence
zookeeper1.add_animal(animale1, recinto1)
zookeeper2.add_animal(animale2, recinto2)
zookeeper2.add_animal(animale3, recinto3)

# remove animal from fence
zookeeper1.remove_animal(animale1, recinto1)
zookeeper2.remove_animal(animale2, recinto2)

# clean fence
tempo_pulizia_recinto1 = zookeeper1.clean(recinto1)
tempo_pulizia_recinto2 = zookeeper2.clean(recinto2)
print(f"Tempo necessario per pulire il recinto 1: {tempo_pulizia_recinto1} unità di tempo")
print(f"Tempo necessario per pulire il recinto 2: {tempo_pulizia_recinto2} unità di tempo")

# describe zoo
zoo.describe_zoo()