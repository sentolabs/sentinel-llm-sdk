# Command routing logic
class CommandRouter:
    def route(self, command):
        if command.startswith("motor"):
            return "MotorControlPlugin"
        elif command.startswith("servo"):
            return "ServoControlPlugin"
        else:
            return "UnknownCommand"