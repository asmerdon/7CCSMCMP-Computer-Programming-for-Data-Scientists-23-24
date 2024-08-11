#In my implementation, I have a global list of products that can be added to the cart.
#During initilisation, I create a few products and add them to this list.
#A user can create their own products in the main program however, using the "C" command I've created.
#This is different to the "A" add command, which allows a user to add a product (and the amount of the product) to the cart.
#The amount of product added to the cart is taken from the total amount in product object.
import random
import json
existingIdentifiers = [] #list of unique identifiers
products = [] #list of products

#main product parent class
class Product:
    def __init__(self, name, price, quantity, brand, uniqueIdentifier=None):
        if not isinstance(name, str): #enforces type on object creation.
            raise TypeError("Name must be a string.")
        self.name = name
        
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")
        self.price = price
        
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        self.quantity = quantity
                
        if not isinstance(brand, str):
            raise TypeError("Brand must be a string.")
        self.brand = brand

        if uniqueIdentifier is None: #a unique identifier is created on product creation. 
            self.uniqueIdentifier = self.generate_unique_identifier()
            existingIdentifiers.append(self.uniqueIdentifier)

    def generate_unique_identifier(self):
        while True:
            identifier = str(random.randrange(10**12, 10**13)) #13 characters.
            if identifier not in existingIdentifiers: #checks list of identifiers (global list) to make sure idenfifier is unique
                return identifier
    
    def toJson(self):
        #converts to json format.
        data = {"name": self.name, "price": self.price, "quantity": self.quantity, "uniqueIdentifier": self.uniqueIdentifier, "brand": self.brand}
        return data
    
    def checkQuantity(self):
        #check the quantity of product in stock.
        if self.quantity == 0:
            print("Product out of stock!")
        else:
            print(self.quantity)
    
    def removeQuantity(self, amount):
        #removes product to add to a shopping cart
        amount = int(amount)
        if amount < 0:
            print("Enter a valid amount (above 0).") #makes sure input is correct
        elif amount <= self.quantity: #checks to see if amount passed into method is less than amount is stock
            self.quantity -= amount  #reduce the available quantity
            print(f"Added {amount} {self.name} to the cart.")
            return amount #returns amount
        else:
            print(f"Not enough {self.name} in stock. Added {self.quantity} to the cart.")
            amount_added = self.quantity #adds the rest of the stock if the amount passed into method is more than the stock
            self.quantity = 0 #adds remaining quantity to a cart
            return amount_added #returns amount for outputting
    
    def addQuantity(self, amount):
        amount = int(amount)
        if amount <= 0:
            print("Enter a valid amount (above 0) to add to remove from your basket.")
        else:
            self.quantity += amount

#clothing child class (extents product)
class Clothing(Product):
    def __init__(self, name, price, quantity, brand, size, material):
        super().__init__(name, price, quantity, brand, uniqueIdentifier=None) #inherits attributes and methods from Product parent class.
        if not isinstance(size, str):
            raise TypeError("Size must be a string.")
        self.size = str(size)

        if not isinstance(material, str):
            raise TypeError("Material must be a string.")
        self.material = str(material)
    
    def toJson(self):
        data = {"name": self.name, "price": self.price, "quantity": self.quantity, "uniqueIdentifier": self.uniqueIdentifier, "brand": self.brand, "size":self.size, "material":self.material}
        return data

#food child class (extents product)
class Food(Product):
    def __init__(self, name, price, quantity, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, brand, uniqueIdentifier=None) #inherits attributes and methods from Product parent class.

        if not isinstance(expiry_date, str):
            raise TypeError("Expiry-date must be a string.")
        self.expiry_date = str(expiry_date)

        if not isinstance(gluten_free, bool):
            raise TypeError("Gluten free attribute must be a boolean value.")
        self.gluten_free = bool(gluten_free)

        if not isinstance(suitable_for_vegans, bool):
            raise TypeError("Suitable for vegans attribute must be a boolean value.")
        self.suitable_for_vegans = bool(suitable_for_vegans)
    
    def toJson(self):
        data = {"name": self.name, "price": self.price, "quantity": self.quantity, "uniqueIdentifier": self.uniqueIdentifier, "brand": self.brand, "expiry_date": self.expiry_date, "gluten_free": self.gluten_free, "suitable_for_vegans": self.suitable_for_vegans}
        return data

#drink child class (extents product)
class Drink(Product):
    def __init__(self, name, price, quantity, brand, expiry_date, alcoholic):
        super().__init__(name, price, quantity, brand, uniqueIdentifier=None) #inherits attributes and methods from Product parent class.

        if not isinstance(expiry_date, str):
            raise TypeError("Expiry-date must be a string.")
        self.expiry_date = expiry_date

        if not isinstance(alcoholic, bool):
            raise TypeError("Alcoholic attribute must be a boolean value.")
        self.alcoholic = alcoholic

    def toJson(self):
        # converts to json
        data = {"name": self.name, "price": self.price, "quantity": self.quantity, "uniqueIdentifier": self.uniqueIdentifier, "brand": self.brand, "expiry_date": self.expiry_date, "alcoholic": self.alcoholic}
        return data
    
