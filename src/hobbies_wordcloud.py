class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping

       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.

       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


hobbies_frequencies = {
    'bateria': 1,
    'fotografia': 1,
    'desenhar': 1,
    'dj de quarto': 1,
    'violão': 1,
    'cozinhar': 4,
    'bodyboard': 1,
    'surf': 1,
    'exercícios físicos': 2,
    'futebol': 4,
    'futebol americano': 1,
    'andar de bicicleta': 1,
    'assistir futebol': 1,
    'xadrez': 1,
    'vlogs de cultura': 1,
    'vlogs de geopolítica': 1,
    'haskell': 1,
    'leitura': 8,
    'documentários de história': 1,
    'idiomas': 1,
    'sair para beber': 1,
    'anime': 1,
    'pokemon': 1,
    'magic': 1,
    'RPG': 1,
    'videogame': 7,
    'videoclipes': 1,
    'filmes': 2,
    'séries': 3,
    'escutar música': 3,
    'colecionar baralhos': 1
}
                      
activity_groups = {
    'Hobbies artísticos': {
        'cor': '#20a483', 
        'atividades': ['bateria', 'fotografia', 'desenhar', 'dj de quarto','violão', 'cozinhar']
    },
    'Hobbies esportivos': {
        'cor': '#c72f00', 
        'atividades': [
            'bodyboard', 'surf', 'exercícios físicos', 'futebol', 'futebol americano',
            'andar de bicicleta', 'assistir futebol', 'xadrez'
        ]
    },
    'Hobbies intelectuais': {
        'cor': "#fca183", 
        'atividades': [
            'vlogs de cultura', 'vlogs de geopolítica', 'haskell', 'leitura',
            'documentários de história', 'idiomas'
        ]
    },
    'Hobbies de entretenimento': {
        'cor': 'white',
        'atividades': [
            'sair para beber', 'anime', 'pokemon', 'magic','RPG', 'videogame', 'videoclipes',
            'filmes', 'séries', 'escutar música', 'colecionar baralhos'
        ]
    }
}


fig = plt.figure(figsize=(16,12), facecolor = 'black')

wc_hobbies = WordCloud(width=1200, height= 800,
                      colormap = 'autumn', 
                      min_font_size = 20).generate_from_frequencies(hobbies_frequencies, max_font_size=110) 

#creating a dict just with colors and activities
color_items = []
for key,item in activity_groups.items():
    for key_sec, item_sec in item.items():
        color_items.append(item_sec) 

it = iter(color_items)
color_to_word_groups = dict(zip(it, it))

#default_color if any words not in groups
default_color = 'grey'

# Create a color function with single tone
grouped_color_func = SimpleGroupedColorFunc(color_to_word_groups, default_color)

# Create a color function with multiple tones
#grouped_color_func = GroupedColorFunc(color_to_word_groups, default_color)

# Apply our color function
wc_hobbies.recolor(color_func=grouped_color_func)

# Plot
plt.imshow(wc_hobbies)
plt.axis("off")

handles = []
for key, item in activity_groups.items():
    patch = mpatches.Patch(color = item["cor"], label = key)
    handles.append(patch)

plt.legend(handles=handles, loc='lower left', bbox_to_anchor=(0.02, -0.08), 
           fontsize=14, ncol= len(handles), framealpha = 0.65)

plt.savefig("hobbies_wordcloud.png", bbox_inches = "tight", pad_inches=0.4, facecolor=fig.get_facecolor())