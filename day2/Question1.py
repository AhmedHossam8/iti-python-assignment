class Vehicle:
    total_vehicles = 0
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, is_rented):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_rented = is_rented
        Vehicle.total_vehicles += 1
        
    def rent(self):
        if self.is_rented:
            print("Vehicle is already rented")
        else:
            self.is_rented = True
    
    def return_vehicle(self):
        self.is_rented = False
    
    def calculate_rental_cost(self, days):
        total = self.rental_price_per_day * days
        return total
    
    def get_details(self):
        return {
            "Vehicle ID": self.vehicle_id,
            "Brand": self.brand,
            "Model": self.model,
            "Price/Day": self.rental_price_per_day,
            "Is Rented": self.is_rented
        }

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, is_rented, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, is_rented)
        self.num_doors = num_doors
    
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 1.0
    
    def get_details(self):
        details = super().get_details()
        details["Number of Doors"] = self.num_doors
        return details
    
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, is_rented, engine_cc):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, is_rented)
        self.engine_cc = engine_cc
    
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 0.7
    
    def get_details(self):
        details = super().get_details()
        details["Engine CC"] = self.engine_cc
        return details
    
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, is_rented, cargo_capacity_tons):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, is_rented)
        self.cargo_capacity_tons = cargo_capacity_tons
    
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) * 1.5
    
    def get_details(self):
        details = super().get_details()
        details["Cargo Capacity (tons)"] = self.cargo_capacity_tons
        return details

class RentalAgency():
    pass

def main():
    car = Car("V001", "Toyota", "Camry", 50, False, 4)
    motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, False, 750)
    truck = Truck("V003", "Ford", "F-150", 80, False, 2.5)
    
    car.rent()
    print(car.is_rented)
    
    cost = car.calculate_rental_cost(5)
    print(f"Rental cost for 5 days: ${cost}")
    
    print(motorcycle.get_details())
    
    car.rent()
    
    car.return_vehicle()
    print(car.is_rented)
    
    print(f"Total vehicles: {Vehicle.total_vehicles}")
    
main()