#creating the products and adding them to a global list of products

Pen = Product(name="Pen", price=0.99, quantity=300, brand="KCL Supplies")
Tshirt = Clothing(name="T-shirt", price=19.99, quantity=50, brand="KCL Drip Co", size="M", material="Cotton")
Bread = Food(name="Bread", price=2.49, quantity=100, brand="KCL Scran Co", expiry_date="01-11-2023", gluten_free=True, suitable_for_vegans=True)
Coke = Drink(name="Coke", price=1.29, quantity=200, brand="KCL Bevs Co", expiry_date="01-12-2023", alcoholic=False)
Beer = Drink(name="Beer", price=1.29, quantity=200, brand="KCL Bevs Co", expiry_date="25-12-2024", alcoholic=True)
#uncomment line below to see an example of product type enforcement (material = 1.) during instantiation:
#Tshirt2 = Clothing(name="T-shirt2", price=19.99, quantity=50, brand="KCL Drip Co", size="M", material=1)
products.append(Pen)
products.append(Tshirt)
products.append(Bread)
products.append(Coke)
products.append(Beer)

#shopping cart class
class ShoppingCart:
    def __init__(self, cart=[]):
        self.cart = cart #list of items in cart

    def addProduct(self, productName, amount):
        product = next((p for p in products if p.name == productName), None) #checks through store product list to see if product is sold
        if product is None:
            print(f"Product '{productName}' not in store! Enter 'L' to see a list of every product available.") #prompts user if product not found
        else:
            addedQuantity = product.removeQuantity(amount) #calls removeQuantity function and passes in the listed amount as arg.
            totalPrice = addedQuantity * product.price #calculates price
            print(f"Cost: £{totalPrice}")
            self.cart.append((product, addedQuantity, totalPrice)) #appends product obj, quantity and total price to cart list.
            print(f"Added {addedQuantity} {productName}(s) to your cart.")
    
    def removeProduct(self, productName, amount):
        for i in range(len(self.cart)): #iterates through cart
            product, addedQuantity, totalPrice = self.cart[i] #assigns each value of i to variable.
            if product.name == productName and addedQuantity >= int(amount): #check inputs are valid.
                product.addQuantity(amount)
                newQuantity = addedQuantity - int(amount)
                newTotalPrice = totalPrice - (int(amount) * product.price)
                if newQuantity > 0:
                    self.cart[i] = (product, newQuantity, newTotalPrice)
                else:
                    self.cart.pop(i)  # removes the product from the cart if the quantity becomes 0.
                print(f"Removed {amount} {productName} from your cart.")
                break
        else:
            print(f"Not enough {productName} in the cart to remove {amount}.") #doesn't remove product if amount inputted is more than what's in the cart.
    
    def getContents(self):
        cartTotal = 0
        for i in range(len(self.cart)): #iterates through cart.
            product, addedQuantity, totalPrice = self.cart[i] #assigns each value of i to variable.
            print(f"{i+1}: {addedQuantity} * {product.name} = £{totalPrice}") #prints price and quantity of each item.
            cartTotal += totalPrice
        print(f"Total = £{cartTotal}") #prints cart total price.
        
    def changeProductQuantity(self, productName, amount):
        for i in range(len(self.cart)-1): #iterates through cart.
            product, addedQuantity, totalPrice = self.cart[i] #assigns each value of i to variable.
            if product.name == productName and addedQuantity < int(amount): #check if amount is more than what's already in the basket.
                self.addProduct(productName, amount-addedQuantity) #adds difference between 2 amounts.
            elif product.name == productName and addedQuantity > int(amount): #check if amount is less than what's already in the basket.
                self.removeProduct(productName, addedQuantity-amount) #removes difference between 2 amounts.

