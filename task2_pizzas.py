class Pizza:

    ingredients = ["Pizza dough"]

    def __init__(self):
        self.ingr_storage = []
        ingredfile = open('possible_ingredients.txt', "r")
        for line in ingredfile:
            self.ingr_storage.append(line.strip())
        ingredfile.close()

    def add_ingredient(self, ingr):
        if(self.isvalid(ingr) == False):
            return "invalid"
        if(self.is_already_added(ingr) == True):
            return "added"
        self.ingredients.append(ingr)
        return "added"

    def isvalid(self, ingr):
        for item in self.ingr_storage:
            if item == ingr:
                return True
        return False

    def is_already_added(self, ingr):
        for item in self.ingredients:
            if item == ingr:
                return True

class Monday_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Ketchup")
        self.add_ingredient("Pepperoni")
        self.add_ingredient("Cheese")
        self.add_ingredient("Olives")

class Tuesday_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Barbecue sauce")
        self.add_ingredient("Chicken")
        self.add_ingredient("Garlic")
        self.add_ingredient("Pickles")

class Wednesday_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Ketchup")
        self.add_ingredient("Bacon")
        self.add_ingredient("Onion")
        self.add_ingredient("Cheese")
        self.add_ingredient("Corn")

class Super_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Ketchup")
        self.add_ingredient("Ice cream")
        self.add_ingredient("Salmon")
        self.add_ingredient("Pickles")

class Vegetarian_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Ketchup")
        self.add_ingredient("Cheese")
        self.add_ingredient("Onion")
        self.add_ingredient("Spinach")
        self.add_ingredient("Broccoli")

class Meat_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Barbecue sauce")
        self.add_ingredient("Chicken")
        self.add_ingredient("Bacon")
        self.add_ingredient("Pepperoni")

class The_Louis_XIII_Pizza(Pizza):

    def __init__(self):
        Pizza.__init__(self)
        self.add_ingredient("Caviar")
        self.add_ingredient("Mantis shrimp")
        self.add_ingredient("Prawns")
        self.add_ingredient("Lobster")
        self.add_ingredient("Cheese")
