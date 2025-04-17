# class
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery_level = 100  

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}")
        self.battery_level -= 5

    def use_app(self, app_name):
        print(f"Using {app_name} on {self.brand} {self.model}")
        self.battery_level -= 15

    def charge(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} is fully charged")

    def show_battery(self):
        print(f"Battery level: {self.battery_level}%")

# Subclass
class GamingPhone(Smartphone):
    def use_app(self, app_name):
        print(f"Launching for {app_name}")
        self.battery_level -= 20 

    def activate_cooling_system(self):
        print(f"Cooling system activated for intense gaming")


# Example usage
def main():
    phone1 = Smartphone("Iphone", "13")
    phone2 = GamingPhone("ASUS", "ROG Phone 7")

    phone1.use_app("google")
    phone1.show_battery()

    phone2.use_app("PUBG Mobile")
    phone2.activate_cooling_system()
    phone2.show_battery()


if __name__ == "__main__":
    main()
