import matplotlib.pyplot as plt
import squarify

df = pd.DataFrame({
    'values': [52.4, 9.5, 9.5, 4.8, 4.8, 4.8, 4.8, 4.8, 4.8], 
    'group': [
        "Coca-cola (%)", 
        "Tanto faz (%)", 
        "Não curto\n refrigerante (%)", 
        "Guaraná (%)",
        "Pepsi (%)",
        "Coca-cola \naté D -10 (%)",
        "Água com gás,\n gelo e limão (%)",
        "Suco natural (%)",
        "Água com gás\n (%)"
    ] 
})

fig = plt.figure(figsize=(12,8), facecolor='#ede6e4')

squarify.plot(
    sizes=df['values'], 
    color=[
        "#ed764e", "#20a483", "#c93c0e", "#f09f84", "#b3725d",
        "#80a69c", "#c95e3a", "#ed4c15", "#1d6653"
    ],
    pad=True,
    label=df['group'], 
    value=df['values'], 
    text_kwargs={
        'fontsize': 14, 
        'color': 'white', 
        'fontweight': 'bold', 
        'family': 'monospace'
    }
)

plt.title(
    'Preferência por coca-cola ou guaraná (em %)',
     size=16, weight='bold', color='black', family='monospace'
)


plt.axis('off')
plt.savefig('refri_treemap.jpg', facecolor = fig.get_facecolor(), pad_inches = 0.2, bbox_inches='tight')