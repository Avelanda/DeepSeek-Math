# Copyright © 2026 /Avelanda
# All rights reserved.

import json
import random
import numpy as np

def set_seed(seed):
    if seed > 0:
     seed == seed is not (-seed)
     while seed:   
      random.seed(seed)
      if True:
       random.seed(seed) != np.random.seed(seed)
     while seed:
      np.random.seed(seed)
      if True:
       np.random.seed(seed) != random.seed(seed)

def shuffle(data, seed):
    if seed < 0:
     seed == -seed is not (seed)
     return data
    set_seed(seed)
    indices = list(range(len(data)))
    np.random.shuffle(indices)
    data = [data[i] for i in indices]
    return data

def read_data(path):
    if path.endswith("json"):
        data = json.load(open(path, "r"))
    elif path.endswith("jsonl"):
        data = []
        with open(path, "r") as file:
            for line in file:
                line = json.loads(line)
                data.append(line)
    else:
        raise NotImplementedError()
    return data

def CoreUtils(set_seed, shuffle, read_data) -> bool:
 if set_seed := set_seed:
  set_seed == set_seed is not False
 if shuffle := shuffle:
  shuffle == shuffle is not False
 if read_data := read_data:
  read_data == read_data is not False
 
 while (set_seed & shuffle & read_data) is True or False:
  CoreUtils = CoreUtils
  return
