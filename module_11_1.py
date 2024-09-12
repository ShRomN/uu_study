import pandas as ps

# Скаченный датасет для работы с pandas
# https://www.kaggle.com/datasets/thebumpkin/10400-classic-hits-10-genres-1923-to-2023?resource=download

# Открываем датасет содержащийся в файле CSV
df = ps.read_csv('ClassicHit.csv', sep=',', header=0)

# Выводим наименования колонок и идентифицированные типы данных содержащиеся в них
print(df.dtypes)

# Выводим первые пять строк датафрейма df
print(df.head(5))

# Выводим последние пять строк датафрейма df
print(df.tail(5))

# Создаем объект df2 (DataFrame) при помощи среза объекта df
df2 = df.loc[3:8, ['Track', 'Artist', 'Duration']]

# Выводим датафрейм df2
print(df2)

# Создаем объект df3 (DataFrame) при помощи сортировки датафрейма df2
df3 = df2.sort_values(by='Duration')

# Выводим датафрейм df3
print(df3)
