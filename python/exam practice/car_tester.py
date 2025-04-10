from car import Car

car_file = []

with open ("cars.txt") as file: 
    for line in file:
        line = line.strip().split()
        color, engine_type, gas_tank, odometer = line[0], line[1], int(line[2]), int(line[3])
        car = Car(color, engine_type, gas_tank, odometer)
        car_file.append(car)

car_type1 = car_file[0]
print(car_type1)

print(car_type1.get_gas_tank())