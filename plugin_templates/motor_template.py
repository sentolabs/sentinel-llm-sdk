# Motor template plugin
class MotorTemplate:
    def __init__(self):
        pass

    def control(self, speed):
        raise NotImplementedError("Subclasses must implement this method")