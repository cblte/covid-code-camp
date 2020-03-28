# -*- encoding: utf-8 -*-
# 
# code camp day 06
#
# title: the vending machine
# 
# a soda vending machine.
# - gives out a list of drinks
# - you can buy one
# - can be restocked

# need a list of soda
#
#

class Product:
    """The product with all its information"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.sold = 0

    def getInfo(self):
        """returns an str with information about the product"""
        s = "%15s costs you %3.2f (sold: %d)" % (self.name, self.price, self.sold)
        return s

    def soldOne(self):
        self.sold += 1


# ----------------- end of class Product

class VendingMachine:
    """A Vending machine that takes products to be sold to customers"""

    def __init__ (self, products):
        self.products = products
        # init vending machine with zero amounts
        self.amountOfProducts = {}
        self.productsSold = 0
        self.moneyEarned = 0
        for p in self.products:
            self.amountOfProducts.update({p.name : 0})


    def infoAbout(self):
        print("--- --- ---")
        print("Vending machine v1.0\n")
        print("In Stock right now:")
        self.listProducts()
        print("---")
        print("Products sold so far: %d" % (self.productsSold))
        print("Generated Money: %.2f" % (self.moneyEarned))



    def listProducts(self):
        """List all available products"""
        print("Available products:")
        for product in self.products:
            inStock = " (In Stock: %3d)" % (self.amountOfProducts[product.name])
            print(product.getInfo() + inStock)


    def refill(self, product, amount = 10):
        """ pass in a product object to refill to maximum if not given"""
        self.amountOfProducts.update({product.name: amount})

    
    def sellProduct(self, product):
        """ sell one piece of a product of possible """
        if(self.amountOfProducts[product.name] > 0):
            self.amountOfProducts[product.name] -= 1
            self.moneyEarned += product.price
            self.productsSold += 1
            product.soldOne()
            print("Thank you for buying %s" % (product.name))
            print("There are %2d of %s left in the machine" % (self.amountOfProducts[product.name], product.name))
        else:
            print("Sorry, no more %s left. Please talk to owner for refill" % (product.name))




# ----------------- end of class VendingMachine


# setup the machine
pCola = Product("Coka Cola", 1.5)
pZero = Product("Cola Zero", 2)
pLight = Product("Cola Light", 1.8)
pWater = Product("Water", 1.0)

products = [pCola, pZero, pLight, pWater]

sodaMachine = VendingMachine(products)
sodaMachine.listProducts()
# refill some products
sodaMachine.refill(pCola)
sodaMachine.refill(pZero,2)
sodaMachine.refill(pLight, 8)
sodaMachine.refill(pWater)
sodaMachine.listProducts()

sodaMachine.sellProduct(pCola)
sodaMachine.sellProduct(pLight)
sodaMachine.sellProduct(pCola)
sodaMachine.sellProduct(pZero)
sodaMachine.sellProduct(pZero)
sodaMachine.sellProduct(pWater)
sodaMachine.sellProduct(pZero)
sodaMachine.sellProduct(pWater)
sodaMachine.sellProduct(pZero)

sodaMachine.infoAbout()
