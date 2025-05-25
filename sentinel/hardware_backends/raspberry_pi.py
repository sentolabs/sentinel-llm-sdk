# Raspberry Pi handler
class RaspberryPiBackend:
    def initialize(self):
        print("Initializing Raspberry Pi backend")

    def read_sensor(self, sensor_id):
        return f"Sensor {sensor_id} data from Raspberry Pi"