#pandas
import pandas as pd

#series
s = pd.Series([1, 2, 3, 4, 5])
print(s)
#dataframe
data= {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'language': ['Python', 'Java', 'C++'],
    'city': ['New York', 'Los Angeles', 'Chicago']

}
df = pd.DataFrame(data)
print(df)

