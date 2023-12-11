import csv
from node_stack import Stack
from array_queue import Queue
import random

# Part 1 (Streets)

class Street:
    __slots__ = ['__name', '__types', '__direction']
    def __init__(self, name, direction, type=None):
        self.__name = name
        self.__types = set()
        if type != None:
            self.__types.add(type)
        self.__direction = direction

    def get_name(self):
        return self.__name
    
    def get_types(self):
        return self.__types
    
    def add_type(self, type):
        self.__types.add(type)
    
    def get_direction(self):
        return self.__direction

class Streets:
    __slots__ = ['__streets']

    def __init__(self):
        self.__streets = dict()
    
    def add_street(self, street: Street):
        self.__streets[street.get_name()] = street
    
    def get_street(self, name):
        if name in self.__streets:
            return self.__streets[name]
    
    def inquire_street(self, name, street_type):
        if (self.get_street(name).get_name() == name) and (street_type in self.get_street_types(name)):
            return True
        return False
    
    def count_streets_type(self, type):
        count = 0
        for street in self.__streets:
            if type in self.__streets[street].get_types():
                count += 1
        return count
    
    def get_street_types(self, name):
        return self.get_street(name).get_types()


def parse_streets(filename):
    try:
        with open(filename) as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader) # Skip the header
            streets = Streets()
            for record in csv_reader:
                StreetName, StreetType, PostDirection = record
                if streets.get_street(StreetName) == None:
                    streets.add_street(Street(StreetName, PostDirection, StreetType))
                else:
                    streets.get_street(StreetName).add_type(StreetType)
            return streets
    except FileNotFoundError:
        print("Could not find or open:", filename)


# Part 3-5 (Exam)

class Exam:
    exam_count = 0
    __slots__ = ['__name', '__total_points', '__total_possible_points', '__exam_id']
    def __init__(self, name, total_points, total_possible_points):
        self.__name = name
        self.__total_points = total_points
        self.__total_possible_points = total_possible_points
        self.__exam_id = Exam.exam_count # Assign current unique exam count identifier to this instance
        
        Exam.exam_count += 1 # Increment exam count when an exam is created

    def __repr__(self):
        return self.__name + " " + "("+str(self.get_ratio())+")"
    
    def __hash__(self):
        return hash(str(self)+str(self.__exam_id))
    
    def __lt__(self, other):
        if type(self) == type(other):
            if self.get_ratio() < other.get_ratio():
                return True
            elif self.get_ratio() == other.get_ratio():
                if self.__name < other.get_name():
                    return True
        return False
    
    def __eq__(self, other):
        if type(self) == type(other):
            if self.__name == other.__name:
                return True
        return False

    def get_name(self):
        return self.__name
    
    def get_total_points(self):
        return self.__total_points
    
    def get_total_possible_points(self):
        return self.__total_possible_points
    
    def add_total_points(self, points):
        self.__total_points += points

    def add_total_possible_points(self, points):
        self.__total_possible_points += points

    def get_ratio(self):
        return 100 * (self.__total_points / self.__total_possible_points)

def simulate_grading_process():
    stack_of_exams = Stack()
    grade_database = Queue()
    student_names = [
    "Emily Johnson", "Ethan Parker", "Olivia Martinez", "Liam Carter", "Sophia Adams",
    "Noah Thompson", "Isabella Rivera", "Mason Wright", "Ava Hall", "Lucas Mitchell",
    "Mia Garcia", "Oliver Cooper", "Amelia Perez", "Elijah Scott", "Harper King",
    "James Ramirez", "Charlotte Bennett", "Alexander Reed", "Abigail Turner", "Benjamin Hayes",
    "Evelyn Flores", "William Ross", "Scarlett Phillips", "Logan Morgan", "Victoria Coleman",
    "Daniel Wood", "Grace Foster", "Samuel Diaz", "Aria Price", "Henry Ward"
    ]
    print("Administering exams:")
    for name in student_names:
        random_score = random.randint(0, 100)
        exam = Exam(name, random_score, 100)
        stack_of_exams.push(exam)
        print("\tCompleted:", exam)
    
    print("Grading exams:")
    list_of_graded = Queue()
    for _ in range(len(stack_of_exams)):
        grade = stack_of_exams.pop()
        list_of_graded.enqueue(grade)
        print("\tGraded:", grade)

    print("Entering grades into grade database")
    database = list()
    for _ in range(len(list_of_graded)):
        grade = list_of_graded.dequeue()
        database.append(grade)
        print("\tEntered:", grade)
    
    database.sort()
    database.reverse()

    print("Displaying sorted grades:")
    for grade in database:
        print("\t",grade)
    
def main():
    # streets = parse_streets("./data/streets.csv")
    # print(streets.count_streets_type('DR'))
    # print(streets.inquire_street('RED LEAF', 'LN'))
    # print(streets.get_street_types('VISTA'))
    simulate_grading_process()


if __name__ == "__main__":
    main()
    

