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
print("Start Door Tests...")

door_relay = MockRelay(16)
doors = Doors(door_relay)
assert doors.get_door_state() == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

doors.unlock_door(2)
doors.unlock_door(3)
assert doors.get_door_state() == [False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False]

doors.lock_door(2)
assert doors.get_door_state() == [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]

doors.toggle(2)
assert doors.get_door_state()[2] == True
doors.toggle(2)
assert doors.get_door_state()[2] == False

doors.unlock_all()
assert doors.get_door_state() == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

doors.lock_all()
assert doors.get_door_state() == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

print("Finished Door Tests.")