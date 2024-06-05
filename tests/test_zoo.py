import unittest 
from unittest import TestCase
from src.zoo import Zoo, Zookeeper, Animal, Fence



class TestZoo(TestCase):
#INIT
    def test_animal_dimension(self):
        
        zookeeper1 : Zookeeper = Zookeeper (name = "Mario", surname = "Rossi", id = "ZK001")  
        zookeeper2 : Zookeeper = Zookeeper (name ="Luigi", surname ="Verdi", id ="ZK002")
        
        recinto1 = Fence (area=100.0, temperature=25.0, habitat="foresta")
        recinto2 = Fence (area=150.0, temperature=20.0, habitat="deserto")
        recinto3 = Fence (area=150.0, temperature=20.0, habitat="deserto")
        
        animale1: Animal = Animal (name="Scimmia", species="Capuchin", age=5, height=0.5, width=0.5, preferred_habitat="foresta", health=100)
        animale2: Animal = Animal (name="Leone", species="Panthera leo", age=8, height=1.2, width=2.0, preferred_habitat="deserto", health=100)
        animale3: Animal = Animal (name="Paguro", species="Crostaceo", age=8, height=1.2, width=2.0, preferred_habitat="deserto", health=100)

        
        zookeeper1.add_animal (animale1, recinto1)
        zookeeper2.add_animal (animale2, recinto2)
        zookeeper2.add_animal (animale3, recinto3)
        
        result1: int = len(recinto1.animals)
        result2: int = len(recinto2.animals)
        result3: int = len(recinto3.animals)
        
        results: set[int ,int ,int] = {result1,result2,result3}
        result = len(results)
        message: str = f"Error: the function add_animal should not add self.animale1 into self.recinto1"
        
        self.assertEqual(result, 1, message)
        
if __name__ == "__main__":
    
    unittest.main()