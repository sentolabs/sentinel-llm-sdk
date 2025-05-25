# Arduino handler
class ArduinoBackend:
    def initialize(self):
        print("Initializing Arduino backend")

    def read_sensor(self, sensor_id):
        return f"Sensor {sensor_id} data from Arduino"