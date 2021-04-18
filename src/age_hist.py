import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

age_df = pd.read_csv("age.csv")

mean = age_df['Idade'].mean()
median = age_df['Idade'].median()
modes = age_df['Idade'].mode()
 
fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)}, figsize = (16,8))
 
sns.boxplot(age_df['Idade'], ax=ax_box, color= '#ff774a')

sns.distplot(age_df['Idade'],bins=15, ax=ax_hist, color= '#ff774a', kde=False)

ax_hist.axvline(mean, color='r', linewidth=4)
ax_hist.axvline(median, color='black', linestyle='dashed', linewidth=3)
for mode in modes:
    ax_hist.axvline(mode, color="#20a483", linestyle='dashed', linewidth=3)
    
ax_box.set(xlabel='')
plt.xlabel("Idade", fontsize=14)

plt.suptitle("Distribuição de idade de cientistas de dados da Loft (em anos)", fontsize=18, family='monospace')

plt.yticks(fontsize=14, family = 'monospace')
plt.xticks(fontsize=14, family = 'monospace')

plt.legend({'Média':mean,'Mediana':median,'Moda':mode}, ncol=3, bbox_to_anchor=(0.7,-0.15),
          fontsize=15)

plt.savefig("age.png", bbox_inches = "tight")