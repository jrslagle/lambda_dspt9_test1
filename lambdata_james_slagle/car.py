
class Car():
    def __init__(self, mpg=30, tank_size_gallons=12):
        self.mpg = mpg
        self.tank_size_gallons = tank_size_gallons
        self.odometer = 0
        self.gallons_left = 12

    def drive(self, distance):
        if self.gallons_left <= 0:
            assert False, "You are out of gas and cannot drive"
        else:
            fuel_needed = distance / self.mpg
            if fuel_needed <= self.gallons_left:
                self.gallons_left -= fuel_needed
                self.odometer += distance
                print(
                    f'You went {distance} miles and have {self.gallons_left:.1f} gallons of fuel left.')
            else:
                distance_possible = self.mpg * self.gallons_left
                self.gallons_left = 0
                self.odometer += distance_possible
                print(
                    f'You only went {distance_possible:.1f} miles and then ran out of gas.')

    def refuel(self, add_gallons):
        if add_gallons > 0:
            if (self.gallons_left + add_gallons) > self.tank_size_gallons:  # too much fuel
                self.gallons_left = self.tank_size_gallons
            else:
                self.gallons_left += add_gallons
            print(f"Refueled the tank to {self.gallons_left} gallons.")
        else:
            assert False, f"Adding {add_gallons} gallons to the tank makes no sense."


if __name__ == '__main__':
    my_car = Car(mpg=30, tank_size_gallons=12)
    while my_car.gallons_left > 0:
        my_car.drive(50)
    my_car.refuel(14)
    while my_car.gallons_left > 0:
        my_car.drive(30)
