from node_stack import Stack
from array_queue import Queue
import random

def reverse_digits(a_digit):
    strigified_digit = str(a_digit)
    new_string_digit = ""
    new_data = Stack()

    for char in strigified_digit:
        new_data.push(char)

    for char in range(len(new_data)):
        new_string_digit += new_data.pop()
    
    return int(new_string_digit)

def hot_potato(a_list, rounds):
    queue = Queue()
    
    for name in a_list:
        queue.enqueue(name)
    
    for _ in range(rounds):
        random_selected = random.randrange(0, len(a_list))
        potato_holder = queue.front()
        for _ in range(random_selected):
            person = queue.dequeue()
            queue.enqueue(person)
        receiver = queue.back()
        print(potato_holder, "tosses the potato to", receiver)
    
    print("The music stops and", queue.back(), "is holding the potato!")

        


def main():
    print(reverse_digits(14))
    hot_potato(['Bobby', 'Bruce', 'Chris', 'Dave'], 4)

if __name__ == "__main__":
    main()