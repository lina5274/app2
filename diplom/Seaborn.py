import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Загрузка данных из CSV файла
data_path = r'C:\Users\79156\Desktop\demography_paneldata_csv_19042021\data.csv'
data = pd.read_csv(data_path, dtype=str, low_memory=False)

# Создание фигуры с заданным размером, чтобы вместить все метки оси X
plt.figure(figsize=(12, 10))
filtered_df = data[data['bride_age'].notna()]


sns.histplot(filtered_df['bride_age'], bins=20, kde=True)
plt.title('Распределение возраста невест')
plt.xlabel('Возраст невесты')
plt.ylabel('Частота')

# Управление метками оси x
plt.xticks(rotation=45)  # Вращение меток на 45 градусов для лучшей читаемости

plt.show()

# Создание фигуры с заданным размером, чтобы вместить все метки оси X
plt.figure(figsize=(10, 9))
# Фильтрация данных для удаления пропущенных значений
filtered_d = data[data[['bride_age', 'groom_age']].notna().all(axis=1)]

sns.scatterplot(data=filtered_d, x='bride_age', y='groom_age')
plt.title('Возраст невесты vs Возраст жениха')
plt.xlabel('Возраст невесты')
plt.ylabel('Возраст жениха')
# Управление метками оси x
plt.xticks(rotation=45)  # Вращение меток на 45 градусов для лучшей читаемости
plt.show()
