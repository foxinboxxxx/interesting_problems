import time
import math


"""
Initialize an array of 101 and 10001 doors where 
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
    
    def get_all_divisors_generator(self, number):
        for i in range(1, int(number / 2) + 1):
            if number % i == 0:
                yield i
        yield number

    def get_open_doors(self, wrap_function):
        for door_number in range(1, len(self.doors)):
            list_of_divisors = len(list(wrap_function(door_number)))
            if list_of_divisors % 2 != 0:
                self.list_open_doors.append(door_number)
        return self.list_open_doors


if __name__ == "__main__":
    doors = Doors()

    print("Improved solution, loop through half of divisors - doors.get_all_divisors_generator")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors_generator))
    end_time = time.process_time()
    result = end_time - start_time
    print("Execution time: {:.7f} ms".format(result))
    print("------------------------------\n")


    doors = Doors()

    print("Simplest solution, loop through all divisors - doors.get_all_divisors")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors))
    end_time = time.process_time()
    result = end_time - start_time
    print(f"Execution time: {result} ms")
    print("------------------------------\n")
