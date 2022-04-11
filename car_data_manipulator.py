import pandas as pd
import classes

car_class = classes.Car
cars = []
print("Please enter car data or 'Stop' to stop:")
while True:
    input_data = input()
    if input_data == 'Stop':
        break
    else:
        try:
            cars.append(car_class(input_data))
        except ValueError:
            print("Invalid input, please enter car data or 'Stop' to stop:")

car_data = {"Manufacturer": [], "Plate Nº": [], "VIN": [], "Part Price": []}
for car in cars:
    car_data["Manufacturer"].append(car.model)
    car_data["Plate Nº"].append(car.plate)
    car_data["VIN"].append(car.vin)
    car_data["Part Price"].append(car.part_price)
file_to_write = pd.DataFrame(car_data)

while True:
    print("Please select your output format:\n1).csv\n2).json\n3).parquet")
    output_select = input()
    if output_select == "1":
        file_to_write.to_csv(path_or_buf='cars.csv', index=False)
        break
    elif output_select == "2":
        file_to_write.to_json(path_or_buf='cars.json')
        break
    elif output_select == "3":
        file_to_write.to_parquet('cars.parquet', index=False)
        break
    else:
        print("Invalid selection. Please choose from the options below.")
        continue

try:
    work_file = pd.read_csv('cars.csv')
except FileNotFoundError:
    work_file = pd.read_json('cars.json')
except FileNotFoundError:
    work_file = pd.read_parquet('cars.parquet')

work_file = pd.DataFrame(work_file)
work_file = work_file.sort_values(by="Manufacturer", ignore_index=True)
print(work_file.head())
print(work_file.tail())
print(f"Most common car: {work_file['Manufacturer'].value_counts().idxmax()}")
print(f"Most expensive part: {max(work_file['Part Price']):.2f}")
print(f"Total sum of VIN: {work_file['VIN'].sum()}")
print(f"Total sum of parts: {work_file['Part Price'].sum():.2f}")
