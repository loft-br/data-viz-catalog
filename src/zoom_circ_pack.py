import circlify
import matplotlib.pyplot as plt


zoom_data = [{
    'id': 'Atraso em uma reunião virtual', 
    'datum': 1, 
    'children': [
        {
            'id': 'Bugs', 
            'datum': 4,
            'children': [
                {'id': 'Deu problema', 'datum':1},
                {'id': 'Lentidão', 'datum':1},
                {'id': 'Tava bugado', 'datum':1},
                {'id': 'Pediu senha', 'datum':1},
                {'id': 'PC reiniciou', 'datum':1},
                {'id': 'Não achei o invite', 'datum':1},
                {'id': 'Internet caiu', 'datum':1}
            ]
        }, {
            'id': 'Distorção de tempo', 
            'datum': 2, 
            'children' : [
                {'id': 'Achei que ia \ndar tempo', 'datum':1},
                {'id': 'Se perder no tempo \npreenchendo ótimos\n forms', 'datum':1},
                {'id': 'Teoria da \nrelatividade \ngeral', 'datum':1}
            ]
        }, {
            'id': 'Prioridades sinceras',
            'datum': 1,
            'children': [
                {'id': 'Estava \npassando um café', 'datum':1}
            ]
        }, {
            'id': 'Alta probabilidade', 
            'datum': 2, 
            'children': [
                {'id': 'Derrubei o PC \nno chuveiro', 'datum':1},
                {'id': 'Deixei cair uma \nbandeja de ovos', 'datum':1},
                {'id': 'Cachorro comeu o \ncabo da internet', 'datum':1}
            ]
        }
    ]
}]


circles_zoom = circlify.circlify(
    zoom_data, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

fig, ax = plt.subplots(figsize=(15,14))

lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)


for circle in circles_zoom:
    if circle.level != 2:
        continue
    x, y, r = circle
    color="#ff774a"
    ax.add_patch(plt.Circle((x, y), r, alpha=0.4, linewidth=2, color=color))
    label = circle.ex["id"]
    value = f'{circle.ex["datum"]} %'
    plt.annotate(label, (x,y + r) ,va='center', ha='center', family='monospace', size=14,
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

for circle in circles_zoom:
    if circle.level != 3:
        continue
    
    x, y, r = circle
    
    if circle.ex["id"] == 'Estava \npassando um café':
        r = 0.1840487986152107 
        
    color = "#ff774a"
    label = circle.ex["id"]
    
    ax.add_patch(plt.Circle((x, y), r, alpha=0.8, linewidth=2, color=color))
    plt.annotate(label, (x,y), ha='center', va='center', color="white", family='monospace', size=12, weight='bold')



ax.set_title('Qual a melhor desculpa para atrasar em uma reunião virtual?', family='monospace', size=20, y=0.97)
ax.axis('off')

plt.savefig("zoom_circ_pack.png", bbox_inches="tight")