def mean(data):
    return sum(data)/len(data)

def median(data):
    data.sort()
    if len(data) % 2 == 0:
        median1 = data[len(data)//2 - 1]
        median2 = data[len(data)//2]
        return (median1 + median2)/2
    else:
        return data[len(data)//2]

def mode(data):
    data_frequency = {}
    for i in data:
        if i in data_frequency:
            data_frequency[i] += 1
        else:
            data_frequency[i] = 1
    mode = max(data_frequency, key=data_frequency.get)
    return mode

n=int(input("Enter the number of data variables:"))
data=[]
for i in range(0,n) :
    ele=int(input())
    data.append(ele)

print("Mean: ", mean(data))
print("Median: ", median(data))
print("Mode: ", mode(data))
