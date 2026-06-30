import openhtf as htf
import serial



# build hardware plug
class MicrocontrollerPlug(htf.plugs.BasePlug):
    """Abstracts communication with the embedded device under tests"""
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    def read_voltage_pin(self) -> float:
        self.ser.write(b'GET_VOLTAGE\n')
        response = self.ser.readline().decode().strip()
        return float(response)

    def close(self):
        self.ser.close()


# define test phases and measurements
@htf.measures(
    htf.Measurement("rail_3v3_voltage")
    .in_range(3.0, 3.6)
    .with_units("V")
)
@htf.plug(dut=MicrocontrollerPlug)
def test_power_rail(test, dut):
    measured_voltage = dut.read_voltage_pin()
    test.measurements.rail_3v3_voltage = measured_voltage


# orchestrate and execute the test
def main():
    my_test = htf.Test(test_power_rail)
    my_test.execute(test_start_trigger=lambda: input("Scan/Enter DUT Serial Number: "))


if __name__ == "__main__":
    main()
