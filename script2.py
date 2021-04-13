import random

MIN = -1000
MAX = 1000
MUTANT_MIN = -10
MUTANT_MAX = 10
ACCEPTED_ERROR = 0
POPULATION_NUMBER = 50


class Solution:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def test_solution(self):
        a = 3 * self.x + 2 * self.y + self.z

        return abs(a - 15)

    def human_readable(self):
        return "(x={}, y={}, z={}) ".format(self.x, self.y, self.z)


def generate_random_between(min, max):
    """ Return a random int between min and max """
    return random.randint(min, max)


def generate_random_solution():
    """ Return a random solution (x, y, z) """
    x = generate_random_between(MIN, MAX)
    y = generate_random_between(MIN, MAX)
    z = generate_random_between(MIN, MAX)

    return Solution(x, y, z)


def generate_random_mutant_solution(parent):
    """ Return a random mutant solution based on given (x, y, z) """
    x = parent.x + generate_random_between(MUTANT_MIN, MUTANT_MAX)
    y = parent.y + generate_random_between(MUTANT_MIN, MUTANT_MAX)
    z = parent.x + generate_random_between(MUTANT_MIN, MUTANT_MAX)

    return Solution(x, y, z)


def generate_population_of_solutions():
    """ Generate a number of random solutions and sort them by best first """
    solutions = []

    for i in range(1, POPULATION_NUMBER):
        solution = generate_random_solution()
        res = solution.test_solution()
        solutions.append((solution, res))

    return sorted(solutions, key = lambda j: j[1])


def generate_population_of_mutant_solutions(parent):
    """ Get a parent and produce mutant children solutions """
    solutions = []

    for i in range(1, POPULATION_NUMBER):
        solution = generate_random_mutant_solution(parent)
        res = solution.test_solution()
        solutions.append((solution, res))

    return sorted(solutions, key = lambda j: j[1])


def select_the_best_mutant(solutions):
    """ Return the best solution, to be used as parent for a new
        generation of mutant solutions.
    """
    return solutions[0][0]


def list_solutions(solutions):
    """ Human readable format
    """
    res = ""
    for s in solutions:
        res += s[0].human_readable()

    print(res)


def main():
    print("==================================================================")
    print("Inteligenta artificiala: Algoritmi evolutivi.")
    print("==================================================================")
    print("Gasim o solutie pentru 3*x + 2*y + z = 15")
    print("------------------------------------------------------------------")
    print("Mai intai generam {} solutii la intamplare si le sortam.".format(
            POPULATION_NUMBER
        ))
    print("Cele mai bune vor fi primele.")

    solutions = generate_population_of_solutions()
    list_solutions(solutions)

    parent = solutions[0][0]
    print("Cea mai buna solutie gasita este: x={}, y={}, z={}".format(
        parent.x, parent.y, parent.z
        ))

    print("3*{} + 2*{} + {} = {}, eroarea fiind {}".format(
        parent.x, parent.y, parent.z,
        3 * parent.x + 2 * parent.y + parent.z,
        solutions[0][1]))

    print("Vom lansa populatii de mutanti, selectand mereu pe cel mai bun.")
    mutant_generations = 0

    while True:
        mutant_generations += 1

        print("---- GENERATIA DE MUTANTI: {}".format(mutant_generations))
        solutions = generate_population_of_mutant_solutions(parent)
        list_solutions(solutions)

        parent = select_the_best_mutant(solutions)
        print("Cea mai buna solutie gasita este: x={}, y={}, z={}".format(
            parent.x, parent.y, parent.z
            ))

        print("3*{} + 2*{} + {} = {}, eroarea fiind {}".format(
            parent.x, parent.y, parent.z,
            3 * parent.x + 2 * parent.y + parent.z,
            solutions[0][1]))

        if solutions[0][1] <= ACCEPTED_ERROR:
            break


if __name__ == '__main__':
    main()
