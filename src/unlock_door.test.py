import sys

from doors import Doors
from mock_relay import MockRelay

# Run this test using
# python .\src\unlock_door.test.py 0

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

# Door Number/Name
print("\nDoor to unlock:", sys.argv[1])

assert sys.argv[1] == "0"

relay = MockRelay(16)
assert relay.state() == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

doors = Doors(relay)
doors.unlock_door(0)
assert doors.get_door_state()[0] == True