from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

book_mask = np.array(Image.open("livro.png"))

book_dict = {
    'História da Sua Vida e Outros Contos': 1,
    'Foundation': 1,
    'Outliers': 1,
    'O Mundo Assombrado pelos Demônios': 1,
    'Quem é você, Alasca?': 1,
    'O Nome do vento ': 1,
    'A História sem Fim': 1,
    'Universo numa casca de noz': 1,
    'O Andar do Bêbado': 1,
    'Factfullness': 1,
    'His dark materials': 1,
    'As Intermitências da Morte': 1,
    'Sapiens': 1,
    'A brief history of time': 1,
    'Scott Pilgrim Contra o Mundo': 1,
    'The Gods Themselves': 1,
    'Anna Karenina': 1,
    'O Guia dos Curiosos': 1,
    'A menina que roubava livros': 1,
    'Brotopia' :1
} 

fig = plt.figure(figsize=(15,15))
wordcloud = WordCloud(background_color="black",mask=book_mask, contour_width=3, contour_color='white', 
                      colormap='autumn', min_font_size=9, prefer_horizontal=1).generate_from_frequencies(book_dict)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.savefig('livro_wordcloud.jpg', pad_inches = 0.2, bbox_inches='tight')