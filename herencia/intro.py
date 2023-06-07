class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TackedVehicle]:
        print(issubclass(cls1,cls2), end="\t")
    print()