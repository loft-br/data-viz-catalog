import pandas as pd
import matplotlib.pyplot as plt

cafe = [61.9]
cha = [19]
toddynho = [9.5]
suco = [4.8]
nescau = [4.8]

df = pd.DataFrame({'Café':cafe, 'Chá':cha, 'Toddynho':toddynho, 'Suco':suco, 'Nescau>Toddy':nescau})

ax = df.plot.barh(stacked=True, color = ["#ff774a", "#20a483", "#c93c0e", "#f09f84", "#b3725d"], figsize=(16,5), position=0.3)

ax.get_legend().remove()

for patch in ax.patches:
    height = patch.get_height()
    width = patch.get_width()
    x = patch.get_x()
    y = patch.get_y()
    
    label_text = f'{width:.1f}'
    
    label_x = x + width / 2
    label_y = y + height / 2
    
    if width > 0:
        ax.text(label_x, label_y, label_text, ha='center', va='center', fontsize=15, color='white', weight='bold', family = 'monospace')
    
plt.axis('off')

plt.title('Preferência entre chá, café ou toddynho (em %)',
          size=18, weight = 'bold', color = 'black', family = 'monospace', y=0.8)

plt.savefig('bebidas.jpg', pad_inches = 0.2, bbox_inches='tight')

plt.legend(fontsize = 15, ncol = len(df.columns), loc = 'lower center', bbox_to_anchor = (0.5, 0))

plt.savefig('bebidas_legenda.jpg', pad_inches = 0.2, bbox_inches='tight')