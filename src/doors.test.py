from doors import Doors
from mock_relay import MockRelay

print("Running Mock Tests...")

relay = MockRelay(16)
assert relay.state() == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

relay.turn_on(0)
assert relay.state()[0] == True

relay.turn_off(0)
assert relay.state()[0] == False

relay.toggle(1)
assert relay.state()[1] == True

relay.all_on()
assert relay.state() == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

relay.all_off()
assert relay.state() == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

print("Finished Mock Tests.")