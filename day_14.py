# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

import random
import math

inside = 0
for total in range(0, 1000):
    tmp = math.hypot(random.random(), random.random())
    if tmp < 1: 
        inside += 1
total += 1
print(4.0 * inside / total)