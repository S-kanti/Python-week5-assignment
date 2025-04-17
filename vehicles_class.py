# Base class (optional in this case)
class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")


# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving")


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing")


# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")


# Main program
def main():
    # Create a list of different vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Loop through and call move on each one
    for vehicle in vehicles:
        vehicle.move()


# Run the main function
if __name__ == "__main__":
    main()
