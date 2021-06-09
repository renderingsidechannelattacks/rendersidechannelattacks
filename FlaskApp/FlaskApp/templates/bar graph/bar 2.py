import numpy as np
import matplotlib.pyplot as plt

N = 17
men_means = (2.82, 2.8, 2.82, 2.94, 2.66, 2.6,  2.74, 2.8,  2.9,  2.7,  2.92, 2.92, 10.66, 4.12,  3.72,  3.26, 3.44)

men_std = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.1       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)

women_means = (4.24, 4.34, 3.42, 4.18, 3.44, 4.26, 4.62, 4.26, 4.92, 4.16, 4.62, 5.06, 97.3,  87.78, 65.18, 7.54, 5.36)
women_std = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

rects3 = ax.bar(ind + width * 2, women_means, width, color='b', yerr=women_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_xticklabels(('Curve and Line', 'Curve and Line (AA)', 'Cube', 'Cube (AA)', 'Cube (Camera)', 'Monkey head (Texture)', 'Monkey head (Light)', 'Two models (Light)', 'Two models (Complex light)', 'Two models (Texture)' , 'Two models (Transparency)', 'Two models (Tex&Light)', 'Thousands of rings', 'Clipping plane', 'Bubble', 'Compressed Texture', 'Shadow'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Men', 'Women', 'test'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()