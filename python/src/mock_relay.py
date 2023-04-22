class MockRelay:
  def __init__(self, number_of_circuits):
    self.number_of_circuits = number_of_circuits
    self.states_list = []
    
    for i in range(number_of_circuits) :
      # default states... False for all
      self.states_list.append(False)

  def state(self):
    return self.states_list
  
  def turn_on(self, index):
    self.states_list[index] = True

  def turn_off(self, index):
    self.states_list[index] = False

  def toggle(self, index):
    self.states_list[index] = not(self.states_list[index])

  def all_on(self):
    for i in range(len(self.states_list)) :
      self.states_list[i] = True

  def all_off(self):
    for i in range(len(self.states_list)) :
      self.states_list[i] = False