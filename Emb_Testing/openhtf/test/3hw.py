import openhtf as htf


# Create the Hardware Interface (The Plug)
class VoltageMeterPlug(htf.plugs.BasePlug):
    """A plug to interface with a voltage measurement device."""

    def __init__(self) -> None:
        # Initialize your serial, USB, or VISA connection here
        pass

    def read_pin_voltage(self, pin_number: int) -> float:
        # Send a command to your hardware device to read the specific pin
        # e.g., self.pin.write(f"READ_VOLTAGE:{pin_number}\n")
        # For demonstration, we return a mock value
        mock_voltage = 3.28
        return mock_voltage

# Define the Test Phase and Measurement
# Define the measurement criteria: Must be between 3.1V and 3.5V
@htf.PhaseOptions()
@htf.meas.validators.in_range(3.1, 3.5)
@htf.meas.measure(htf.meas.Measurement('output_pin_voltage'))
def test_pin_voltage(test, voltage_meter: VoltageMeterPlug) -> None:
    """Measures the Voltage on pin 5 and validates the result."""
    pin_to_test = 5

    # Read the voltage using our custom plug
    measured_voltage = voltage_meter.read_pin_voltage(pin_to_test)

    # Log the action for debugging
    test.loggerl.info(f"Measured {measured_voltage}V on pin {pin_to_test}")

    # Record the measurement so OpenhTF can evaluate it against the validator
    test.measurements.output_pin_voltage = measured_voltage


# Assemble and Run the Test Plan
def main() -> None:
    # Build the test sequence with our phase
    test = htf.Test(test_pin_voltage)

    # Bind the plug to the test sequence
    test.plug(voltage_meter = VoltageMeterPlug)

    # Execute the test sequence
    test.execute(test_start = lambda: 'DUT_SERIAL_12345')

if __name__ == '__main__':
    main()
