import matplotlib.pyplot as plt
from pywaffle import Waffle 

plt.rcParams['text.color'] = 'w'

work_loft = [45, 35, 20]

fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=work_loft,
    labels=[
        "Menos de 12 meses (45%)",
        "Entre 12 e 18 meses (35%)",
        "Mais de 18 até 24 meses (20%)"
    ],
    figsize=(16, 6),
    icons='key',
    icon_style='solid',
    icon_size=22,
    icon_legend=True,
    facecolor='black',
    colors=["#ffffff", "#ff774a", "#66ccb6"],
    legend={
        'loc': 'lower center',
        'bbox_to_anchor': (0.5, -0.35),
        'fontsize': 18,
        'ncol': len(work_loft),
        'framealpha': 0
    }    
)

plt.title(
    'Tempo de trabalhando na Loft',
     size=25, weight='bold'
)

plt.savefig('trabalho_loft_waffle.jpg', bbox_inches='tight', pad_inches=0.4, facecolor=fig.get_facecolor())