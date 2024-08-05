import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Загрузка данных из CSV файла
data_path = r'C:\Users\79156\Desktop\demography_paneldata_csv_19042021\data.csv'
data = pd.read_csv(data_path, dtype=str, low_memory=False)

# filtered_df = data[data['bride_age'].notna()]
#
# sns.histplot(filtered_df['bride_age'], bins=20, kde=True)
# plt.title('Распределение возраста невест')
# plt.xlabel('Возраст невесты')
# plt.ylabel('Частота')
# plt.show()

# # Фильтрация данных для удаления пропущенных значений
# filtered_df = data[data[['bride_age', 'groom_age']].notna().all(axis=1)]
#
# sns.scatterplot(data=filtered_df, x='bride_age', y='groom_age')
# plt.title('Возраст невесты vs Возраст жениха')
# plt.xlabel('Возраст невесты')
# plt.ylabel('Возраст жениха')
# plt.show()

# Примерный датафрейм для демонстрации
dat = {
    'year': [2015, 2016, 2017, 2018],
    'region': ['Region1', 'Region2', 'Region3', 'Region4'],
    'marriages': [100, 150, 120, 130]
}
df_marriages = pd.DataFrame(dat)

# Переформатирование датафрейма для heatmap
df_pivot = df_marriages.pivot(index='year', columns='region', values='marriages')

# Создание heatmap с аннотациями чисел с плавающей точкой
sns.heatmap(df_pivot, annot=True, fmt=".1f")  # Использование ".1f" для аннотаций
plt.title('Heatmap с аннотациями чисел с плавающей точкой')
plt.show()