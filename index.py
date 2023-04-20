from sainsmart import devices

relay = devices.EthernetRelay()

# Access the state of the relays
# relay.state() is a list of bools
relay_state = relay.state()

# Turn on the relay at index 0.
relay.turn_on(0)

# Turn off the relay at index 0.
relay.turn_off(0)

# Toggle the state of relay 0.
relay.toggle(0)

# Turn on all relays.
relay.all_on()

# Turn off all relays.
relay.all_off()