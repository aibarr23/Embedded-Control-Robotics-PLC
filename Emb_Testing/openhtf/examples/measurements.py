import os.path
import random

import openhtf as htf
from openhtf.output.callbacks import json_factory
from openhtf.util import validators

@htf.measures(htf.Measurement('hello_world_measurement'))
def hello_phase(test):
    test.measurements.hello_world_measurement = 'Hello!'

@htf.measures('hello_again_measurement')
def again_phase(test):
    test.measurements.hello_again_measurement = 'Again!'

@htf.measures('first_measurement', 'second_measurement')
@htf.measures(htf.Measurement('third'), htf.Measurement('fourth'))
def lots_of_measurements(test):
    test.measurements.first_measurement = 'First!'
    test.measurements['second_measurement'] = 'Second :('

    for measurement in ('third', 'fourth'):
        test.measurements[measurement] = measurement + ' is the best!'

@htf.measures(
    htf.Measurement('validated_measurement')
    .in_range(0, 10)
    .doc('This is measurement is validatted.')
    .with_units(htf.units.SECOND)
)
def measure_seconds(test):
    test.measurements.validated_measurement = 5

@htf.measures(
    'inline_kwargs',
    docstring='This measurement is declared inline!',
    units=htf.units.HERTZ,
    validators=[validators.in_range(0,10)],
)
@htf.measures('another_inline', docstring='Because why not?')
def inline_phase(test):
    """Phase that declares a measurements validators as a keyword argument."""
    test.measurements.inline_kwargs = 15
    test.measurements.another_inline = 'This one is unvalidated'
    test.logger.info('Set inline_kwargs to a failing value, test should FAIL!')

@htf.measures(
    htf.Measurement('power_time_series').with_dimensions('ms', 'V', 'A')
)
@htf.measures(htf.Measurement('average_voltage').with_units('V'))
@htf.measures(htf.Measurement('average_current').with_units('A'))
@htf.measures(htf.Measurement('resistance').with_units('ohm').in_range(9, 11))
def multdim_measurements(test):
    """Phase with a multidimensional emasurement."""
    
    for t in range(10):
        resistance = 10
        voltage = 10 + 10.0 * t
        current = voltage / resistance + 0.01 * random.random()
        dimensions = (t, voltage, current)
        test.measurements['power_time_series'][dimensions] = 0

    dim_measured_value = test.measurements['power_time_series']
    
    power_df = dim_measured_value.to_dataframe(columns=['ms', 'V', 'A', 'n/a'])
    test.logger.info('This is what a dataframe looks like:\n%s', power_df)
    test.measurements['average_voltage'] = power_df['V'].mean()

    power_array = power_df.to_numpy()
    test.logger.info('This is the same data in a numpy array:\n%s', power_array)
    test.measurements['average_current'] = power_array.mean(axis=0)[2]

    test.measurements['resistance'] = (
        test.measurements['average_voltage']
        / test.measurements['average_current']
    )


@htf.measures(
    htf.Measurement('resistance')
    .with_units('ohm')
    .in_range(minimum=5, maximum=17, marginal_minimum=9, marginal_maximum=11)
)
def marginal_measurements(test):
    """Phase with a marginal measurement"""
    test.measurements.resistance = 13


def create_and_run_test(output_dir: str = '.'):
    test = htf.Test(
        hello_phase,
        again_phase,
        lots_of_measurements,
        measure_seconds,
        inline_phase,
        multdim_measurements,
    )

    test.add_output_callbacks(
        json_factory.OutputToJSON(
            os.path.join(output_dir, 'measurements.json'), indent=2
        )
    )

    test.execute(test_start=lambda: 'MyDutId')

if __name__ == '__main__':
    create_and_run_test()
