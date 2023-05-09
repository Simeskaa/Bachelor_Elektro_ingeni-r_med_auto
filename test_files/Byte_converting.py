import copy as copy
from struct import *


val_array = [1, 2, 3, 4, 5, 6]

print(pack(">bhl", val_array))