#main program
def main_loop():
    print("The program has started.")
    print("Please insert your next command (H for help):")
    currentShop = ShoppingCart() #create instance of shoppingCart.
    terminated = False
    while not terminated:
        #product names list (for easier functionality/testing).
        product_names = [product.name for product in products] #list products in store.
        print("Products in store: ")
        print(product_names)
        c = input("Type your next command: ")
        if c == "A":
            productName = input("Enter the product you would like to add: ") #add product.
            positive = False
            while positive == False:
                amount = input(f"Enter the amount of {productName} you would like: ")
                if amount.isnumeric():
                    positive = True
            currentShop.addProduct(productName, amount) #calls addProduct function.
        elif c == "R":
            productName = input("Enter the product you would like to remove from your cart: ")
            amount = input(f"Enter the amount of {productName} you would like to remove from your cart: ")
            currentShop.removeProduct(productName, amount) #calls removeProduct function.
        elif c == "S":
            currentShop.getContents()
        elif c == "Q":
            productName = input("Enter the product you would like to change the quantity of: ")
            amount = int(input(f"Enter the amount of {productName} you would like instead: "))
            currentShop.changeProductQuantity(productName, amount) #calls changeProductQuantity function.
        elif c == "C": #my own product creation option.
            objectType = str(input("Enter type product you would like to add to the store (generic, clothing, food, drink): ")) #determines type of product, for object instance creation.
            objectName = str(input("Enter the name of the product: ")) #product name.

            while True: #makes sure the input is valid (float).
                try:
                    objectPrice = float(input("Enter the price of the product: ")) #product price.
                except ValueError:
                    print("Enter a valid input (float).")
                else:
                    break
            
            while True: #makessure the input is valid (int).
                try:
                    objectQuantity = int(input("Enter the quantity of the product in stock: ")) #product quantity in stock.
                except ValueError:
                    print("Enter a valid input (int): ")
                else:
                    break

            objectBrand = str(input("Enter the brand of the product: ")) #product brand.

            def boolChecker(input): #function to convert user input (0 or 1) to a boolean value.
                    if input == "0":
                        return False
                    if input == "1":
                        return True
                    else:
                        print("Bool input not valid. Try creating product again.")

            if objectType == "generic": #generic as in the Product class (parent).
                newProduct = Product(name=objectName, price=objectPrice , quantity=objectQuantity, brand=objectBrand)
                products.append(newProduct)

            elif objectType == "clothing": #clothing class.
                clothingSize = str(input("Enter the size of the clothing item: "))
                clothingMaterial = str(input("Enter the material of the clothing input: "))
                newProduct = Clothing(name=objectName, price=objectPrice , quantity=objectQuantity, brand=objectBrand, size=clothingSize, material=clothingMaterial)
                products.append(newProduct)

            elif objectType == "food": #food class.
                foodExpiry = str(input("Enter the expiry date: "))

                isBool = False #makes sure value inputted is 0 or a 1.
                while isBool == False:
                    foodGluten = str(input("Enter if food product is gluten free (0 for false, 1 for true): "))
                    if foodGluten == '0' or foodGluten == '1':
                        foodGlutenBool = boolChecker(foodGluten)
                        isBool = True
                    else:
                        print("Try again (0 or 1):")

                isBool = False
                while isBool == False: #makes sure value inputted is 0 or a 1.
                    foodVegan = str(input("Enter if food product is suitable of vegans (0 for false, 1 for true): "))
                    if foodVegan =='0' or foodGluten =='1':
                        foodVeganBool = boolChecker(foodVegan)
                        isBool = True
                    else:
                        print("Try agian (0 or 1):")

                newProduct = Food(name=objectName, price=objectPrice , quantity=objectQuantity, brand=objectBrand, expiry_date=foodExpiry, gluten_free=foodGlutenBool, suitable_for_vegans=foodVeganBool)
                products.append(newProduct)

            elif objectType == "drink": #drink class.
                drinkExpiry = str(input("Enter the expiry date: "))

                isBool = False
                while isBool == False: #makes sure value inputted is 0 or a 1.
                    alcoholic = str(input("Enter if drink product is alcoholic (0 for false, 1 for true): "))
                    if alcoholic == '0' or alcoholic == '1':
                        alcoholicBool = boolChecker(alcoholic)
                        isBool = True
                    else:
                        print("Try again (0 or 1): ")

                newProduct = Drink(name=objectName, price=objectPrice , quantity=objectQuantity, brand=objectBrand, expiry_date=drinkExpiry, alcoholic=alcoholicBool)
                products.append(newProduct)

        elif c == "E":
            jsonList = [] #creates list for json 
            for product, _, _ in currentShop.cart:
                jsonList.append(product.toJson())
            print("JSON Output: ")
            print(jsonList) #outputs to terminal
            filename = input("Enter file name for JSON export: ") #input for json file
            with open(filename, 'w') as json_file:
                json.dump(jsonList, json_file, indent=3)
            print(f"The data has been exported to {filename}.json.") #exports to json file
        elif c == "T":
            print("Thanks for shopping!")
            terminated = True
        elif c == "H":
            print("The program supports the following commands:")
            print("[A] - Add a new product to the cart")
            print("[R] - Remove a product from the cart")
            print("[S] - Print a summary of the cart")
            print("[Q] - Change the quantity of a product")
            print("[C] - Create a new product for the shop")
            print("[E] - Export a JSON version of the cart")
            print("[T] - Terminate the program")
            print("[H] - List the supported commands")
            print("[L] - List the products in store")
        elif c == "L": #added my own command that lists the product names for easier testing
            print(product_names)
        else:
            print("Command not recognised, please try again (H for help, T to terminate).")

main_loop()