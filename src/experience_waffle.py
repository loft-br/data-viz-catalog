import matplotlib.pyplot as plt
from pywaffle import Waffle 

plt.rcParams['text.color'] = 'w'

experience = [23.8, 38.1, 38.1]

fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=experience,
    labels=["1-2 anos (24%)","3-4 anos (38%)","mais de 5 anos (38%)"],
    figsize=(16, 6),
    icons = 'laptop-code',
    icon_style = 'solid',
    icon_size = 22,
    icon_legend=True,
    facecolor = 'black',
    colors=["#ffffff", "#ff774a", "#66ccb6"],
    legend={'loc':'lower center', 'bbox_to_anchor': (0.5, -0.25), 'fontsize':18,
            'ncol': len(experience), 'framealpha': 0}    
)

plt.title(
    'Tempo de Experiência trabalhando com dados',
     size=25, weight='bold')


plt.savefig('experience_waffle.jpg', bbox_inches = 'tight', pad_inches=0.4, facecolor=fig.get_facecolor())