from openhtf.plugs import BasePlug

class MultimeterPlug(BasePlug):
    # Simulate connecting to the multimeter
    def __init__(self):
        self.connected = True

    # Simulate measuring the voltage
    def measure_voltage(self):
        return 3.3

    # Simulate disconnecting from the multimeter
    # Called automatically by OpenHTF at test end
    def tearDown(self):
        self.connected = False
