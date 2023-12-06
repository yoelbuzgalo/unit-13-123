from node_stack import Stack
from array_queue import Queue

def reverse_digits(a_digit):
    strigified_digit = str(a_digit)
    new_string_digit = ""
    new_data = Stack()

    for char in strigified_digit:
        new_data.push(char)

    for char in range(len(new_data)):
        new_string_digit += new_data.pop()
    
    return int(new_string_digit)

def main():
    print(reverse_digits(14))

if __name__ == "__main__":
    main()