import matplotlib.pyplot as plt

diversity=["Pessoas não-brancas", "Gênero feminino", "LGBTQIAP+"]  
non_diverse=[81, 81, 81]  
diverse=[19, 19, 19]  

fig=plt.figure(figsize=(12,8))

plt.bar(diversity, diverse, color='#ff774a', edgecolor='black')
plt.bar(diversity, non_diverse, bottom=diverse, color='white', edgecolor='black')

plt.xlabel('Grupo de Diversidade', fontsize=16, family='monospace')  
plt.ylabel('Porcentagem de Pessoas', fontsize=16, family='monospace')
for i, percentage in enumerate(diverse)
    plt.annotate(f"{percentage} %", xy=(i, percentage + 2), color='#ff774a', fontsize=16, weight='bold', ha='center', va='bottom')


plt.yticks(fontsize=14, family='monospace')
plt.xticks(fontsize=14, family='monospace')

plt.title('Pessoas que se identificam com grupos de diversidade \n (% em relação ao total de respondentes)', color='black', 
          fontsize=16, family='monospace')

#plt.box(False)

plt.savefig("diversity.png", bbox_inches="tight")