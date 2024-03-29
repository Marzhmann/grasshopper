'''
component inputs:
    buildings_number
    start_floor_range
    end_floor_range
    density
    fprints_area
    iterations
    recompute
component outputs:
    best_floors_match
    result_densities
    best_seed
    best_iter_index
    best_match_density  
'''
import random

x = 0
result_densities = []
seeds = []
floors_list = []

if density<3:
    end_floor_range = 4
elif density>3 and density<6:
    end_floor_range = 7
elif density>11:
    start_floor_range = 9

for i in range(iterations):
    s = random.random()
    seeds.append(s)
    random.seed(s)
    randomlist = []

    for i in range(buildings_number):
        n = random.randint(start_floor_range,end_floor_range)
        randomlist.append(n)

    floors_list.append(randomlist)
    products = []

    for num1, num2 in zip(randomlist, fprints_area):
        products.append(num1 * num2)

    density_c = sum(products)/sum(fprints_area)
    result_densities.append(density_c)


closest_seed = min(result_densities, key = lambda x: abs(x - density))


best_iter_index = result_densities.index(closest_seed)
best_floors_match = floors_list[best_iter_index]
best_seed = seeds[best_iter_index]
best_match_density = result_densities[best_iter_index]
