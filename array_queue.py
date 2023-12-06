import arrays

class Queue:
    __slots__ = ['__size', '__front', '__back', '__array']
    def __init__ (self, capacity = 3):
        self.__array = arrays.Array (capacity)
        self.__size = 0
        self.__front = 0
        self.__back = 0

    def __increment(self, index):
        return (index + 1) % len (self.__array)

    def __repr__(self):
        string = ''
        index = self.__front
        for _ in range (self.__size):
            string += str (self.__array [index]) + ', '
            index = self.__increment (index)

        return '[' + string[:-2] + ']'

    def __resize(self):
        new_array = arrays.Array (len (self.__array) * 2)
        index = self.__front
        for i in range(self.__size):
            new_array[i] = self.__array[index]
            index = self.__increment(index)
        self.__front = 0
        self.__back = self.__size
        self.__array = new_array

    def is_empty(self):
        return self.__size == 0

    def __len__(self):
        return self.__size

    def enqueue(self, value):
        if self.__size == len(self.__array):
            self.__resize()

        self.__array[self.__back] = value
        self.__size += 1
        self.__back = self.__increment(self.__back)

    def front(self):
        if self.__size == 0:
            raise IndexError ("Queue is empty")
        return self.__array[self.__front]

    def back(self):
        if self.__size == 0:
            raise IndexError("Queue is empty")
        return self.__array[self.__back - 1]

    def dequeue(self):
        if self.__size == 0:
            raise IndexError ("Queue is empty")
        value = self.__array[self.__front]
        self.__front = self.__increment(self.__front)
        self.__size -= 1
        return value
        