import tkinter as tkinter_import
from tkinter import messagebox  # this allows for notifications
from time import sleep  # to implement a type of loading screen


class ShoppingCart():
    """This class is created as a shopping cart.It contains items(the items that the user wants), wallet(money in the users account) and price_of_cart(the total price)"""
    def __init__(self, items, wallet, price_of_cart):
        self.items = items
        self.__wallet = wallet  # wallet is private so this is not accidentally changed
        self.price_of_cart = price_of_cart

    def __str__(self):
        string1 = "Products\n"
        for key in self.items.keys():
            string1 += str(key)
            string1 += '\n'
        for value in self.items.values():
            string1 += str(value)
            string1 += '\n'
        return string1 + 'Wallet: {} + Total Price: {}'.format(self.__wallet, self.price_of_cart)

    def print_items(self):
        """This prints out the shopping cart dictionary in the format k ----> v where k is key and v is value"""
        print("\nShopping Cart\n")
        print("=================\n")
        for k, v in self.items.items():
            print(k, '---->', v)

    def get_wallet(self):
        """get as wallet is private"""
        return self.__wallet

    def set_wallet(self, wallet):
        """set as wallet is private"""
        self.__wallet = wallet

    def add_wallet(self, wallet_money):
        """this adds a user-defined amount of money to the wallet"""
        self.__wallet += wallet_money
        return self.__wallet

    def __gt__(self, new_wallet):
        if new_wallet > sc.price_of_cart:
            print("You have paid")
        else:
            print("You have not paid")

    def __add__(self, new_wallet):
        new_wallet += sc.get_wallet()


class Customer(object):
    """A customer class which the loyal customers and bargain hunters inherit"""
    def __init__(self, customer_type, name, product_list):
        self.name = name
        self.customer_type = customer_type
        self.product_list = product_list

    def __str__(self):
        return "\nCustomer Name: {} Customer Type: {}".format(self.name, self.customer_type)


class LoyalCustomers(Customer):
    """Loyal Customer class inherited from Customer class"""
    def __init__(self, customer_type, name, product_list, exclusive):
        Customer.__init__(self, customer_type, name, product_list)
        self.exclusive = exclusive

    def __str__(self):
        return "\nCustomer Name: {} Customer Type: {}".format(self.name, self.customer_type)

    def print_exclusive(self):
        """This prints out the exclusive items for the loyal customers.The bargain hunter dictionary and the loyal customer dictionary"""
        print("\nProducts including Exclusives\n")
        print("=================\n")
        for k, v in self.product_list.items():
            print(k, '---->', v)
        for k, v in self.exclusive.items():
            print(k, '---->', v)
        print("\n")

    def loyal_notification(self):
        """sends out notification for loyal customers"""
        box = tkinter_import.Tk()
        box.withdraw()  # This allows to just show the message box
        messagebox.showinfo(self.name, "Thanks for being a loyal customer")


class BargainHunters(Customer):
    """Bargain Hunter class inherited from Customer class"""
    def __init__(self, customer_type, name, product_list):
        Customer.__init__(self, customer_type, name, product_list)

    def __str__(self):
        return "\nCustomer Name: {} Customer Type: {}".format(self.name, self.customer_type)

    def print_normal(self):
        """This prints out the normal items for the bargain hunters."""
        print("\nProducts available\n")
        print("=================\n")
        for k, v in self.product_list.items():
            print(k, '---->', v)
        print("\n")

    def bargain_notification(self):
        """Notification for bargain hunters"""
        box = tkinter_import.Tk()
        box.withdraw()  # This allows for just showing the message box
        messagebox.showinfo(self.name, "Remember if you spend over 100 a week you can become a LoyalCustomer. This grants exclusive access to products")


# defining classes
bh = BargainHunters("Bargain Hunter", "", dict({"6 Oranges": 1.00, "6 Apples": 1.10, "2 pack of Steak": 10.00, "4 cod fillets": 7.00, "Orange Juice": 1.00, "4 chicken fillets": 7.50}))
lc = LoyalCustomers("Loyal Customer", "", dict({"6 Oranges": 1.00, "6 Apples": 1.10, "2 pack of Steak": 10.00, "4 cod fillets": 7.00, "Orange Juice": 1.00, "4 chicken fillets": 7.50}), dict({"Apple Juice": 1.00, "Kobe Beef": 50.00, "4 salmon fillets": 7.50, "6 Organic Oranges": 2.00, "6 Organic Apples": 2.10}))
sc = ShoppingCart(dict({}), 0.00, 0.00)


