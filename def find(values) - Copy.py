def find(values):   
    minimum = min(values)
    maximum = max(values)
    avg = sum(values)/ len(values)
    return minimum, maximum, avg
numbers = [10,34,54,67,84,48]
minimum, maximum, avg = find(numbers)
print("minimum=", minimum)
print("maximum=", maximum)
print("average=", avg)