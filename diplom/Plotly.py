
import plotly.express as px
import pandas as pd

# Загрузка данных из CSV файла
data_path = r'C:\Users\79156\Desktop\demography_paneldata_csv_19042021\data.csv'
data = pd.read_csv(data_path, dtype=str, low_memory=False)

# # Создание интерактивного линейного графика
# fig = px.line(data, x="year", y="indicator_value",
#               title='Среднее значение индикатора по годам',
#               labels={'value': 'Среднее значение индикатора'},
#               template='plotly_white')
#
# fig.update_layout(xaxis=dict(
#     rangeslider=dict(
#         visible=True
#     ),
#     type='date'
# ))
#
# fig.show()

# # Создание интерактивной гистограммы
# fig = px.histogram(data, x="bride_age",
#                    nbins=30,
#                    title='Распределение возраста невест',
#                    labels={'bride_age': 'Возраст невесты'})
#
# fig.show()

df = data.dropna(subset=['bride_age', 'groom_age'])

# Создание интерактивного scatter plot с изменяемым размером точек
fig = px.scatter(df, x="bride_age", y="groom_age",
                 size="birth_order",  # Размер точек зависит от количества детей
                 hover_data=['object_name'],  # Показываем имя объекта при наведении
                 title='Возраст невесты vs Возраст жениха с учетом количества детей',
                 labels={'birth_order': 'Количество детей'}
                 )

fig.show()