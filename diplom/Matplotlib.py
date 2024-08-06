

import matplotlib.pyplot as plt
import pandas as pd



# Загрузка данных из CSV файла
data_path = r'C:\Users\79156\Desktop\demography_paneldata_csv_19042021\data.csv'
data = pd.read_csv(data_path, dtype=str, low_memory=False)

# Преобразование столбца 'indicator_value' в числовой тип и замена некорректных значений на NaN
data['indicator_value'] = pd.to_numeric(data['indicator_value'], errors='coerce')

# Замена пропущенных значений на среднее значение столбца
data['indicator_value'].fillna(data['indicator_value'].mean(), inplace=True)

# Фильтрация данных для удаления пропущенных значений (если есть другие важные фильтры, примените их здесь)
filtered_df = data[data['bride_age'].notna()]

# Группировка данных по году и расчет среднего значения индикатора
grouped_data = data.groupby('year')['indicator_value'].mean().reset_index()

# Создание линейного графика
plt.figure(figsize=(12, 6))
plt.plot(grouped_data['year'], grouped_data['indicator_value'], marker='o')

# Добавление заголовка графика и подписей осей
plt.title('Среднее значение индикатора по годам')
plt.xlabel('Год')
plt.ylabel('Среднее значение индикатора')

# Настройка подписи оси X с шагом 5 лет
plt.xticks(ticks=grouped_data['year'][::5], rotation=45)

# Отображение сетки для лучшей читаемости графика
plt.grid(True)

# Отображение графика
plt.tight_layout()
plt.show()

# Фильтрация данных для удаления пропущенных значений
filtered = data[data['bride_age'].notna()]

# Создание гистограммы
plt.figure(figsize=(12, 6))
plt.hist(filtered['bride_age'], bins=20, edgecolor='black')

# Добавление заголовка графика и подписей осей
plt.title('Распределение возраста невест')
plt.xlabel('Возраст невесты')
plt.ylabel('Частота')

# Настройка подписи оси X
plt.xticks(rotation=45, ha='right')  # Поворот подписей и выравнивание по правому краю
plt.tight_layout()  # Подстройка макета, чтобы избежать наложений

# Отображение графика
plt.show()

# Фильтрация данных для удаления пропущенных значений
filtered_d = data[['bride_age', 'groom_age']].dropna()

# Создание scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(filtered_d['bride_age'], filtered_df['groom_age'], alpha=0.5)

# Добавление заголовка графика и подписей осей
plt.title('Возраст невесты vs Возраст жениха')
plt.xlabel('Возраст невесты')
plt.ylabel('Возраст жениха')

# Настройка подписи оси X
plt.xticks(rotation=45, ha='right')  # Поворот подписей и выравнивание по правому краю

# Отображение графика
plt.tight_layout()  # Подстройка макета, чтобы избежать наложений
plt.show()
