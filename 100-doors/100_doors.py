import time
import math


"""
Initialize an array of 101 doors where 
False - door is closed,
True - is opened
"""
class Doors:
    def __init__(self):
        self.doors = [False] * 101 # ignore index 0
        self.list_open_doors = []
        self.doors_10000 = [False] * 10001 # ignore index 0

    def get_all_divisors(self, number):
        divisors_list = []
        for i in range(1, int(number) + 1):
            if number % i == 0:
                divisors_list.append(i)
        return divisors_list
    
    def get_open_doors(self, doors):
        for door_number in range(1, len(doors)):
            list_of_divisors = len(self.get_all_divisors(door_number))
            if list_of_divisors % 2 != 0:
                self.list_open_doors.append(door_number)
        return self.list_open_doors


if __name__ == "__main__":
    doors = Doors()

    start_time = time.process_time()
    print(doors.get_open_doors(doors.doors))
    end_time = time.process_time()
    result = end_time - start_time
    print(f"Execution time: {result} ms")
