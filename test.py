import time

x = time.perf_counter() + 5
print(x, time.perf_counter())
while True:
    if x < time.perf_counter():
        #print('penis')
        break