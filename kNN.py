import sys
import math
import time

def main(training_schema, test_schema, k, features_allow):
    correct_attempts = 0
    wrong_attempts = 0
    start = time.time()

    for indexTest in range(len(test_schema)):
        current_test_instance = test_schema[indexTest]
        test_schema_length = len(test_schema[indexTest])
        table_kNN = []
        
        for indexTraining in range(len(training_schema)):
            current_training_instance = training_schema[indexTraining]
            current_training_instance_length = len(current_training_instance)
            euclidean_distance = 0

            for indexFeature in range(test_schema_length - 1):
                if(features_allow[indexFeature] == 1):
                    value = current_training_instance[indexFeature] - current_test_instance[indexFeature]
                    euclidean_distance += value*value

            table_kNN.append({
                'euclidean_distance': math.sqrt(euclidean_distance),
                'class': current_training_instance[current_training_instance_length - 1]
            })

        table_kNN.sort(key = lambda item: item['euclidean_distance'])

        if(k == 1):
            attempt_class = table_kNN[0]['class']
        else:
            k_near_neighbors = list(map(lambda item: item['class'], table_kNN[0:k]))
            attempt_class = max(set(k_near_neighbors), key = k_near_neighbors.count)

        if(attempt_class == current_test_instance[test_schema_length - 1]):
            correct_attempts += 1
            # print('§§Line {} - That\'s correct!!'.format(correct_attempts + wrong_attempts))
        else:
            wrong_attempts += 1
            # print('§§Line {} - You got wrong :('.format(correct_attempts + wrong_attempts))

    elapsed_time = round(time.time() - start, 2)
    attempt_percentage = (correct_attempts / (correct_attempts + wrong_attempts)) * 100

    # print('\n\n§§§§§§ Correct Attempts: {}'.format(correct_attempts))
    # print('§§§§§§ Wrong Attempts: {}'.format(wrong_attempts))
    # print('§§§§§§ Correct Attempts Percentage: {}%'.format(correct_attempts / (correct_attempts + wrong_attempts) * 100))
    # print('§§§§§§ Time: {}sec'.format(round(end - start, 2)))

    return elapsed_time, attempt_percentage
