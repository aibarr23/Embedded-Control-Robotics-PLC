import subprocess
import time

import openhtf as htf
from openhtf.core import base_plugs

class PingPlug(base_plugs.BasePlug):
    """This plug simply does a ping aginst the host attribute"""
    host = None

    def __init__(self):
        assert self.host is not None
    
    def _get_command(self,count):
        return [
            'ping',
            '-c',
            str(count),
            self.host,
        ]

    def run(self,count):
        command = self._get_command(count)
        print('running: %s' % ' '.join(command))
        return subprocess.call(command)


class PingGoogle(PingPlug):
    host = 'google.com'
class PingDnsA(PingPlug):
    host = '8.8.8.8'
class PingDnsB(PingPlug):
    host = '8.8.4.4'


@htf.PhaseOptions(name='Ping-{pinger.host}-{count}')
@htf.plug(pinger=PingPlug.placeholder)
@htf.measures('total_time_{pinger.host}_{count}',
              htf.Measurement('retcode').equals('{expected_retcode}', type=str))
def test_ping(test, pinger, count, expected_retcode):
    del expected_retcode
    start = time.time()
    retcode = pinger.run(count)
    elapsed = time.time() - start
    test.measurements['total_time_%s_%s' % (pinger.host, count)] = elapsed
    test.measurements.retcode = retcode


def main():
    ping_plugs = [
        PingGoogle,
        PingDnsA,
        PingDnsB,
    ]
    phases = [
        test_ping.with_plugs(pinger=plug).with_args(count=2, expected_retcode=0)
        for plug in ping_plugs
    ]

    test = htf.Test(*phases)
    test.execute(test_start=lambda: 'MyDutId')

if __name__ == '__main__':
    main()
