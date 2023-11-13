# vehciledata/tests/test_main.py
import unittest
from vehicledata.details import getChallan, get_vehicle_details , getvehicle

class TestMainFunctions(unittest.TestCase):

    def test_getChallan(self):
        print(getChallan("DL8CX5463"))
        print(getChallan("DL8CX5463"))
        pass

    def test_get_vehicle_details(self):
        print(get_vehicle_details("DL8CX5463"))
        print(get_vehicle_details("DL8CX5463"))
        
        pass
    
    def test_getvehicle(self):
        print(getvehicle("DL8CX5463"))
       
        pass


if __name__ == '__main__':
    unittest.main()
