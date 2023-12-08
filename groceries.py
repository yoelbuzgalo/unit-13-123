class GroceryItem:
    __slots__ = ['__name', '__weight', '__price']

    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def __repr__(self):
        return "Item Name: " + self.__name\
        + "\nItem Weight: " + str(self.__weight)\
        + "\nItem Price: " + str(self.__price)
        
    def __eq__(self, other):
        if type(self) == type(other):
            if self.__name == other.get_name():
                return True
        return False

    def __hash__(self):
        return hash(self.__name)
    
    def __lt__(self, other):
        if type(self) == type(other):
            if self.__weight < other.get_weight():
                return True
        return False

    def get_name(self):
        return self.__name
    
    def get_weight(self):
        return self.__weight
    
    def get_price(self):
        return self.__price
    
def main():
    item_1 = GroceryItem('Banana', 4.08, 1.00)
    item_2 = GroceryItem('Salami', 3.05, 1.35)
    item_3 = GroceryItem('Bread', 1, 3)
    item_4 = GroceryItem('Coke', 5.00, 1)
    item_5 = GroceryItem('Wine', 2, 5)
    
    items = [item_1, item_2, item_3, item_4, item_5]

    print(items)
    print(sorted(items))


if __name__ == "__main__":
    main()