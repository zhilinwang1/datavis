import pandas as pd
import numpy as np
df_all = pd.read_csv('electricity_production_proportion(raw).csv')
print(df_all.keys())
print(len(df_all))
df_valid = df_all.dropna()
keys = df_all.keys()
for i in keys[5:]:
    ind = df_valid[df_valid[i] == '..'].index
    df_valid.drop(ind,inplace = True)
print(len(df_valid))

#


growth = {}
growth[keys[0]] = df_valid[keys[0]].values
growth[keys[2]] = df_valid[keys[2]].values
for i in range(5,len(keys)):
    #print(df_valid[keys[6]].values)
    #print(list(map(float,df_valid[keys[6]].values)))
    key = keys[i]
    key_prev = keys[i-1]
    year = key.split()[0]
    growth[year] = np.subtract(list(map(float,df_valid[key].values)),
                               list(map(float,df_valid[key_prev].values)))
#print(growth)
df_growth = pd.DataFrame(data = growth)


col_dic = {df_valid.keys()[4]:'1996'}
i = 2
for key in df_valid.keys()[5:]:

    col_dic[key] = df_growth.keys()[i]
    i += 1
print(col_dic)
df_valid = df_valid.rename(columns=col_dic)

df_growth.set_index('Series Name', inplace=True)
df_growth.to_csv('changes.csv')

df_valid = df_valid.drop(columns=['Series Code', 'Country Code'])

print(df_valid.keys())
sources = np.unique(df_valid[keys[0]].values)
for i in sources:
    df_i = df_valid[df_valid[keys[0]] == i]
    df_i.set_index('Series Name', inplace=True)
    df_i.to_csv(i+'.csv')

df_china = df_valid[df_valid[keys[2]]== 'China']
#df_china.set_index('Series Name', inplace=True)
df_china.to_csv('china.csv')
print(df_china.keys())
print(df_china)

extra = pd.read_csv('data_extra.csv')
print(extra.keys())
extra_keys = extra.keys()
extra = extra.dropna()
# for i in extra_keys[4:]:
#     ind = extra[extra[i] == '..'].index
#     extra.drop(ind,inplace = True)

more_var = np.unique(extra[extra_keys[2]].values)
print('more var: '+more_var)
# for i in sources:
#     df_i = df_valid[df_valid[extra_keys[2]] == i]
#     df_i.set_index('Series Name', inplace=True)
    #df_i.to_csv(i+'.csv')
#countries = df_valid[keys[2]]
df_source = df_valid[df_valid[keys[0]] == sources[0]]
countries = df_source[keys[2]]
print(len(countries))
by_country = {'Country':countries}
source_index = [0,1,2,3,4,6]
for i in source_index:

    source = sources[i]

    df_source = df_valid[df_valid[keys[0]] == source]
    #countries = df_source[keys[2]]

    arr = []
    for country in countries:
        if country in df_source[keys[2]].values:
            value = float(df_source[df_source[keys[2]] == country]['2014'].values[0])
            arr.append(value)
        else:
            arr.append(0)
    by_country[source] = arr

more_var_index = [0,1,2,4,5]
for i in more_var_index:
    source = more_var[i]
    df_source = extra[extra[extra_keys[2]] == source]
    #countries = df_source[extra_keys[0]]
    print(len(df_source))
    arr = []
    for country in countries:
        if country in df_source[extra_keys[0]].values:
            value = df_source[df_source[extra_keys[0]] == country]['2014 [YR2014]'].values[0]
            arr.append(value)
        else:
            arr.append(0)
    by_country[source] = arr

by_country_df = pd.DataFrame(by_country)
by_country_df.to_csv('by_country.csv')
print(sources)

import seaborn as sns
import matplotlib.pyplot as plt
print(by_country_df.keys())
print('extra keys')
for key in by_country_df.keys()[7:]:
    print(key)
    print('key')
    arr = by_country_df[key].values
    lis = []
    for i in arr:
        if i == '..':
            lis.append(0)
        else:
            lis.append(float(i))
    by_country_df[key] = lis


print('keys')
print(by_country_df.keys())
corr = by_country_df.corr()
ax = sns.heatmap(corr,vmin = -1,vmax = 1, center = 0,
                 cmap=sns.diverging_palette(20,220),square = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom+0.5,top-0.5)
#ax.set_xticklabels(ax.get_xticklabels(),rotation = 45,horizontalalignment = 'right')
plt.show()

# df_transpose = df_i.transpose()
# print(df_transpose.keys())
transpose = {'Country':df_i['Country name'],'Year':keys[5:]}

for country in transpose['Country']:
    df_country = df_i[df_i['Country name'] == country]
    for source in sources:
        df_source = df_country[df_country['Series name'] == source]
        values_by_time = df_source[:,5:].values
        print(values_by_time)

