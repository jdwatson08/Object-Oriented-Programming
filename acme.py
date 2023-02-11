import random


'''This initializes the product class and creates
the attributes for the class.'''


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    '''Function determines how stealable a product is based off its weight'''

    def stealability(self):
        if (self.price / self.weight) < 0.5:
            return "Not so stealable."

        elif self.price / self.weight >= 0.5 and self.price / self.weight < 1:
            return "Kinda Stealable."

        else:
            return "Very Stealable"

    '''Function determines who flammable a product is'''
    def explode(self):
        flame = self.flammability
        heavy = self.weight
        if flame * heavy < 10:
            return "...fizzle."

        elif (flame * heavy) >= 10 and (flame * heavy) < 50:
            return "...boom!"

        else:
            return "...BABOOM!!!"


'''This initializes a child class of Product called BoxingGlove.
The default weight is changed from 2 to 10'''


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability,
                         identifier)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    '''Function overwrites the flammability for the Boxing Glove product.'''
    def explode(self):
        return "...its a glove."

    '''Function returns a statement about the effectiveness of the Boxing Glove
    based off its weight'''
    def punch(self):
        if self.weight < 5:
            return "That tickles."

        elif 5 <= self.weight < 15:
            return "Hey that hurt!"

        else:
            return "OUCH!"
