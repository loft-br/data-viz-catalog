import matplotlib.pyplot as plt
from pywaffle import Waffle

values = [62,28,5,5]
fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=values,
    labels=["Mestrado (62%)","Ensino superior \n completo (28%)","Ensino superior \n incompleto (5%)","Pós-graduação \n latu sensu (5%)"],
    figsize=(12, 8),
    colors=["#f59778", "#a6e3d5", "#20a483", "#d9562b"],
    legend={'loc':'lower left', 'bbox_to_anchor': (0, -0.35), 'fontsize':14, 'ncol': len(values), 'framealpha': 0}    
)

fig.set_facecolor('#EEEEEE')

plt.savefig('education_waffle.jpg', bbox_inches='tight')