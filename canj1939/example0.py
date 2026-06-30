import can, cantools
from cantools.j1939 import pgn_from_frame_id

CHANNEL = "1f72d84a-usb.local@1"
FILE = "/mnt/c/Users/aibar/Downloads/REPOSITORY/data/j1939-dbc-demo+/CSS-Electronics-SAE-J1939-DEMO+.dbc"
file = "j1939.dbc"

db = cantools.database.load_file(FILE, strict=False)
eec1 = db.get_message_by_name("EEC1")
EEC1_PGN = pgn_from_frame_id(eec1.frame_id)

with can.Bus(interface="cansub", channel=CHANNEL, bitrate=250_000, data_bitrate=1_000_000) as bus:
        for msg in bus:
            if pgn_from_frame_id(msg.arbitration_id) == EEC1_PGN:
                printf(f"{msg.timestamp:.3f} EngineSpeed = {eec1.decode(msg.data)['EngineSpeed']} rpm")
