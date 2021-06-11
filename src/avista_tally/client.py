from autobahn.twisted.component import Component
from twisted.internet.defer import inlineCallbacks

import os

try:
    import blinkt
except ModuleNotFoundError:
    import avista_tally.fake_blinkt as blinkt
    print('blinkt library not found, using mock blinkt.')


component = Component(
    transports=os.environ.get('AVISTA_ROUTER'),
    realm=os.environ.get('AVISTA_REALM', 'avista')
)

TALLY_DEVICE_NAME = os.environ['AVISTA_TALLY_DEVICE']
TALLY_INPUT_NUMBER = int(os.environ['AVISTA_TALLY_INPUT']) - 1

TALLY_BRIGHTNESS = os.environ.get('AVISTA_TALLY_BRIGHTNESS', 0.1)


def handle_tally(message):
    blinkt.clear()
    tally = message.get('data')
    if 'by_index' in tally:
        my_tally = tally['by_index'].get(TALLY_INPUT_NUMBER, {})

        if my_tally.get('program'):
            blinkt.set_all(255, 0, 0, TALLY_BRIGHTNESS)
        elif my_tally.get('preview'):
            blinkt.set_all(0, 255, 0, TALLY_BRIGHTNESS)
    blinkt.show()


@component.on_join
@inlineCallbacks
def on_join(session, _):
    print("Connected to Avista router")
    yield session.subscribe(
        handle_tally,
        'avista.devices.{}/tally'.format(TALLY_DEVICE_NAME)
    )
