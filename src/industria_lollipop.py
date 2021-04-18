import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))

industries = ["Financeira", "Varejo", "Mineração", "Mídia e Entretenimento", "Seguros", "Saúde", 
              "Produtos industriais", "Telecomunicações", "Educação","Bens de Consumo", "Óleo e gás",
              "Agricultura", "Farmacêutica", "Pesquisa", "Mobilidade", "Logística", "Construção Civil"]

count = [9, 6, 3, 4, 2, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

df = pd.DataFrame({'industry': industries, 'count': count})

ordered_df = df.sort_values(by='count')

plt.hlines(y=ordered_df['industry'], xmin=0, xmax=ordered_df['count'], color='orange', linewidth=5)

plt.plot(ordered_df['count'], ordered_df['industry'], "o", markersize=20, color = "#ff774a")
for i, count in enumerate(ordered_df['count']):
    plt.annotate(count, xy=(count, i), color='white', fontsize=16, weight = 'bold', ha='center', va='center')


plt.title('Indústrias em que cientistas de dados da Loft já trabalharam \n (por quantidade de menções)', 
          loc='center', color = 'black', fontsize = 20, family = 'monospace', y = 1.02)

plt.xlabel('Número de menções', fontsize=18, family = 'monospace')
plt.ylabel('Indústria', fontsize=18, family = 'monospace')

plt.yticks(fontsize=18, family = 'monospace')
plt.xticks(ticks=[])
plt.box(False)

plt.savefig("industrias_lollipop.png", bbox_inches = "tight")