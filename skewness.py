import statistics
import math

def skewness(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    standard_deviation = statistics.stdev(data)
    skewness = 3 * (mean - median) / standard_deviation
    return skewness

data = [3, 4, 3, 6, 7]
print("Skewness Coefficient: ", skewness(data))
