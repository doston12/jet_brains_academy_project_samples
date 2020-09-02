# Write your code here
# Solution for the stage 3/4 of Simple Banking System project

import sqlite3
import math
import sys
import random

card_id = 0

conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS card")
cursor.execute('''CREATE TABLE card
                (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)''')
conn.commit()

class Card:

    def __init__(self):
        self.credit_card_number = self.generate_card_number()
        self.pin_code = self.generate_random_pin()
        self.balance = 0

    def show_balance(self):
        print("Balance:", self.balance)
        print()

    def generate_card_number(self):
        card_digits = self.generate_random_digits()

        card_number = self.generate_number_from_digits(card_digits)

        last_digit = self.luhn_algorithm(card_digits)

        card_number += last_digit

        return card_number

    def generate_random_digits(self):
        card_digits = [4, 0, 0, 0, 0, 0]

        for i in range(8):
            card_digits.append(random.randint(0, 9))

        return card_digits

    def luhn_algorithm(self, card_digits):
        for i in range(14):
            if i % 2 == 0:
                card_digits[i] *= 2

        card_digits_sum = 0

        for digit in card_digits:
            if digit > 9:
                digit -= 9
            card_digits_sum += digit

        last_digit = 0

        while True:
            if (card_digits_sum + last_digit) % 10 == 0:
                return last_digit
            last_digit += 1

    def generate_number_from_digits(self, card_digits):
        card_number = 0
        length = len(card_digits)
        for i in range(length):
            card_number += card_digits[i] * math.pow(10, length-i)
        card_number *= 10

        return int(card_number)

    def generate_random_pin(self):
        pin_code = ''
        for i in range(4):
            pin_code += str(random.randint(0, 9))
        return pin_code

    def card_creation_info(self):
        print("Your card has been created")
        print("Your card number:")
        print(self.credit_card_number)
        print("Your card PIN:")
        print(self.pin_code)
        print()

    def get_card_number(self):
        return str(self.credit_card_number)



def validate_card_number(card_number):
    if len(card_number) < 16:
        return False

    card = int(card_number)
    #print(card)
    card_digits = []

    last_digit = card % 10
    card = card // 10

    while card > 0:
        card_digits.append(card % 10)
        card = card // 10

    card_digits.reverse()
    for i in range(15):
            if i % 2 == 0:
                card_digits[i] *= 2

    card_digits_sum = 0

    for digit in card_digits:
        if digit > 9:
            digit -= 9
        card_digits_sum += digit

    last_digit_x = 0

    while True:
        if (card_digits_sum + last_digit_x) % 10 == 0:
            break
        last_digit_x += 1

    if last_digit == last_digit_x:
        return True
    else:
        return False

while True:

    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    user_action = int(input())
    print()

    if user_action == 1:
        new_card = Card()
        cursor.execute(f"INSERT INTO card VALUES({card_id},{new_card.get_card_number()}, {new_card.pin_code}, 0)")
        conn.commit()
        card_id += 1
        new_card.card_creation_info()
    elif user_action == 2:
        print("Enter your card number:")
        card_number = input()
        print("Enter your PIN:")
        pin = input()
        print()

        cursor.execute('SELECT number, pin FROM card;')
        cards = cursor.fetchall()

        card_exists = False
        for card in cards:

            if card[0] == card_number and card[1] == pin:
                card_exists = True
                print("You have successfully logged in!")
                print()

                while True:
                    print("1. Balance")
                    print("2. Add income")
                    print("3. Do transfer")
                    print("4. Close account")
                    print("5. Log out")
                    print("0. Exit")
                    user_input = int(input())
                    print()

                    if user_input == 1:
                        cursor.execute(f"SELECT balance FROM card WHERE number={card_number}")
                        data = cursor.fetchone()
                        balance = int(data[0])
                        print("Balance:", balance)
                        print()

                    elif user_input == 2:
                        print("Enter income:")
                        income_new = int(input())
                        cursor.execute(f"SELECT balance FROM card WHERE number={card_number};")
                        income_existing = cursor.fetchone()[0]
                        income = income_new + income_existing
                        cursor.execute(f"UPDATE card SET balance={income} WHERE number={card_number}")
                        conn.commit()
                        print("Income was added!")
                        print()

                    elif user_input == 3:
                        print("Transfer")
                        print("Enter card number:")
                        recipient_card_number = input()
                        if validate_card_number(recipient_card_number):
                            if card_number == recipient_card_number:
                                print("You can't transfer money to the same account!")
                                print()
                                continue

                            else:
                                cursor.execute(f"SELECT * FROM card WHERE number={recipient_card_number}")
                                res = cursor.fetchone()

                                if res is not None and res[1] == recipient_card_number:
                                    print("Enter how much money you want to transfer:")
                                    money = int(input())
                                    recipient_balance = res[3]
                                    cursor.execute(f"SELECT balance FROM card WHERE number={card_number}")
                                    x = cursor.fetchone()
                                    sender_balance = x[0]

                                    if money > sender_balance:
                                        print("Not enough money!")
                                        print()
                                    else:
                                        sender_balance -= money
                                        recipient_balance += money
                                        cursor.execute(f"UPDATE card SET balance={recipient_balance} WHERE number={recipient_card_number}")
                                        conn.commit()
                                        cursor.execute(f"UPDATE card SET balance={sender_balance} WHERE number={card_number}")
                                        conn.commit()
                                        print("Success!")
                                        print()
                                else:
                                    print("Such a card does not exist.")
                                    print()

                        else:
                            print("Probably you made a mistake in the card number. Please try again!")
                            print()

                    elif user_input == 4:
                        cursor.execute(f"DELETE FROM card WHERE number={card_number}")
                        conn.commit()
                        print("The account has been closed!")
                        print()

                    elif user_input == 5:
                        break

                    elif user_input == 0:
                        print("Bye!")
                        sys.exit(0)

        if not card_exists:
            print("Wrong card number or PIN!")
            print()

    elif user_action == 0:
        print("Bye!")
        break


