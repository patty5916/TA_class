# Pandas
## Introduction
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

## Useful Links
- [official Pandas website](https://pandas.pydata.org/)
- [official documentation](https://pandas.pydata.org/docs/)
- [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas cookbook](https://github.com/jvns/pandas-cookbook)

## Dataset
### Iris.csv
There are 150 records in 3 species, which 50 records are Iris-setosa, 50 records are Iris-versicolor, and 50 records are Iris-virginica.  
There are 4 numerical characteristics, which are the sepal length (cm), the sepal width (cm), the petal length (cm), and the petal width (cm).

## Contents
- Install and import pandas
  > `pip install pandas`, and `import pandas`
- Read data and some basic
  > `read_csv()`, `head()`, `shape()`, `dtypes()`, `describe()`, and `columns()`
- Create Series and DataFrame
  > `Series()`, and `DataFrame()`
- Missing values
  > `isnull()`, `fillna(<value>)`, and `dropna()`
- Extract row, column, and element
  > `df.loc[<label>]`, `df.iloc[<location>]`, `df[<column>]`, and `df.<column>`
- Mask and filter
  > `>`, `<`, `==`, `!=`, `and`, `or`, and `not`
- Operator broadcast and compute statistics
  > `argmax()`, `count()`, `prod()`, and `cumsum()`
- Group
  > `groupby()`, `get_group()`, and `aggregate()`
- Plot
  > with `matplotlib.pyplot`
