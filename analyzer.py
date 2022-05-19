import os
from numpy import average
import pandas as pd
from matplotlib import pyplot as plt

print(*[filename.split('.')[0] for filename in os.listdir('./opinions')], sep = "\n")
product_id = input('Please enter a valid product id: ')

opinions = pd.read_json(f'opinions/{product_id}.json')
print(opinions)

opinions.stars = opinions.star_amount.map(lambda x: float(x.split('/')[0].replace(',', '.')))
opinions_count = len(opinions.index)
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_count = opinions.stars.mean().round(2)

recommendation = opinions.recomendation.value_counts(dropna = False).sort_index().reindex(['Nie polecam', 'Polecam', None])
recommendation.plot.pie(
    label="", 
    autopct='%1.1f%%',
    colors=['crimson', 'lightskyblue', 'forestgreen'],
    labels=['Nie polecam', 'Polecam', 'Nie mam zdania']
    )

plt.title('Rekomendacja')
plt.savefig(f'plots/{product_id}_recommendations.png')
plt.close()

stars = opinions.stars.value_counts().sort_index().reindex(list())
stars.plot.bar()
plt.title('Oceny produktu')
plt.xlabel('Liczba gwiazdek')
plt.ylabel('Liczba opinii')
plt.grid(True)
plt.xticks(rotation=0)
plt.show()


