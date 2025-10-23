# PANDAS


Follow these instructions:

1. make new file with python code `touch stat_report.py`
2. prepare `data.csv` and
3. write these code to import data from data.csv and show the data

```python
import pandas
data = pandas.read_csv('./ID_6r9r_N1N9_normalized.csv')
print(data)
```
4. razdelitev v skupine:

```python
grade6 = data.loc[data['GRD'] == 6]
grade9 = data.loc[data['GRD'] == 9]
print(grade6)
print(grade9)
```

```python
mean_x = np.mean(final_score['XSUM%'])
std_x  =  np.std(final_score['XSUM%'], ddof=1)
mean_y = np.mean(final_score['YSUM%'])
std_y  =  np.std(final_score['YSUM%'], ddof=1)
print(mean_x, std_x)
print(mean_y, std_y)
```


5. statistika t-testa za odvisne vzorce:

```python
from scipy import stats
t_test=stats.ttest_rel(grade6['XSUM%'],grade6['YSUM%'])
print(t_test)
```

6. 
