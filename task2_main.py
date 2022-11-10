import task2_pizzas
from datetime import date

class Customer_service:

    def __init__(self, pizzamenu):
        todays_date = date.today()
        todays_weekday = todays_date.weekday() + 1
        self.pizzaname = pizzamenu[todays_weekday]
        self.pizza = getattr(task2_pizzas, self.pizzaname)()
        self.display_and_serve()

    def display_and_serve(self):
        print("\nWelcome to our pizza place! Today's pizza of the day is", self.pizzaname)
        print(self.pizzaname, "consists of", self.pizza.ingredients, "\n")
        answer = input("Press 1 if you want to add some ingredients to your pizza (press anything else if you dont): ")
        if (answer == "1"):
            print("\nThese are the available ingredients:\n***")
            for item in self.pizza.ingr_storage:
                print(item)
            print("***\nAll available ingredients are listed above")
            print("Please enter desired ingredients one by one (enter [Nothing] if you want to stop)")
            while True:
                newingr = input("Add an ingredient: ")
                if (newingr == "Nothing"):
                    break
                if(self.pizza.add_ingredient(newingr) == "added"):
                    print("Okay, we will make sure your pizza has", newingr)
                elif(self.pizza.add_ingredient(newingr) == "invalid"):
                    print("Sorry, we do not have", newingr)
        print("Okay, enjoy your pizza made of", self.pizza.ingredients)


if __name__ == '__main__':
    pizzamenu = {}
    menufile = open('pizzamenu.txt', "r")
    for line in menufile:
        day, name = line.split('-')
        pizzamenu[int(day)] = name.strip()
    menufile.close()
    today = Customer_service(pizzamenu)
