# Builder Pattern

# client --> order(Something=HamBuilder) --> HamBuilder --> concreate implementation of Builder interface

from typing import Type
from abc import ABC, abstractmethod
# import abstract classes decorator

class Order:
    
    def __init__(self, builder: Type["Builder"]):
        self.builder = builder
    
    def serve_order(self) -> Type["Food"]:
        food = Food()

        ingredient = self.builder.build_ingredient()
        food.add_ingredient(ingredient)

        drink = self.builder.build_drink()
        food.add_drink(drink)

        side_dish = self.builder.build_side_dish()
        food.add_side_dish(side_dish)

        return food

class Food:
    def __init__(self):
        self.ingredient = []
        self.drink = None
        self.side_dish = []

    def add_ingredient(self, ingredient):
        self.ingredient.append(ingredient)

    def add_drink(self, drink):
        self.drink = drink
    
    def add_side_dish(self, side_dish):
        self.side_dish.append(side_dish)

    def __str__(self):
        return f"Your Order is this --> \nIngredients include: {self.ingredient}\nDrink is: {self.drink}\nSide Dish include: {self.side_dish}"

class Builder:
    @abstractmethod
    def build_ingredient(self): pass
    @abstractmethod
    def build_drink(self): pass
    @abstractmethod
    def build_side_dish(self): pass

class HamburgerBuilder(Builder):
    def build_ingredient(self):
        ingredient = Ingredient()
        ingredient.include.extend(['Meat', 'Sausages', 'Lettuce', 'Tomato'])
        return ingredient

    def build_drink(self):
        drink = Drink()
        drink.is_cup = True
        return drink

    def build_side_dish(self):
        side_dish = SideDish()
        side_dish.plate = "Blue"
        return side_dish

class Ingredient:
    def __init__(self):
        self.include = []

class Drink:
    def __init__(self):
        self.is_cup = False

class SideDish:
    def __init__(self):
        self.plate = None

def main():
    hamburger = HamburgerBuilder()
    order = Order(hamburger)
    ham = order.serve_order()
    print(ham)

if __name__ == "__main__":
    main()
