import json
import numpy as np
import sys

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

if len(sys.argv) < 2:
    print("Usage: python3 statistics.py <path_to_dataset>.json")
    print("Options: -f include filling=true datapoints")
    exit()

dataset_file = open(sys.argv[1],)

dataset = json.load(dataset_file)

#to create a matrix according to the level of water init a dictionary
dataset_matrix = {}

for datapoint in dataset:
    if len(sys.argv)>2 and sys.argv[2] == "-f":
        pass
    elif datapoint["filling"] == True:
        continue

    level = int(datapoint["level"])
    value = int(datapoint["val"])

    if dataset_matrix.get(level) == None:
        dataset_matrix[level] = eval(str(level))
        dataset_matrix[level] = []


    dataset_matrix[level].append(value)

for lvl in dataset_matrix:
    if "-m" in sys.argv:
        mean = np.mean(moving_average(dataset_matrix[lvl], 10))
        sd = np.std(moving_average(dataset_matrix[lvl], 10))
        print("Level {} -> Mean: {}, SD: {}".format(lvl, mean, sd))
    else:
        mean = np.mean(dataset_matrix[lvl])
        sd = np.std(dataset_matrix[lvl])
        print("Level {} -> Mean: {}, SD: {}".format(lvl, mean, sd))

