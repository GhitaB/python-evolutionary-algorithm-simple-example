import random

MIN = -1000
MAX = 1000
MUTANT_MIN = -10
MUTANT_MAX = 10
ACCEPTED_ERROR = 0
POPULATION_NUMBER = 50


def generate_random_between(min, max):
    """ Return a random int between min and max """
    return random.randint(min, max)


def generate_random_solution():
    """ Return a random solution (x, y, z) """
    x = generate_random_between(MIN, MAX)
    y = generate_random_between(MIN, MAX)
    z = generate_random_between(MIN, MAX)

    return (x, y, z)


def generate_random_mutant_solution(parent):
    """ Return a random mutant solution based on given (x, y, z) """
    x = parent[0] + generate_random_between(MUTANT_MIN, MUTANT_MAX)
    y = parent[1] + generate_random_between(MUTANT_MIN, MUTANT_MAX)
    z = parent[2] + generate_random_between(MUTANT_MIN, MUTANT_MAX)

    return (x, y, z)


def test_solution(x, y, z):
    """ Test how good a solution is. 0 means perfect, 1 = almost there. """
    a = 3 * x + 2 * y + z

    return abs(a-15)


def generate_population_of_solutions():
    """ Generate a number of random solutions and sort them by best first """
    solutions = []

    for i in range(1, POPULATION_NUMBER):
        x, y, z = generate_random_solution()
        res = test_solution(x, y, z)
        solutions.append(((x, y, z), res))

    return sorted(solutions, key = lambda j: j[1])


def generate_population_of_mutant_solutions(parent):
    """ Get a parent and produce mutant children solutions """
    solutions = []

    for i in range(1, POPULATION_NUMBER):
        x, y, z = generate_random_mutant_solution(parent)
        res = test_solution(x, y, z)
        solutions.append(((x, y, z), res))

    return sorted(solutions, key = lambda j: j[1])


def select_the_best_mutant(solutions):
    """ Return the best solution, to be used as parent for a new
        generation of mutant solutions.
    """
    return solutions[0][0]


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
    print(solutions)

    parent = solutions[0][0]
    print("Cea mai buna solutie gasita este: x={}, y={}, z={}".format(
        parent[0], parent[1], parent[2]
        ))

    print("3*{} + 2*{} + {} = {}, eroarea fiind {}".format(
        parent[0], parent[1], parent[2],
        3 * parent[0] + 2 * parent[1] + parent[2],
        solutions[0][1]))

    print("Vom lansa populatii de mutanti, selectand mereu pe cel mai bun.")
    mutant_generations = 0

    while True:
        mutant_generations += 1

        print("---- GENERATIA DE MUTANTI: {}".format(mutant_generations))
        solutions = generate_population_of_mutant_solutions(parent)
        print(solutions)

        parent = select_the_best_mutant(solutions)
        print("Cea mai buna solutie gasita este: x={}, y={}, z={}".format(
            parent[0], parent[1], parent[2]
            ))

        print("3*{} + 2*{} + {} = {}, eroarea fiind {}".format(
            parent[0], parent[1], parent[2],
            3 * parent[0] + 2 * parent[1] + parent[2],
            solutions[0][1]))

        if solutions[0][1] <= ACCEPTED_ERROR:
            break


if __name__ == '__main__':
    main()
