import csv

def zip_lookup(filename, zipcode):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        for record in csv_reader:
            if zipcode == record[0]:
                return record[1]
        raise ValueError("Doesn't exist in the file")
    
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


if __name__ == "__main__":
    main()