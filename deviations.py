import statistics
import math

def mean_deviation(data):
    mean = statistics.mean(data)
    return sum(abs(x - mean) for x in data) / len(data)

def standard_deviation(data):
    mean = statistics.mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

data = [3, 4, 5, 6, 7]
print("Mean Deviation: ", mean_deviation(data))
print("Standard Deviation: ", standard_deviation(data))
