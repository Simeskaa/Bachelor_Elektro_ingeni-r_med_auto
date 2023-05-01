import numpy as np

max_dist = 10
U = [0.3, 0.7]


xnew = max_dist * U[0]
ynew = max_dist * U[1]

print(f'xnew: {xnew}\n'
      f'ynew: {ynew}\n')

Unew = np.dot(max_dist, U)

print(f'Unew: {Unew}')