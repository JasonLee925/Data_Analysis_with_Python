import numpy as np

def calculate(list):
  # reshape
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    
  _list = np.asarray(list)
  _list = _list.reshape(3,3)

  # init
  calculations = {}
  np.set_printoptions(precision=12)
  
  # mean
  calculations["mean"] = [
    _list.mean(axis=0).tolist(), # vertical
    _list.mean(axis=1).tolist(), # horizontal
    _list.mean()                 # flattened
  ]
  
  # variance
  calculations["variance"] = [
    _list.var(axis=0).tolist(), # vertical
    _list.var(axis=1).tolist(), # horizontal
    _list.var()                 # flattened
  ]

  # std
  calculations["standard deviation"] = [
    _list.std(axis=0).tolist(), # vertical
    _list.std(axis=1).tolist(), # horizontal
    _list.std()                 # flattened
  ]
  
  # max
  calculations["max"] = [
    _list.max(axis=0).tolist(), # vertical
    _list.max(axis=1).tolist(), # horizontal
    _list.max()                 # flattened
  ]

  # min
  calculations["min"] = [
    _list.min(axis=0).tolist(), # vertical
    _list.min(axis=1).tolist(), # horizontal
    _list.min()                 # flattened
  ]
  
  # sum
  calculations["sum"] = [
    _list.sum(axis=0).tolist(), # vertical
    _list.sum(axis=1).tolist(), # horizontal
    _list.sum()                 # flattened
  ]
  
  return calculations
