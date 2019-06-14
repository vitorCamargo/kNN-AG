import sys
import random

import kNN

NUMBER_STOPOVER = 100
POPULATION_RATE = 0.01
MUTATION_RATE = 0.01

best_in_history = None

def random_population(number_features):
    return [random.randint(0, 1) for i in range(number_features)]

def selection_cross(table_population, random_number):
    parent_elements = table_population[0:2]

    first_cross = parent_elements[0]['features'][0:random_number]
    first_cross.extend(parent_elements[1]['features'][random_number:])

    second_cross = parent_elements[1]['features'][0:random_number]
    second_cross.extend(parent_elements[0]['features'][random_number:])

    return [parent_elements[0]['features'], first_cross, second_cross]

def mutation(table_population):
    random_element_index = random.randint(0, len(table_population) - 1)
    random_feature_index = random.randint(0, len(table_population[random_element_index]) - 1)

    value = table_population[random_element_index][random_feature_index]
    if(value == 0):
        table_population[random_element_index][random_feature_index] = 1
    else:
        table_population[random_element_index][random_feature_index] = 0

    return table_population

def main(training_schema, test_schema, k, genetic_features = [], count = 0, max = NUMBER_STOPOVER):
    global best_in_history
    stopover_max = max
    features = genetic_features
    number_features = len(test_schema[0]) - 1

    number_mutation = round(len(test_schema) * MUTATION_RATE)
    number_population = round(len(test_schema) * POPULATION_RATE)
    if(number_population <= 3):
        number_population = 3

    table_population = []

    if(count == max):
        response = 'not_aneta'

        while(response != 'n' and response != 'y'):
            response = input('\n\nYou got {} interactions, would you like to go on? [y/n]: '.format(count))

            if(response == 'y'):
                stopover_max += NUMBER_STOPOVER
            if(response == 'n'):
                return 1

    if(len(genetic_features) == 0):
        features = [random_population(number_features) for i in range(number_population)]
    
    print('\n\n\n\n@@ Generation {}:'.format(count + 1))
    for indexPopulation in range(number_population):
        print(features[indexPopulation])
        time, percentage = kNN.main(training_schema, test_schema, k, features[indexPopulation])
        
        table_population.append({
            'percentage': percentage,
            'features': features[indexPopulation]
        })

        print('@@ Time: {}sec \n@@ Correct Percentage: {}%\n\n'.format(time, percentage))
    
    table_population.sort(key = lambda item: item['percentage'], reverse = True)

    if(best_in_history != None):
        if(best_in_history['percentage'] < table_population[0]['percentage']):
            best_in_history = table_population[0]
    else:
        best_in_history = table_population[0]
    
    print('\n\n########## BEST IN HISTORY:')
    print(best_in_history['features'])
    print('## Correct Percentage: {}%'.format(best_in_history['percentage']))

    new_genetic_features = selection_cross(table_population, random.randint(0, number_features))
    new_genetic_features.extend(random_population(number_features) for i in range(number_population - len(new_genetic_features)))

    for _ in range(number_mutation):
        new_genetic_features = mutation(new_genetic_features)

    main(training_schema, test_schema, k, new_genetic_features, count + 1, stopover_max)
