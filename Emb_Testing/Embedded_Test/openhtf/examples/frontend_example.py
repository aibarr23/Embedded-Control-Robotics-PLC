import openhtf as htf
from openhtf.output.servers import station_server
from openhtf.output.web_gui import web_launcher
from openhtf.plugs import user_input
from openhtf.util import configuration

CONF = configuration.CONF

@htf.measures(htf.Measurement('hello_world_measurement'))
def hello_world(test):
    test.logger.info('Hello World!')
    test.measurements.hello_world_measurement = 'Hello Again!'

def main():
    CONF.load(station_server_port='4444')
    with station_server.StationServer() as server:
        web_launcher.launch('http://localhost:4444')
        for _ in range(5):
            test = htf.Test(hello_world)
            test.add_output_callbacks(server.publish_final_state)
            test.execute(test_start=user_input.prompt_for_test_start())


if __name__ == '__main__':
    main()
