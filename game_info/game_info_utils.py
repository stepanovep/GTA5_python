car_collection = []

with open('car_collections.txt', 'r') as f:
    for line in f:
        car_collection.append(line.strip().lower())


print(car_collection.__contains__('widebod'.lower()))
