import pandas as pd


class Car:
    """Create an instance of each car with its assigned attributes"""
    def __init__(self, data):
        self.model, self.plate, self.color, self.vin, self.part_price = data.split(", ")
        self.part_price = float(self.part_price) * 1.2


def initial_cars_data():
    cars = []
    print("Please enter car data or 'Stop' to stop:")
    while True:
        input_data = input()
        if input_data == 'Stop':
            break
        else:
            try:
                cars.append(Car(input_data))
            except ValueError:
                print("Invalid input, please enter car data or 'Stop' to stop:")
        continue
    return cars


def car_data_creator(cars_list):
    car_data = {"Manufacturer": [], "Plate Nº": [], "VIN": [], "Part Price": []}
    for car in cars_list:
        car_data["Manufacturer"].append(car.model)
        car_data["Plate Nº"].append(car.plate)
        car_data["VIN"].append(car.vin)
        car_data["Part Price"].append(car.part_price)
    return pd.DataFrame(car_data)


def output_selection(file):
    while True:
        print("Please select your output format:\n1).csv\n2).json\n3).parquet")
        input_selection = input()
        if input_selection == "1":
            file.to_csv(path_or_buf='cars.csv', index=False)
            break
        elif input_selection == "2":
            file.to_json(path_or_buf='cars.json')
            break
        elif input_selection == "3":
            file.to_parquet('cars.parquet', index=False)
            break
        else:
            print("Invalid selection. Please choose from the options below.")
            print("Please select your output format:\n1).csv\n2).json\n3).parquet")
            continue


def open_file():
    try:
        file_to_open = pd.read_csv('cars.csv')
    except FileNotFoundError:
        try:
            file_to_open = pd.read_json('cars.json')
        except ValueError:
            file_to_open = pd.read_parquet('cars.parquet')
    return file_to_open


def most_common(data_file):
    return data_file['Manufacturer'].value_counts().idxmax()


def least_common(data_file):
    return data_file['Manufacturer'].value_counts().idxmin()


def most_expensive(data_file):
    return max(data_file['Part Price'])


def cheapest(data_file):
    return min(data_file['Part Price'])


def total_sum(data_file):
    return data_file['Part Price'].sum()


def most_plates(data_file):
    data_file['Plate Nº'] = data_file['Plate Nº'].str[:2]
    return data_file['Plate Nº'].value_counts().idxmax()


def least_plates(data_file):
    data_file['Plate Nº'] = data_file['Plate Nº'].str[:2]
    return data_file['Plate Nº'].value_counts().idxmin()


def statistics(dataframe_file):
    while True:
        print("Please select the desired statistic or type 'Stop' to exit:")
        print("1) Most common car\n2) Least common car\n3) Most expensive car part\n4) Cheapest car part"
              "\n5) Sum of car parts\n6) Most plates from a city\n7) Least plates from a city")
        command = input()
        if command == '1':
            print(f"Most common car: {most_common(dataframe_file)}")
            continue
        elif command == '2':
            print(f"Least common car: {least_common(dataframe_file)}")
            continue
        elif command == '3':
            print(f"Most expensive car part: {most_expensive(dataframe_file):.2f}")
            continue
        elif command == '4':
            print(f"Cheapest car part: {cheapest(dataframe_file):.2f}")
            continue
        elif command == '5':
            print(f"Total sum of parts: {total_sum(dataframe_file):.2f}")
        elif command == '6':
            print(f"Most plates from city: {most_plates(dataframe_file)}")
            continue
        elif command == '7':
            print(f"Least plates from city: {least_plates(dataframe_file)}")
            continue
        elif command == 'Stop':
            break
        else:
            print("Invalid command. Please select from the options below:")
            continue
