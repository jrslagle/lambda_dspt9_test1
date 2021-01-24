
class Car():
    def __init__(self, mpg=30, tank_size_gallons=12):
        """
        Create a new car.

        :param mpg: how many miles per gallon this car has, by default 30.
        :param tank_size_gallons: the max gallons the tank can hold, by default 12.
        :variable odometer: the number of miles the car has driven, initially 0.
        :variable gallons_left: the number of gallons left in the tank, initially tank_size_gallons.
        """
        self.mpg = mpg
        self.tank_size_gallons = tank_size_gallons
        self.odometer = 0
        self.gallons_left = tank_size_gallons

    def drive(self, miles):
        """
        Drive the car.

        :param miles: number of miles to drive the car
        :returns: a string describing how many miles were driven and 
            how many gallons are left in the tank
        """
        if self.gallons_left <= 0:
            assert False, "You are out of gas and cannot drive"
        else:
            fuel_needed = miles / self.mpg
            if fuel_needed <= self.gallons_left:
                self.gallons_left -= fuel_needed
                self.odometer += miles
                return(
                    f'You went {miles} miles and have {self.gallons_left:.1f} gallons of fuel left.')
            else:
                distance_possible = self.mpg * self.gallons_left
                self.gallons_left = 0
                self.odometer += distance_possible
                return(
                    f'You only went {distance_possible:.1f} miles and then ran out of gas.')

    def refuel(self, add_gallons):
        """
        Refuel the car.

        :param add_gallons: number of gallons to add to the tanks
        :returns: a string describing how many gallons are now in the tank
        """
        if add_gallons >= 0:
            if (self.gallons_left + add_gallons) > self.tank_size_gallons:  # too much fuel
                self.gallons_left = self.tank_size_gallons
            else:
                self.gallons_left += add_gallons
            return f"Refueled the tank to {self.gallons_left} gallons."
        else:
            return f"Adding {add_gallons} gallons to the tank makes no sense."


if __name__ == '__main__':
    my_car = Car(mpg=30, tank_size_gallons=12)
    while my_car.gallons_left > 0:
        my_car.drive(50)
    my_car.refuel(14)
    while my_car.gallons_left > 0:
        my_car.drive(30)
