from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Car(Engine):
    ''' assuming the car travels 15KM per Litre of Fuel'''
    def __init__(self, fuelInLitre):
        self.fuelInLitre = fuelInLitre
    def mileage(self):
        self.mileage = 15 * self.fuelInLitre
        return self.mileage

class Bike(Engine):
    ''' assuming the bike travels 50KM per Litre of Fuel'''
    def __init__(self, fuelInLitre):
        self.fuelInLitre = fuelInLitre
    def mileage(self):
        self.mileage = 50 * self.fuelInLitre
        return self.mileage


class MileageCalculatorFactory():
    def mileage_calculator(self, vehicleType, fuelInLitre):
        if ( vehicleType == 'car' ):
            car = Car(fuelInLitre)
            return car.mileage()
        elif ( vehicleType == 'bike' ):
            bike = Bike(fuelInLitre)
            return bike.mileage()

mileage = MileageCalculatorFactory()
print(f'{mileage.mileage_calculator( vehicleType = "car", fuelInLitre = 5)}KMs')
print(f'{mileage.mileage_calculator( vehicleType = "bike", fuelInLitre = 5)}KMs')
