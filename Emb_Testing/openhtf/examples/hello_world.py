# ref: github.com/google/openhtf/blob/master/examples/hello_world.py

import os.path

import openhtf as htf
from openhtf.output.callbacks import json_factory
from openhtf.plugs import user_input


@htf.measures(htf.Measurement('hello_world_measurement'))
def hello_world(test):
    """A hello world test phase"""
    test.logger.info('Hello World!')
    test.measurements.hello_world_measurement ='Hello Again!'

def create_and_run_test(output_dir: str='.'):
    test = htf.Test(hello_world)

    test.add_output_callbacks(json_factory.OutputToJSON(os.path.join(output_dir, '{dut_id}.hello_world.json'), indent=2))
    test.execute(test_start=user_input.prompt_for_test_start())

if __name__ == '__main__':
    create_and_run_test()
