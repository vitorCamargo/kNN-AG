# ERROR -1: program entries are wrong
# ERROR -2: invalid files
# RETURN 1: finished by number of interactions

import sys
import os

import kNN
import genetic_algorithm

def read_file():
    if(len(sys.argv) != 4):
        print('\n\n---------------> ERROR: -1 <---------------')
        print('Run programm with: ')
        print('# python .\\main.py .\\training_file.txt .\\test_line.txt value_of_k\n\n')
        return -1

    if(os.path.isfile(str(sys.argv[1])) == False or os.path.isfile(str(sys.argv[2])) == False):
        print('\n\n---------------> ERROR: -2 <---------------')
        print('Invalid Files!\n\n')
        return -2

    print('\n\nProgram developed by Vitor Bueno (RA: 1921959) for Artificial Intelligence Subject at the Federal Technological University of Paraná - Câmpus Campo Mourão')
    print('§§§§§§§§§§§ k-NN and Genetic Algorithms §§§§§§§§§§§\n\n')

    k = int(sys.argv[3])
    training_file = open(str(sys.argv[1]), 'r')
    test_file = open(str(sys.argv[2]), 'r')

    training_schema = []
    line_file_training = training_file.readline()
    while line_file_training:
        array_float = [float(i) for i in line_file_training.rstrip('\n\r').split(' ')]
        training_schema.append(array_float)
        line_file_training = training_file.readline()

    test_schema = []
    line_file_test = test_file.readline()
    while line_file_test:
        array_float = [float(i) for i in line_file_test.rstrip('\n\r').split(' ')]
        test_schema.append(array_float)
        line_file_test = test_file.readline()

    return training_schema, test_schema, k


def main():
    training_schema, test_schema, k = read_file()

    genetic_algorithm.main(training_schema, test_schema, k)
    # kNN.main(training_schema, test_schema, k)

main()