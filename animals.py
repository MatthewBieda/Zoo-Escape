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
        self.value = "chicken"

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

#Object instatiations
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

#Created array of all objects
animals_array = [antelope, bigfish, bug, bear, chicken, cow, fox, giraffe, lion, panda, sheep]
test1 = "fox,bug,chicken,grass,sheep" 

def find_remaining_animals(testcase):
    '''
    This function takes in the testcase, and returns an output array containing the input, all the
    steps of eating, and the remaining animals when eating is no longer possible
    '''
    testcase = test1.split(",")
    #Setting a boolean flag to detect when the array has been mutated, then resetting the loop
    list_mutated = True
    output_array = [test1]
    
    #For every animal in the testcase, find its corresponding index in the object array and 
    #run its object method to obtain the animals it can eat. Then check if those animals are to the
    #left or right of it in the input array, whilst respecting array bounds. If so mutate the list,
    #update the flag and break the loop for another iteration.
    while list_mutated and len(testcase) > 1:
        for index, item in enumerate(testcase):
            if item in str(animals_array):
                location = animals_array.index(eval(item))
                animals_eaten = animals_array[location].eat()

                #Check for leftmost bound of array
                if index == 0:
                    if testcase[index+1] in animals_eaten:
                        output_array.append(f"{item} eats {testcase[index+1]}")
                        testcase.pop(index+1)
                        list_mutated = True
                        break
            
                #Check for rightmost bound of array
                elif index == len(testcase)-1:
                    if testcase[index-1] in animals_eaten:
                        output_array.append(f"{item} eats {testcase[index-1]}")
                        testcase.pop(index-1)
                        list_mutated = True
                        break

                else:
                    if testcase[index-1] in animals_eaten:
                        output_array.append(f"{item} eats {testcase[index-1]}")
                        testcase.pop(index-1)
                        list_mutated = True
                        break

                    elif testcase[index+1] in animals_eaten:
                        output_array.append(f"{item} eats {testcase[index+1]}")
                        testcase.pop(index+1)
                        list_mutated = True
                        break
        
                list_mutated = False

            else:
                print(f"{item} doesn't eat anything")

    #Append remaning animals onto end of the output array
    output_array += testcase
    return output_array

print(find_remaining_animals(test1))