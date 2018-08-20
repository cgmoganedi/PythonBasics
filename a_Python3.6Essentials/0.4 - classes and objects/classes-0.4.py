class animal :
    kindom = "mammal"
class dog(animal) :
    breed = "GSD"
    
class bird(animal):
    kindom = "bird"
class eagle(bird, animal) :
    species = "eagle"
