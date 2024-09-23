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
# Используем агрегированные данные из с фильтрацие по кол-ву повторений (count >= 30) в обратном порядке
agg_df_2 = agg_df[agg_df['count'] > 30].sort_values(by='count', ascending=False)

# # Рендеринг графика с использованием PANDAS-стиля (внутрь которого встроин MATPLOTLIB)
# agg_df_2['count'].plot(
#     kind='bar',
#     title='Артисты написавшие больше всего хитов за последние 100 лет',
#     xlabel='Имя артиста',
#     ylabel='Количество написаных хитов'
#     )

fig, ax = plt.subplots()

# Получаем данные для оси-X из агрегированных agg_df_2
artists = list(agg_df_2.index)
# Получаем данные для оси-Y из агрегированных agg_df_2
counts = list(agg_df_2['count'])

# Установка данных графика для осей X и Y
ax.bar(artists, counts)


# Установка заголовка графика
ax.set_title('Артисты написавшие больше всего хитов за последние 100 лет')

# Поворот подписей по оси X вертикально
plt.xticks(rotation='vertical')
# Установка подписи оси-X
ax.set_xlabel('Имя артиста')

# Установка подписи оси-Y
ax.set_ylabel('Количество написаных хитов')

# Сдвиг графика вверх чтобы были видны подписи оси-X
plt.subplots_adjust(bottom=0.4)

# Рендеринг графика
# plt.show()

# Сохранение графика в png
plt.savefig('./matplotlib_imgs/test.png', format='png')
# ===========================================================================================
