import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
df = pd.DataFrame({
    'Pop': [2],
    'MPB': [1],
    'Eclético': [1],
    'Jazz': [2],
    'Rap': [1],
    'Sertanejo': [1],
    'Rock': [3],
    'Indie': [1],
    'Indie Rock': [2],
    'Heavy metal': [1],
    'Stoner Rock': [1],
    'Indie Pop': [2],
    'Eletrônica': [1],
})
 
categories=list(df)
N = len(categories)
 
# Repeat the first value to close the circular graph
values = df.values.flatten().tolist()
values += values[:1]
 
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

fig = plt.figure(figsize=(12,12), facecolor='white')
ax = plt.subplot(111, polar=True)
 
ax.set_rlabel_position(0)
plt.yticks([1,2,3], ["1","2","3"], color="black", size=10)
plt.ylim(0,)
 
ax.plot(angles, values, linewidth=1, linestyle='solid', color="#ff774a")
 
ax.fill(angles, values, color="#ff774a", alpha=0.5)

plt.xticks(angles[:-1], categories, color='black', size=16, family='monospace')
ax.tick_params(axis='x', which='major', pad=33)

ax.set_title('Estilo musical favorito por quantidade de menções', family='monospace', size=20, y=1.09)

plt.savefig("musica.png", bbox_inches="tight")