# This is a sample Python script.
from typing import List

import sorting


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def list_comprehension():
    list_1 = [num for num in range(1, 21)]
    list_squares = [num ** 2 for num in list_1]
    list_even = [num for num in list_1 if num % 2 == 0]

    return list_1, list_squares, list_even


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_comprehension()


