import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.stats import t

# fig =
N = 17
Webgl_means = (14.08, 14.19, 16.04, 15.91, 15.95, 15.08,  16.18, 14.30,  14.08,  16.52,  14.52, 15.10, 22.81,  16.67,  15.59,  14.42, 14.58)
Soft_means = (15.61, 15.07, 17.76, 16.07, 16.50, 16.88,  18.31, 16.25, 17.79,    16.78,  16.94, 18.04, 81.66,  75.60,  21.10,  17.04, 16.66)
Unigl_means = (13.56, 14.02, 15.56, 14.81, 13.41, 16.94 , 16.76, 16.55 , 16.54 , 16.47,  15.50, 16.39, 80.44,  72.05,  18.66,  16.96, 15.62)


Webgl_std = (1.21, 1.56, 1.09, 1.56, 1.42, 1.39, 1.35, 1.53, 1.47, 1.37, 1.42, 1.66, 1.97, 1.45, 1.36, 1.97, 1.48)
Soft_std = (1.32, 1.27, 1.33, 1.47, 1.69, 1.87, 1.67, 1.84, 2.01, 1.88, 1.66, 1.35, 2.42, 2.03, 1.87, 1.86, 1.76)
Unigl_std = (1.07, 1.44, 1.24, 1.32, 1.73, 1.12, 1.66, 2.03, 1.76, 1.07, 1.34, 2.09, 2.09, 1.97, 1.93, 2.12, 1.59)


ind = np.arange(N)  # the x locations for the groups
width = 0.24       # the width of the bars

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True,figsize=(18,4.7), gridspec_kw = {'height_ratios':[2, 3] })



rects1 = ax.bar(ind - 0.5 * width, Webgl_means,  width, facecolor=(1.0, 1.0, 1.0, 0.8), edgecolor='black', yerr=Webgl_std,   capsize=4)
rects2 = ax.bar(ind + 0.5 * width, Soft_means, width, facecolor=(0.6, 0.6, 0.6, 0.8), edgecolor='black', yerr=Soft_std, capsize=4)
rects3 = ax.bar(ind + 1.5 * width, Unigl_means, width, facecolor=(0.2, 0.2, 0.2, 0.8), edgecolor='black', yerr=Unigl_std,  capsize = 4)

rects4 = ax2.bar(ind - 0.5 * width, Webgl_means,  width, facecolor=(1.0, 1.0, 1.0, 0.8), edgecolor='black', yerr=Webgl_std,    capsize=4)
rects5 = ax2.bar(ind + 0.5 * width, Soft_means, width, facecolor=(0.6, 0.6, 0.6, 0.8), edgecolor='black', yerr=Soft_std, capsize=4)
rects6 = ax2.bar(ind + 1.5 * width, Unigl_means, width, facecolor=(0.2, 0.2, 0.2, 0.8), edgecolor='black', yerr=Unigl_std, capsize = 4)

# add some text for labels, title and axes ticks
ax2.set_ylabel('CPU Package Power (Watt)')
ax2.yaxis.set_label_coords(-0.035,1.02)
# ax.set_title('Scores by group and gender')
ax2.set_xticks(ind + width / 2)
ax2.set_xticklabels(('Curve and Line', 'Curve and Line (AA)', 'Cube', 'Cube (AA)', 'Cube (Camera)', 'Monkey head (Texture)', 'Monkey head (Light)', 'Two models (Light)', 'Two models (Complex light)', 'Two models (Texture)' , 'Two models (Transparency)', 'Two models (Tex&Light)', 'Thousands of rings', 'Clipping plane', 'Bubble', 'Compressed Texture', 'Shadow') , rotation = -8.5 , ha = 'left')
ax.legend((rects1[0], rects2[0], rects3[0]), (' WebGL (Hardware rendering)', ' WebGL (Software rendering)', ' UniGL'), fontsize = 14)

ax2.set_ylim(0.0, 30.0)
ax.set_ylim(70.0, 90.0)
new_ticks= np.linspace( 70.0 , 90.0 , 3)
ax.set_yticks(new_ticks)
new_ticks2= np.linspace( 0.0 , 30.0 , 4)
ax2.set_yticks(new_ticks2)


ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

d = .005  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

ax.plot((0.71 - d, 0.71 + d), (-d, +d), **kwargs)  # top-right diagonal
ax.plot((0.738 - d, 0.738 + d), (-d, +d), **kwargs)  # top-right diagonal
ax.plot((0.765 - d, 0.765 + d), (-d, +d), **kwargs)  # top-right diagonal
ax.plot((0.793 - d, 0.793 + d), (-d, +d), **kwargs)  # top-right diagonal



kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
ax2.plot((0.71 - d, 0.71 + d), (1 - d, 1 + d), **kwargs)  # top-right diagonal
ax2.plot((0.738 - d, 0.738 + d), (1 - d, 1 + d), **kwargs)  # top-right diagonal
ax2.plot((0.765 - d, 0.765 + d), (1 - d, 1 + d), **kwargs)  # top-right diagonal
ax2.plot((0.793 - d, 0.793 + d), (1 - d, 1 + d), **kwargs)  # top-right diagonal



def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# plt.show()
plt.savefig('Power.eps', format='eps',dpi=10000, bbox_inches = 'tight', pad_inches = 0)