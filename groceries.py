import csv
import arrays
import random
from array_queue import Queue
from node_stack import Stack

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
    
class Customer:
    __slots__ = ['__list', '__cart', '__bags']
    def __init__(self, list_size, store):
        self.__cart = set()
        self.__bags = list()
        possible_items = list(store.keys())
        random.shuffle(possible_items)
        self.__list = possible_items[:list_size]

    def get_list(self):
        return self.__list
    
    def get_cart(self):
        return self.__cart
    
    def shop(self, store):
        for item_name in self.__list:
            self.__cart.add(store[item_name])

    def unload(self, conveyor):
        for _ in range(len(self.__cart)):
            conveyor.enqueue(self.__cart.pop())
        return
    
    def checkout(self, conveyor):
        total_price = 0
        bagged = False
    
        while(not conveyor.is_empty()):
            item = conveyor.dequeue()
            total_price += item.get_price()
            for bag in self.__bags:
                if item < bag.peek():
                    bag.push(item)
                    bagged = True
                    break
            if not bagged:
                bag = Stack()
                bag.push(item)
                self.__bags.append(bag)

        return total_price
    
    def unpack(self):
        for bag_num in range(len(self.__bags)):
            print("Bag #", bag_num, sep="")
            while (not self.__bags[bag_num].is_empty()):
                print(self.__bags[bag_num].pop())

def stock_store(filename):
    stock = dict()
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for record in csv_reader:
                stock[record[0]] = GroceryItem(record[0], int(record[1]), int(record[2]))
        return stock
    except FileNotFoundError:
        print("There was an error trying to open the file")
    return



    
def main():
    # item_1 = GroceryItem('Banana', 4.08, 1.00)
    # item_2 = GroceryItem('Salami', 3.05, 1.35)
    # item_3 = GroceryItem('Bread', 1, 3)
    # item_4 = GroceryItem('Coke', 5.00, 1)
    # item_5 = GroceryItem('Wine', 2, 5)
    
    # items = [item_1, item_2, item_3, item_4, item_5]

    # print(items)
    # print(sorted(items))

    store = stock_store("./data/groceries.csv")
    customer = Customer(25, store)
    customer.shop(store)
    # print(customer.get_cart())

    conveyor_belt = Queue()
    customer.unload(conveyor_belt)
    
    # print(conveyor_belt)
    print(customer.checkout(conveyor_belt))
    customer.unpack()
    
    


if __name__ == "__main__":
    main()