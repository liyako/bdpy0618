import pandas
from matplotlib import pyplot, rc

data1 = pandas.read_csv('data\\data3.csv', skiprows=4, index_col='Country Name')
print data1.shape
data1.to_excel('data\\pandas_output.xlsx', sheet_name='population')
print data1.head()
print data1.columns
print data1['1960'].mean(), data1['1960'].std(), data1['1960'].median()
data1['alpha'] = data1['1960'] + data1['1970'] + data1['1980']
print data1.columns
print data1['Country Code']
belData = data1[data1['Country Code'] == 'BEL']
print belData
selected_years = ['1960', '1970', '1980']
font = {'family': 'Courier New'}
rc('font', **font)
print pyplot.style.available
pyplot.style.use('seaborn-notebook')
belData.plot(kind='bar', figsize=(12, 6), y=selected_years, fontsize=10)
pyplot.show()