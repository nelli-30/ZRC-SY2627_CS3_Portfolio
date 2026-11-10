from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")

class TempSensor(Sensor):
    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")

# Running the Lab Inventory System (Success Run)
print("--- Lab Inventory System ---")
ph_sensor = PHSensor()
ph_sensor.get_reading()

temp_sensor = TempSensor()
temp_sensor.get_reading()
print("----------------------------")

my_sensor = Sensor()