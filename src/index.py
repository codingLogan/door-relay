import sys

# https://github.com/vicyap/sainsmart
from sainsmart import devices
from mock_relay import MockRelay
from doors import Doors

# Example command
# python src/index.py {lock|unlock} {door-number}
# python src/index.py {lock-all|unlock-all}


# GET ARGUMENTS
arg_count = len(sys.argv)
command = ""
door = ""

if arg_count > 1 :
  command = sys.argv[1]

if arg_count > 2 :
  # Treat the arg as an integer
  door = int(sys.argv[2])

print("command:", command)
print("door:", door)


# BEGIN SCRIPT
mode = "test"
relay = ""

if mode == "test":
  # Default the test mode to a 16 channel relay
  relay = MockRelay(16)
else:
  # Get the real device, could be any amount of channels
  relay = devices.EthernetRelay()

doors = Doors(relay)

if command == "lock" :
  doors.lock_door(door)
elif command == "unlock" :
  doors.unlock_door(door)
elif command == "lock-all" :
  doors.lock_all()
elif command == "unlock-all" :
  doors.unlock_all()
else :
  print("no valid command")

print("Channel states:", doors.get_door_state())
