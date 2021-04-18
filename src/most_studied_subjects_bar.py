import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

n_frames = 10

height_states = [[0, 0, 0, 0, 0],
                 [2, 2, 2, 0, 0],
                 [2, 2, 2, 4, 0],
                 [2, 2, 2, 4, 6]]

x = np.arange(len(height_states[0]))

subjects_states = [['', '', '', '', ''],
                  ['Recomendação', 'Análise de \nSobrevivência', 'Álgebra Linear', '', ''],
                  ['Recomendação', 'Análise de \nSobrevivência', 'Álgebra Linear', 'Desenvolvimento/\nProgramação', ''],
                  ['Recomendação', 'Análise de \nSobrevivência', 'Álgebra Linear', 'Desenvolvimento/\nProgramação', 'Inferência Causal']]



frames = []
for state_number in range(len(height_states)-1):
    initial_height = height_states[state_number]
    next_height = height_states[state_number+1]
    next_subject = subjects_states[state_number+1]

    height_diff = np.array(next_height) - np.array(initial_height)
    
    for frame_number in range(n_frames + 1):
        temp_height = (initial_height + (height_diff / n_frames) * frame_number)
        
        fig = plt.figure(figsize=(15,8), linewidth=8, edgecolor="black", facecolor = 'white')
        plt.bar(x, temp_height, color=['sienna', 'sienna', 'sienna', 'grey', 'goldenrod'], edgecolor='black')
        plt.ylim(0,7.5)
        frame_name = f'frame_{state_number}_{frame_number}.png'
        frames.append(frame_name)
        
        if state_number > 0 and frame_number!= n_frames:
            for bar_number, bar_text in enumerate(next_height):
                if height_diff[bar_number] == 0:
                    plt.annotate(str(bar_text), xy=(bar_number,bar_text/2), 
                                 ha='center', va='bottom', size=20, color='white', weight='bold')
                    plt.annotate(str(next_subject[bar_number]), xy=(bar_number,bar_text+0.5), weight = 'normal',
                                 ha='center', va='bottom', size=18, color='black',family = 'monospace')
        
        if (frame_number == n_frames):
            for bar_number, bar_text in enumerate(next_height):
                plt.annotate(str(bar_text), xy=(bar_number,bar_text/2), 
                             ha='center', va='bottom', size=20, color='white', weight='bold')
                plt.annotate(str(next_subject[bar_number]), xy=(bar_number,bar_text+0.5), weight = 'normal', 
                             ha='center', va='bottom', size=18, color='black', family = 'monospace')
            for i in range(20):
                frames.append(frame_name)

        plt.title('Pódio de assuntos mais estudados por cientistas de dados \n da Loft nos últimos meses (por quantidade de menções)',
                  size=18, weight = 'bold', color = 'black', family = 'monospace')
        
        plt.axis('off')
        plt.savefig(frame_name, pad_inches=0.3, bbox_inches = 'tight',facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())
        plt.close()


with imageio.get_writer('most_studied_subjects_podium_final.gif', mode='I') as writer:
    for frame_name in frames:
        image = imageio.imread(frame_name)
        writer.append_data(image)


for frame_name in set(frames):
    os.remove(frame_name)