def main():
    print("             Welcome to the shop...              \n")
    print("=================================================\n")
    sleep(2)  # this just shows welcome to the shop for 2 seconds
    one_equals = False  # this is to check whether option one has been chosen or not
    loyal_cust = False  # this checks whether the customer is a loyal customer
    name_in_file = ""
    wallet_data = "0.0"  # default value for users wallet

    while True:
        # command line menu
        print("1.Create a customer.")
        print("2.List products.")
        print("3.Add/remove a product to the shopping cart.")
        print("4.See current shopping cart.")
        print("5.Checkout")

        input1 = input("Enter a number please")
        if input1 == "1":
            print("You are about to create a customer...")
            cust_name = input("What is your name?").strip()  # strip gets rid of any trailing or leading whitespace

            # checks for name in file
            with open('wallet.txt', 'r') as name:
                for line in name:
                    if cust_name in line:
                        print("Welcome back " + cust_name)
                        name_in_file += "name"

            try:
                spend = float(input("How much money do you spend a week in the shop?"))

                if spend >= 100:
                    lc.name = cust_name
                    loyal_cust = True  # sets loyal customer to True
                else:
                    bh.name = cust_name
                one_equals = True  # one has been chosen

            except ValueError:  # ensures a number has been entered
                print("That is not a value.Try again")

        elif one_equals is True and input1 == "2":  # checks that one has been chosen and that input is 2
            if loyal_cust:
                print(lc)  # prints loyal customer item
                lc.print_exclusive()  # prints the exclusive items for loyal customer
            else:
                print(bh)  # prints the bargain hunter class
                bh.print_normal()  # prints the normal items

        elif input1 == "3" and one_equals is True:

            add_remove = input("Would you like to add or remove a/r")
            if add_remove == "a" or add_remove == "A":
                item1 = input("Enter the item you want to add")
                if item1 in sc.items and item1 in lc.product_list:
                    sc.items.update({item1: sc.items.get(item1) + lc.product_list.get(item1)})  # adds the price of the item again if the item is already in the shopping cart

                elif item1 in sc.items and item1 in lc.exclusive:
                    sc.items.update({item1: sc.items.get(item1) + lc.exclusive.get(item1)})  # adds the price of the item again if the item is already in the shopping cart

                else:  # if the item is not in the shopping cart
                    if loyal_cust is True and item1 in lc.exclusive:
                        sc.items.update({item1: lc.exclusive.get(item1)})  # adds an exclusive item

                    elif loyal_cust is True and item1 in lc.product_list:
                        sc.items.update({item1: lc.product_list.get(item1)})  # adds a loyal customer normal item

                    elif loyal_cust is not True and item1 in bh.product_list:
                        sc.items.update({item1: bh.product_list.get(item1)})  # adds a bargain hunter item

            if add_remove == "r" or add_remove == "R" and len(sc.items) > 0:  # ensures that there are items to be removed in the cart
                item1 = input("Enter the item you want to remove")
                if item1 in sc.items:
                    sc.items.pop(item1)  # removes an item
                else:
                    print("This cannot be removed")

        elif input1 == "4" and one_equals is True:
            sc.print_items()  # prints out the shopping cart

        elif input1 == "5" and len(sc.items) > 0:  # an item has to be added to the shopping cart for this to work

            if loyal_cust:
                with open("wallet.txt", "r") as wallet:
                    for line in wallet:
                        if lc.name in line:
                            wallet_data = line.replace(lc.name, '')  # this takes just the money from the file and stores it in wallet_data

            else:
                with open("wallet.txt", "r") as wallet:
                    for line in wallet:
                        if bh.name in line:
                            wallet_data = line.replace(bh.name, '')  # this takes just the money from the file and stores it in wallet_data

            new_wallet = float(wallet_data)
            sc.price_of_cart = sum(sc.items.values())  # gets the total of the shopping cart
            print("You are checking out")
            print("Your wallet contains" + str(new_wallet))
            print("Your total is " + str(sc.price_of_cart))
            print("Your remaining wallet funds will be stored for your next purchase in the shop")

            while True:
                thing = input("Would you like to add to your wallet?y/n")

                if thing == "Y" or thing == "y":
                    new = float(input("How much are you adding to your wallet?"))
                    sc.add_wallet(new)  # new is added to the wallet
                    new_wallet += sc.get_wallet()  # the new amount in wallet
                    print("Your wallet contains " + str(new_wallet))

                elif thing == "N" or thing == "n":
                    print("Ok then you can pay")
                    paying_input = input("Would you like to pay?y/n")
                    if paying_input == "y" or paying_input == "Y":
                        if new_wallet >= sc.price_of_cart:
                            new_wallet -= sc.price_of_cart
                            print("You have paid, Goodbye")

                            if name_in_file != "name":
                                with open("wallet.txt", "a") as wallet:
                                    if loyal_cust:
                                        wallet.write(lc.name + ' ' + str(new_wallet) + '\n')  # stores the remainder of wallet in the text file along with the users name
                                    else:
                                        wallet.write(bh.name + ' ' + str(new_wallet) + '\n')  # stores the remainder of wallet in the text file along with the users name
                            else:
                                # this reads the file first
                                with open("wallet.txt", "r") as wallet_text:
                                    line_new = []  # creates a list which allows the replacement of certain words in a line

                                    for words in wallet_text.readlines():
                                        if lc.name in words or bh.name in words:
                                            line_new.append(words.replace(wallet_data, str(new_wallet) + '\n'))

                                # this writes line_new to the file replacing the old funds with the new
                                with open("wallet.txt", "w") as wallet_text:
                                    for line in line_new:
                                        wallet_text.writelines(line)

                            if loyal_cust:
                                lc.loyal_notification()  # sends the loyal customer notification
                            else:
                                bh.bargain_notification()  # sends the bargain hunter notification
                            exit()
                        else:
                            print("You do not have enough money")
                            if loyal_cust:
                                lc.loyal_notification()  # sends the loyal customer notification
                            else:
                                bh.bargain_notification()  # sends the bargain hunter notification
                            exit()  # exits the loop
                    elif paying_input == "n" or paying_input == "N":
                        print("Ok thank you goodbye!")
                        exit()  # exits the loop
        else:
            print("That is not a valid option")

main()
