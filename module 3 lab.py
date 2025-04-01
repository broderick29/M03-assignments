"""
Broderick Clapper
Python Vehicle app

This assignment is an app that contains a super class called vehicle and a class called automobile that has different vechice attributes."
The app accept a users input for a car and then asks for year, make, model, doors, and roof type. The app then gives the information in an easy to read format"
"""
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"Vehichle type: {self.vehicle_type}"

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Year: {self.year}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Doors: {self.doors}\n"
                f"Roof: {self.roof}")
def get_car_details():
    print("Enter car inforamtion")
    year = int(input("Enter vehicle year: "))
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")

    while True:
        try:
            doors = int(input("Enter the number of doors (2 or 4): "))
            if doors in [2, 4]:
                break
            else:
                print("Invalid number of doors. Enter 2 or 4.")
        except ValueError:
            print("Invalid input, put a number.")
    while True:
        roof = input("Enter roof type (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        else:
            print("Invalid roof type")

    return Automobile(year, make, model, doors, roof)

def main():
    car = get_car_details()
    print("\nCar Details:")
    print(car)


if __name__ == "__main__":
    main()



