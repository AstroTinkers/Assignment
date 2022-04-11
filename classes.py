class Car:
    def __init__(self, data):
        self.model, self.plate, self.color, self.vin, self.part_price = data.split(", ")
        self.vin = int(self.vin)
        self.part_price = float(self.part_price) * 1.2
