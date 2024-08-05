
import matplotlib.pyplot as plt
import pandas as pd



# Загрузка данных из CSV файла
data_path = r'C:\Users\79156\Desktop\demography_paneldata_csv_19042021\data.csv'
data = pd.read_csv(data_path, dtype=str, low_memory=False)

# Преобразование столбца 'indicator_value' в числовой тип, замена некорректных значений на NaN
data['indicator_value'] = pd.to_numeric(data['indicator_value'], errors='coerce')

# Замена пропущенных значений на среднее значение столбца
data['indicator_value'].fillna(data['indicator_value'].mean(), inplace=True)

# Фильтрация данных для удаления пропущенных значений
filtered_df = data[data['bride_age'].notna()]
# Группировка данных по году и расчет среднего значения индикатора
grouped_data = data.groupby('year')['indicator_value'].mean().reset_index()

# Создание линейного графика
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['year'], grouped_data['indicator_value'])

# Добавление заголовка графика и подписей осей
plt.title('Среднее значение индикатора по годам')
plt.xlabel('Год')
plt.ylabel('Среднее значение индикатора')

# Отображение сетки для лучшей читаемости графика
plt.grid(True)

# Отображение графика
plt.show()


# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['bride_age'], bins=20, edgecolor='black')
plt.title('Распределение возраста невест')
plt.xlabel('Возраст невесты')
plt.ylabel('Частота')
plt.show()

# Фильтрация данных для удаления пропущенных значений
filtered_df = data[data[['bride_age', 'groom_age']].notna().all(axis=1)]

# Создание scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['bride_age'], filtered_df['groom_age'])
plt.title('Возраст невесты vs Возраст жениха')
plt.xlabel('Возраст невесты')
plt.ylabel('Возраст жениха')
plt.show()