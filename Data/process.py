import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv('769c7dd7-f6be-4a6a-b28c-bf2fbdae12d6_Data.csv')
#
# for i in df.keys()[4:]:
#     for j in range(len(df[i])):
#         if df[i][j] == '..':
#             df[i][j] = '0'
#
# df.to_csv('by_time.csv')
by_time = pd.read_csv('by_time.csv')
corr = by_time.corr()
ax = sns.heatmap(corr,vmin = -1,vmax = 1, center = 0,
                 cmap=sns.diverging_palette(20,220),square = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom+0.5,top-0.5)
xticklabels = ['u','KWH','access','access rural','access urban','coal','hydro','natural gas','nuclear','oil','oil gas coal','renewed','renewed amount','t']
ax.set_xticklabels(xticklabels,rotation = 45,horizontalalignment = 'right')
ax.set_yticklabels(xticklabels)
plt.show()