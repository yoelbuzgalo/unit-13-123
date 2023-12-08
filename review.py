import csv
import array_utils

def zip_lookup(filename, zipcode):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        for record in csv_reader:
            if zipcode == record[0]:
                return record[1]
        raise ValueError("Doesn't exist in the file")
    
def arrays_equal(array_1, array_2, index=0):
    if len(array_1) != len(array_2):
        return False
    elif index == len(array_1):
        return True
    elif array_1[index] == array_2[index]:
        return arrays_equal(array_1, array_2, index +1)
    else:
        return False
    
def is_power(a, b):
    if a == 1:
        return True
    elif a % b == 0:
        return is_power(a/b, b)
    else:
        return False


def main():
    # print(zip_lookup("./data/zip_codes.csv", "00603"))
    print(is_power(27, 3))
    array_1 = array_utils.range_array(0,10)
    array_2 = array_utils.range_array(0,10)
    array_3 = array_utils.range_array(0,5)
    print(arrays_equal(array_1, array_2))
    print(arrays_equal(array_1, array_3))


if __name__ == "__main__":
    main()