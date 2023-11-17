# Создание DataFrame

import pandas as pd

data = {'Имя': ['Даниил', 'Александр', 'Артём'],
        'Возраст': [21, 20, 20 ],
        'Город': ['Липецк', 'Ефремов', 'Воронеж']}

df = pd.DataFrame(data)

print(df)
