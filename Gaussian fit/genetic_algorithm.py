import matplotlib.pyplot as plt
import pygad
import pandas
from statistics import get_p_value


last_fitness = pandas.read_csv("input_data.csv")
num_generations = 50
num_parents_mating = 3
sol_per_pop = 10
num_genes = 12


def fitness_func(solution, solution_id):
    return get_p_value(solution)


def on_generation(ga_instance):
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    last_fitness = ga_instance.best_solution(pop_fitness=ga_instance.last_generation_fitness)[1]
    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
    print()
    sol_df = pandas.DataFrame(solution)
    sol_df.to_csv('best_solution.csv')
    sol_df.plot.kde()
    plt.legend(['solution'])
    plt.savefig('best_solution.jpg')


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       fitness_func=fitness_func,
                       on_generation=on_generation)
ga_instance.run()
