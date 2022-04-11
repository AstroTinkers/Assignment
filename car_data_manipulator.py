import pandas as pd
import classes_and_functions

cars = classes_and_functions.initial_cars_data()
file_to_write = classes_and_functions.car_data_creator(cars)
classes_and_functions.output_selection(file_to_write)
work_file = pd.DataFrame(classes_and_functions.open_file())
work_file = work_file.sort_values(by="Manufacturer", ignore_index=True)
print(work_file.head())
print(work_file.tail())
classes_and_functions.statistics(work_file)
