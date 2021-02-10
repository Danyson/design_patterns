from abc import ABC, abstractmethod

class Tyre(ABC):
    @abstractmethod
    def size(self):
        pass

class CarTyre(Tyre):
    def size(self):
        return 25

class BikeTyre(Tyre):
    def size(self):
        return 20

class TyreFactory(ABC):
    @abstractmethod
    def get_tyre_size(self):
        pass

class CarTyreFactory(TyreFactory):
    def get_tyre_size(self):
        self.carTyre = CarTyre()
        return self.carTyre.size()

class BikeTyreFactory(TyreFactory):
    def get_tyre_size(self):
        self.bikeTyre = BikeTyre()
        return self.bikeTyre.size()

class TyreProducer:
    def get_tyre_factory(self, typeOfVehicle):
        if ( typeOfVehicle == 'car' ):
            return CarTyreFactory()
        elif (typeOfVehicle == 'bike' ):
            return BikeTyreFactory()

tyre = TyreProducer()
carTyre = tyre.get_tyre_factory('car')
bikeTyre = tyre.get_tyre_factory('bike')

print(f'car tyre size is {carTyre.get_tyre_size()}')
print(f'bike tyre size is {bikeTyre.get_tyre_size()}')
