import pandas as pd
import matplotlib.pyplot as plt


# =============================  РАБОТА С БИБЛИОТЕКОй - PANDAS  =============================
# Скаченный датасет для работы с pandas
# https://www.kaggle.com/datasets/thebumpkin/10400-classic-hits-10-genres-1923-to-2023?resource=download

# Открываем датасет содержащийся в файле CSV
df = pd.read_csv('ClassicHit.csv', sep=',', header=0)

# Выводим наименования колонок и идентифицированные типы данных содержащиеся в них
print('-' * 50)
print(df.dtypes)
print('-' * 50)

# Выводим первые пять строк датафрейма df
print('-' * 50)
print(df.head(5))
print('-' * 50)

# Выводим последние пять строк датафрейма df
print('-' * 50)
print(df.tail(5))
print('-' * 50)

# Создаем объект df2 (DataFrame) при помощи среза объекта df
df2 = df.loc[3:7, ['Track', 'Artist', 'Duration']]

# Выводим датафрейм df2
print('-' * 50)
print(df2)
print('-' * 50)

# Создаем объект df3 (DataFrame) при помощи сортировки датафрейма df2
df3 = df2.sort_values(by='Duration')

# Выводим датафрейм df3
print('-' * 50)
print(df3)
print('-' * 50)

# Создаем объект df4 (DataFrame) при помощи фильтрации значения по столюцу Duration
df4 = df2[df2['Duration'] >= 245573]

# Выводим датафрейм df3
print('-' * 50)
print(df4)
print('-' * 50)

# Группируем df по столбцу Artist
grouped_1 = df.groupby('Artist')
# Агрегируем данные создавая столбцы с колличеством сгрупированных строк (count)
# и общей суммой продолжительности треков (duration_sum) 

agg_df = grouped_1.agg(
    count=pd.NamedAgg(column="Duration", aggfunc="count"),
    duration_sum=pd.NamedAgg(column="Duration", aggfunc="sum")
)

# Выводим сгрупированные данные с фильтрацие по кол-ву повторений (count >= 30) в обратном порядке
print('-' * 50)
print(agg_df[agg_df['count'] > 30].sort_values(by='count', ascending=False))
print('-' * 50)

# ===========================================================================================


# ===========================  РАБОТА С БИБЛИОТЕКОй - MATPLOTLIB  ===========================
agg_df_2 = agg_df[agg_df['count'] > 30].sort_values(by='count', ascending=False)
print(agg_df_2.dtypes)
print(type(agg_df_2['count']))

# Печать графика с использованием PANDAS
agg_df_2['count'].plot(
    kind='bar',
    title='Артисты написавшие больше всего хитов за последние 100 лет',
    xlabel='Имя артиста',
    ylabel='Количество написаных хитов'
    )

print(agg_df_2.index)







fig, ax = plt.subplots()

# artists = ['apple', 'blueberry', 'cherry', 'orange']
artists = list(agg_df_2.index)
# counts = [40, 100, 30, 55, 40, 100, 30, 55]
counts = list(agg_df_2['count'])
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# ax.bar(artists, counts, label=bar_labels)
ax.bar(artists, counts)


# Установка заголовка графика
ax.set_title('Артисты написавшие больше всего хитов за последние 100 лет')

# Поворот подписей по оси X вертикально
plt.xticks(rotation='vertical')
# Установка подписи оси X
ax.set_xlabel('Имя артиста')

# Установка подписи оси Y
ax.set_ylabel('Количество написаных хитов')

# ax.legend(title='Имя артиста')


plt.show()
# plt.savefig('./matplotlib_imgs/test.png', format='png')
# ===========================================================================================
