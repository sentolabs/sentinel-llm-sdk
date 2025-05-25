# Servo template plugin
class ServoTemplate:
    def __init__(self):
        pass

    def control(self, angle):
        raise NotImplementedError("Subclasses must implement this method")