import pandas as pd

# Загрузка данных из таблицы с пингвинами
df = pd.read_csv('pinguins.csv')

# Создание нового столбца height_group на основе значения flipper_length_mm
df['height_group'] = pd.cut(df['flipper_length_mm'],
                            bins=[0, 35, 42, df['flipper_length_mm'].max()],
                            labels=['low', 'middle', 'high'],
                            right=False)

# Вывод таблицы с новым столбцом height_group
print(df)
