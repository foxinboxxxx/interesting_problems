import time
import math
import collections
import itertools

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

    def get_all_divisors_square_number_2_delimeters(self, number):
        divisors_list = []
        for i in range (1, int(number ** 0.5) + 1):
            if number % i == 0:
                # Add 2 numbers during one iteration
                divisors_list.append(i)
                divisors_list.append(number // i)
        return set(divisors_list)

    def get_all_divisors_prime_factor(self, number):
        primes = self._prime_factor(number)
        primes_counted = collections.Counter(primes)

        divisors_exponentiated = [
            [divisor ** i for i in range(count + 1)]
            for divisor, count in primes_counted.items()
        ]

        for prime_exp_combination in itertools.product(*divisors_exponentiated):
            yield self._calculate_product(prime_exp_combination)

    def _prime_factor(self, number):
        delimeter_count = 2
        while math.sqrt(delimeter_count) <= number:
            if number % delimeter_count == 0:
                number /= delimeter_count
                yield delimeter_count
            else:
                delimeter_count += 1

        if number > 1:
            yield number
    
    def _calculate_product(self, iterable):
        acc = 1
        for i in iterable:
            acc *= i
        return acc

    def get_open_doors(self, wrap_function):
        for door_number in range(1, len(self.doors)):
            list_of_divisors = len(list(wrap_function(door_number)))
            if list_of_divisors % 2 != 0:
                self.list_open_doors.append(door_number)
        return self.list_open_doors

if __name__ == "__main__":
    doors = Doors()
    print("Simplest solution, loop through all divisors - doors.get_all_divisors")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors))
    end_time = time.process_time()
    result = end_time - start_time
    print(f"Execution time: {result} ms")
    print("------------------------------\n")

    doors = Doors()
    print("Improved solution, loop through half of divisors - doors.get_all_divisors_generator")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors_generator))
    end_time = time.process_time()
    result = end_time - start_time
    print("Execution time: {:.7f} ms".format(result))
    print("------------------------------\n")

    doors = Doors()
    print("Improved solution, loop through root square of number - doors.get_all_divisors_square_number_2_delimeters")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors_square_number_2_delimeters))
    end_time = time.process_time()
    result = end_time - start_time
    print("Execution time: {:.7f} ms".format(result))
    print("------------------------------\n")

    doors = Doors()
    print("Prime factor solution - doors.prime_factor")
    start_time = time.process_time()
    print(doors.get_open_doors(doors.get_all_divisors_prime_factor))
    end_time = time.process_time()
    result = end_time - start_time
    print(f"Execution time: {result} ms")
    print("------------------------------\n")
