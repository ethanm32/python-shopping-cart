# python-shopping-cart
This is a python application to manage a shopping cart

Author: Ethan Moran
Date: 16/02/2021

This program utilises a command line menu. A user can choose one of 5 options. These are Create a customer, List products, Add/Remove a product to the shopping cart, see current shopping cart and checkout. These are chosen by their corresponding numbers – 1-5.

When option 1 is chosen a new customer is created. If your name is already logged in the system(wallet.txt) you will receive a welcome back message(your name is case sensitive). The user funds from the last purchase will be available in the wallet. You will also be asked how much money you spend per week in the shop to determine what kind of shopper you are. Option two is only accessible if option one has already been chosen. 

This option shows the products available. Option 3 allows for the adding and removal of items in the shopping cart. When option 4 is chosen the shopping cart with the items the user has chosen is shown. Finally, when number 5 is chosen, the user can checkout and can pay for their items. The wallet of each user is logged and can be used for more purchases if the same name is entered in Option 1 (otherwise a new customer is created). 

In the checkout area, the user can add to their wallet or not. If the user chooses not to and they do not have enough funds the program exits. Otherwise it exits if the user has paid for their items. 
