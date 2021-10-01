from abc import ABC, abstractmethod

class Abstract_writer(ABC):
  def __init__(self, data, path = ""):
    self.data = data
    self.path = path

  @abstractmethod
  def encode_data(self):
    pass

  @abstractmethod
  def write_data(self):
    pass

class JSON_writer(Abstract_writer):
  def __init__(self, data, path = "./data/default.json"):
    super().__init__(data, path)

  def encode_data(self):
    print('Encode... Done')
    return self

  def write_data(self):
    print(f"Writting {self.path}... Done")
    return self

  def display(self):
    print(self.data)



t = JSON_writer(5)
t.encode_data().write_data().display()