class Product(object):
    #a function takes arguments
    def __init__(self, name, quantity=0):
        #initializing
        self.name = name
        self.quantity = quantity

    def restock(self, quantity):
        #self.quantity + quantity = self.quantity
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            raise Exception("I'm sorry we don't have that many.")
