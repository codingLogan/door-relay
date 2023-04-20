# https://github.com/vicyap/sainsmart
from sainsmart import devices

def get_relay(devices):
  return devices.EthernetRelay()

# Returns a list of boolean
def get_door_state(relay):
  return relay.state()

# Locks unlock when voltage is received
def unlock_door(relay, index):
  relay.turn_on(index)

# Locks lock when voltage is absent
def lock_door(relay, index):
  relay.turn_off(index)

def toggle(relay, index):
  relay.toggle(index)

def unlock_all(relay):
  relay.all_on()

def lock_all(relay):
  relay.all_off()

get_relay(devices)
