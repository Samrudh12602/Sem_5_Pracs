import math

def harmonic_mean(data):
    return len(data) / sum(1/i for i in data)

def geometric_mean(data):
    log_sum = 0
    for i in data:
        log_sum += math.log(i)
    return math.exp(log_sum/len(data))

data = [3, 4, 5, 6, 7]
print("Harmonic Mean: ", harmonic_mean(data))
print("Geometric Mean: ", geometric_mean(data))