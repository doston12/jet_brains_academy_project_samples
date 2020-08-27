
class CoffeeMachine:

    def __init__(self):
        self.available_water = 400
        self.available_milk = 540
        self.available_coffee_beans = 120
        self.available_disposable_cups = 9
        self.available_cash = 550

    def fill_coffee(self):
        print()
        water_to_add = int(input("Write how many ml of water do you want to add: "))
        self.available_water += water_to_add
        milk_to_add = int(input("Write how many ml of milk do you want to add: "))
        self.available_milk += milk_to_add
        coffee_beans_to_add = int(input("Write how many grams of coffee beans do you want to add: "))
        self.available_coffee_beans += coffee_beans_to_add
        cups_to_add = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.available_disposable_cups += cups_to_add
        print()

    def show_remaining(self):
        print("remaining")
        print()
        print('The coffee machine has: ')
        print(self.available_water, "of water")
        print(self.available_milk, "of milk")
        print(self.available_coffee_beans, "of coffee beans")
        print(self.available_disposable_cups, "of disposable cups")
        print(self.available_cash, "of money")
        print()

    def buy_coffee(self):
        print()
        x = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if x == "1":
            if self.available_water >= 250 and self.available_coffee_beans >= 16 and self.available_disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.available_cash += 4
                self.available_water -= 250
                self.available_coffee_beans -= 16
                self.available_disposable_cups -= 1
            else:
                if self.available_water < 250:
                    print("Sorry, not enough water!")
                elif self.available_coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                elif self.available_disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
        elif x == "2":
            if self.available_water >= 350 and self.available_milk >= 75 \
                    and self.available_coffee_beans >= 20 and self.available_disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.available_cash += 7
                self.available_water -= 350
                self.available_milk -= 75
                self.available_coffee_beans -= 20
                self.available_disposable_cups -= 1
            else:
                if self.available_water < 350:
                    print("Sorry, not enough water!")
                elif self.available_coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                elif self.available_milk < 75:
                    print("Sorry, not enough coffee milk!")
                elif self.available_disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
        elif x == "3":
            if self.available_water >= 200 and self.available_milk >= 100 \
                    and self.available_coffee_beans >= 12 and self.available_disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.available_cash += 6
                self.available_water -= 200
                self.available_milk -= 100
                self.available_coffee_beans -= 12
                self.available_disposable_cups -= 1
            else:
                if self.available_water < 200:
                    print("Sorry, not enough water!")
                elif self.available_coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                elif self.available_milk < 100:
                    print("Sorry, not enough coffee milk!")
                elif self.available_disposable_cups < 1:
                    print("Sorry, not enough disposable cups!")
        print()

    def take_cash(self):
        print()
        print("I gave you ${}".format(self.available_cash))
        self.available_cash = 0
        print()


my_coffee_machine = CoffeeMachine()

while True:
    user_action = input("Write action (buy, fill, take, remaining, exit): ")

    if user_action == "buy":
        my_coffee_machine.buy_coffee()
    elif user_action == 'fill':
        my_coffee_machine.fill_coffee()
    elif user_action == 'take':
        my_coffee_machine.take_cash()
    elif user_action == 'remaining':
        my_coffee_machine.show_remaining()
    elif user_action == 'exit':
        break
