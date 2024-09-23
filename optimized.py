"""
Optimisation de l'algorithme brute force :
1) read_csv() : utilisation d'une compréhension de liste
"""
import csv
import time
import timeit


# Function to retrieve data from a CSV file
def read_csv(file_name):
    """
    Retrieve data from a CSV file.

    :param file_name: Name file.
    :return: Data in list form.
    """

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        raw_data = csv.reader(file)
        next(raw_data)
        return [(row[0], int(row[1]), float(row[2].strip("%"))) for row in raw_data]

