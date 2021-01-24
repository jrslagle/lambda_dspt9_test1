import unittest
from lambdata_james_slagle.car import Car


class Car_Test(unittest.TestCase):
    def setUp(self):
        self.go_cart = Car(mpg=10, tank_size_gallons=2)  # go cart

    def test_init(self):
        self.assertEqual(self.go_cart.mpg, 10)
        self.assertEqual(self.go_cart.tank_size_gallons, 2)
        self.assertEqual(self.go_cart.odometer, 0)
        self.assertEqual(self.go_cart.gallons_left, 2)

    def test_drive(self):
        # Fill the tank
        fuel_before = self.go_cart.gallons_left
        fuel_needed_to_fill = self.go_cart.tank_size_gallons - self.go_cart.gallons_left
        self.go_cart.refuel(add_gallons=fuel_needed_to_fill)

        # Use half the tank
        distance_to_half = (self.go_cart.gallons_left * self.go_cart.mpg) / 2
        self.go_cart.drive(miles=distance_to_half)
        fuel_after = self.go_cart.gallons_left
        half_tank = self.go_cart.tank_size_gallons / 2
        self.assertEqual(fuel_after, half_tank)

        # Put it back the way you found it
        self.go_cart.gallons_left = fuel_before

    def test_refuel(self):
        fuel_before = self.go_cart.gallons_left

        # test if adding -10 gallons works
        result = self.go_cart.refuel(add_gallons=-10)
        expected = f"Adding -10 gallons to the tank makes no sense."
        self.assertEqual(result, expected)

        # test if adding 0 gallons works
        result = self.go_cart.refuel(add_gallons=0)
        expected = f"Refueled the tank to {self.go_cart.gallons_left} gallons."
        self.assertEqual(result, expected)

        # test if filling mid way works
        self.go_cart.gallons_left = 0
        half_tank = self.go_cart.tank_size_gallons / 2
        result = self.go_cart.refuel(add_gallons=half_tank)
        expected = f"Refueled the tank to {half_tank} gallons."
        self.assertEqual(result, expected)

        # test if overfilling fills to capacity
        full_tank = self.go_cart.tank_size_gallons
        result = self.go_cart.refuel(add_gallons=full_tank*2)
        expected = f"Refueled the tank to {full_tank} gallons."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()