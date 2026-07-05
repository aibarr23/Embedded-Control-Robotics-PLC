import openhtf as htf
import can
import j1939
import queue

class J1939TestPlug(htf.plugs.BasePlug):
    def __init__(self):
        self.bus = can.interface.Bus(interface='pcan', channel='PCAN_USBBUS1', bitrate=250000)

        self.j1939_ecu = j1939.ElectronicControlUnit()
        self.j1939_ecu.connect(self.bus)

    name = j1939.Name(
        arbitrary_address_capable=0,
        industry_group=0,
        vehicle_system_instance=0,
        vehicle_system=0,
        reserved=0,
        function=0,
        function_instance=0,
        ecu_instance=0,
        manufacturer_code=0,
        identity_number=12345
    )
    self.node = j1939.Node(self.j1939_ecu, name,preferred_address=249)
    self.j1939_ecu.add_node(self.node)

    self.message_queue = queue.Queue()
    self.node.subscribe(self._on_message_received)

def _on_message_received(self, priority, pgn, source, destination, data):
    self.message_queue.put({
        'pgn': pgn,
        'source': source,
        'data': list(data)
    })


def send_request(self, target_pgn: int, destination_address: int = 0x00):
    data = [target_pgn & 0xFF, (target_pgn >> 8) & 0xFF, (target_pgn >> 16) & 0xFF]
    self.node.send_pgn(priority=6, pgn=0xEA00, source=self.node.address, destination=destination_address, data=data)

def wait_for_pgn(self, target_pgn: int, timeout_sec: float = 2.0):
    try:
        while True:
            msg = self.message_queue.get(timeout=timeout_sec)
            if msg['pgn'] == target_pgn:
                return msg
    except queue.Empty:
        return None


def close(self):
    self.j1939_ecu.disconnect()
    self.bus.shutdown()




@htf.measures(
    htf.Measurement("ecu_component_id")
    .equals("MY-EMBEDDED-ECU-V1.0")
)
@htf.plug(can_stack=J1939TestPlug)
def test_ecu_identification(test, can_stack):
    target_pgn = 65259
    ecu_address = 0x00

    can_stack.send_request(target_pgn=target_pgn, destination_address=ecu_address)
    received_packet = can_stack.wait_for_pgn(target_pgn=target_pgn, timeout_sec=3.0,)

    if received_packet:
        raw_bytes = bytes(received_packet['data'])
        component_id_str = raw_bytes.decode('ascii', errors='ignor').split('*')[0].strip()

        test.logger.info(f"Received Component ID from Source {received_packet['source']}: {component_id_str}")
        test.measuremets.ecu_component_id = component_id_str
    else:
        test.logger.error("Timeout reached! ECU failed to broadcast Component ID")
        test.measurements.ecu_component_id = "TIMEOUT"


    def main():
        test_suite = htf.Test(test_ecu_identification)
        test_suite.execute(test_start_trigger=lambda: input("Scan ECU Barcode to start: "))

    if __name__ == "__main__":
        main()
