import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

sources_df = pd.read_csv('professional_up.csv')
sources_df.rename(columns={sources_df.columns[0]:"Fontes"}, inplace=True)

sources = sources_df["Fontes"].apply(lambda x: pd.value_counts([s.strip() for s in x.split(",")])).sum()

frequencies = dict(sources)

plt.figure(figsize=(12,12))
wordcloud = WordCloud(width=1200, height= 800,
                      colormap = 'autumn', 
                      min_font_size = 20).generate_from_frequencies(frequencies) 
                        
plt.imshow(wordcloud) 
plt.axis("off") 
  
plt.savefig('estudos_wordcloud.jpg', bbox_inches='tight')
