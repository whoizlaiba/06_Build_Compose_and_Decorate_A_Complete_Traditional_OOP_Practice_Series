# 8. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  

    @property
    def price(self):
        """Getter for price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price with basic validation"""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price


p = Product(100)
print(p.price)    

p.price = 150
print(p.price)    

del p.price       
