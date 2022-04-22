from abc import ABC, abstractmethod

#input: "fox,bug,chicken,grass,sheep" 
#output: ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", 
#"sheep eats grass", "fox eats sheep", "fox"] 

#Class definitions
class AnimalClass(ABC):
    #Constructor
    def __init__(self):
        self.value = "Animal"

    #Methods
    @abstractmethod
    def eat(self):
        pass

class antelopeClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "antelope"

    #Methods
    def eat(self):
        return(f"{self.value} eats grass")

class bigfishClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "bigfish"

    #Methods
    def eat(self):
        return(f"{self.value} eats little-fish")

class bugClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "bug"

    #Methods
    def eat(self):
        return(f"{self.value} eats leaves")

class bearClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "bear"

    #Methods
    def eat(self):
        return(f"{self.value} eats big-fish, bug, chicken, cow, leaves, sheep")

class chickenClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "bug"

    #Methods
    def eat(self):
        return(f"{self.value} eats bug")

class cowClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "bear"

    #Methods
    def eat(self):
        return(f"{self.value} eats grass")

class foxClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "fox"

    #Methods
    def eat(self):
        return(f"{self.value} eats chicken, sheep")

class giraffeClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "giraffe"

    #Methods
    def eat(self):
        return(f"{self.value} eats leaves")

class lionClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "lion"

    #Methods
    def eat(self):
        return(f"{self.value} eats antelope, cow")

class pandaClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "panda"

    #Methods
    def eat(self):
        return(f"{self.value} eats leaves")

class sheepClass(AnimalClass):
    #Constructor
    def __init__(self):
        self.value = "sheep"

    #Methods
    def eat(self):
        return(f"{self.value} eats grass")

antelope = antelopeClass()
bigfish = bigfishClass()
bug = bugClass()
bear = bearClass()
chicken = chickenClass()
cow = cowClass()
fox = foxClass()
giraffe = giraffeClass()
lion = lionClass()
panda = pandaClass()
sheep = sheepClass()

#Can animal[0] eat animal[1]?
#Determine what animal[0] can eat
#If is not in animal[1], not possible
#If possible, remove animal[1]

animals_array = [antelope, bigfish, bug, bear, chicken, cow, fox, giraffe, lion, panda, sheep]
test1 = "fox,bug,chicken,sheep" 
split_testcase = test1.split(",")
strip_quotes = [x for x in split_testcase]


for index, item in enumerate(split_testcase):
    if item in str(animals_array):
        print(item)
        print(animals_array.index(item))
        animals_eaten = animals_array[6].eat()
        print(animals_eaten)

        #Check for leftmost bound of array
        if index == 0:
            if split_testcase[index+1]in animals_eaten:
                print(f"{split_testcase[index+1]} gets eaten by {item}")
            
        #Check for rightmost bound of array
        elif index == len(split_testcase)-1:
            if split_testcase[index-1]in animals_eaten:
                print(f"{split_testcase[index-1]} gets eaten by {item}")

        else:
            if split_testcase[index-1] in animals_eaten:
                print(f"{split_testcase[index-1]} gets eaten by {item}")
            elif split_testcase[index+1]in animals_eaten:
                print(f"{split_testcase[index+1]} gets eaten by {item}")

    else:
        print(f"{item} doesn't eat anything")
