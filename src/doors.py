class Doors:
  def __init__(relay):
    self.relay = relay

  # Returns a list of boolean
  def get_door_state():
    return self.relay.state()

  # Locks unlock when voltage is received
  def unlock_door(index):
    self.relay.turn_on(index)

  # Locks lock when voltage is absent
  def lock_door(index):
    self.relay.turn_off(index)

  # If the door is locked, it will unlock it
  # If the door is unlocked, it will lock it
  def toggle(index):
    self.relay.toggle(index)

  def unlock_all():
    self.relay.all_on()

  def lock_all():
    self.relay.all_off()