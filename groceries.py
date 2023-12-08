class GroceryItem:
    __slots__ = ['__name', '__weight', '__price']

    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get__weight(self):
        return self.__weight
    
    def get_price(self):
        return self.__price