
import unittest
from datetime import datetime
from engine.model.calliope import Calliope

class TestCalliope(unittest.TestCase):
    def setUp(self):
        today = datetime.today().date()
        self.last_service_date_3_years_ago = today.replace(year=today.year - 3)
        self.last_service_date_1_year_ago = today.replace(year=today.year - 1)
        self.current_mileage_30001 = 30001
        self.current_mileage_0 = 0
        self.last_service_mileage_0 = 0

    def test_battery_should_be_serviced(self):
        car = Calliope(self.last_service_date_3_years_ago, self.current_mileage_0, self.last_service_mileage_0)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = Calliope(self.last_service_date_1_year_ago, self.current_mileage_0, self.last_service_mileage_0)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = Calliope(datetime.today().date(), self.current_mileage_30001, self.last_service_mileage_0)
        self.assertTrue(car.needs_service())

if __name__ == "__main__":
    unittest.main()
