from Assignement import classes
import pandas

car_class = classes.Car
cars = []
while True:
    input_data = input("Please enter car data or 'q' to stop: ")
    if input_data == 'q':
        break
    else:
        cars.append(car_class(input_data))
print(cars)