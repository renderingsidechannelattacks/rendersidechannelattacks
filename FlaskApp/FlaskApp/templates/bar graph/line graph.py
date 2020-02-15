import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

linestyles = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
y = [15.4, 10.3, 7.6, 5.4, 4.4, 3.1, 2.6, 2.4, 2.9, 2.6, 2.3, 2.2, 2.0, 2.3, 2.6, 2.9, 2.1, 2.6, 2.4, 2.3]

y2 = [27.1, 25.4, 24.3, 23.3, 22.4, 21.3, 20.9, 20.1, 19.6, 16.0, 15.3, 14.7, 14.3, 13.9, 14.0,13.7,13.3,13.9,13.7,13.5]

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y2, linestyle='--', label='UniGL', marker='x')
line2, = ax.plot(x, y, linestyle='-', label='WebGL', marker='o')

ax.set_ylabel('CPU Utilization (%)')
ax.set_xlabel('Time (seconds)')
plt.xticks(x);


# Using plot(..., dashes=...) to set the dashing when creating a line


ax.legend()
plt.show()