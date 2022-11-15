# In python doesn't support interfaces, however Abstrct Base Classes are feature
# from the abc module that lets is declare what method should implement. Python supports this module
# since version 2.7 
from abc import ABC, abstractmethod

class Polygon(ABC):
    #abstract method
    def noofsides(self):
        pass

class Triangle(Polygon):
    #overriding abstract method 
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    #overriding abstract method
    def noofsides(self):
        print("I have 5 sides")