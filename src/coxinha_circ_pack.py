import circlify
import matplotlib.pyplot as plt


coxinha_data = [{
    'id': 'Coxinha', 
    'datum': 1, 
    'children' : [
         {'id' : "Ponta", 'datum' : 52.4},
         {'id' : "Tanto faz", 'datum' : 19},
         {'id' : "Base", 'datum' : 14.3},
         {'id' : "Lado", 'datum' : 9.5},  
         {'id' : "Não é gostoso", 'datum' : 4.8}
    ]
}]
    

circles = circlify.circlify(
    coxinha_data, 
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


for circle in circles:
    if circle.level != 1:
        continue
    x, y, r = circle
    ax.add_patch(plt.Circle((x, y), r, alpha=0.2, linewidth=2, color = "#918f8e", label='_nolegend_'))
    label = circle.ex["id"]
    plt.annotate(label, (x,y + r) ,va='center', ha='center', family='monospace', size=14,
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round', pad=.5))

for circle in circles:
    if circle.level != 2:
        continue
    x, y, r = circle
    if circle.ex["id"] == "Não é gostoso":
        color="#20a483"
    else:
        color="#ff774a"
    ax.add_patch(plt.Circle((x, y), r, alpha=0.6, linewidth=2, color=color))
    label = circle.ex["id"]
    value = f'{circle.ex["datum"]} %'
    plt.annotate(label, (x,y), ha='center', va='center', color="white", family='monospace', size=18, weight='bold')
    plt.annotate(value, (x,y - 0.05), ha='center', va='center', color="white", family='monospace', size=18, weight='bold')


ax.set_title('Coxinha se come pela base ou pela ponta?', family='monospace', size=20, y=1.04)
ax.axis('off')

ax.legend(["Não gostam de coxinha", "Gostam de coxinha"], fontsize=14)

plt.savefig("coxinha.png", bbox_inches = "tight")