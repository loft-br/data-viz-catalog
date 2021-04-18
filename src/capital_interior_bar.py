import pandas as pd
import matplotlib.pyplot as plt
import imageio
import os


proportion_states = [[50, 50],
                     [60,40]]

names = ["Capital", "Interior"]

n_frames = 10
frames = []

for prop_state in range(len(proportion_states)-1):
    initial_prop = proportion_states[prop_state]
    next_prop = proportion_states[prop_state+1]
    
    width_diff = np.array(next_prop) - np.array(initial_prop)
    
    for frame_number in range(n_frames + 1):
        temp_width = (initial_prop + (width_diff / n_frames) * frame_number)

        df = pd.DataFrame(np.array([temp_width]),
                   columns=names)
        df.plot.barh(stacked=True, color = ["#ff774a", "#20a483"], figsize=(16,5), position=0.3)

        plt.legend(fontsize = 15, ncol = len(names), loc = 'lower center', bbox_to_anchor = (0.5, 0.1))
        plt.axis('off')
        plt.title('Proporção de origem de nascimento de cientistas de dados \n da Loft entre Capital e Interior',
                  size=18, weight = 'bold', color = 'black', family = 'monospace')
    
        frame_name = f'frame_{prop_state}_{frame_number}.png'
        frames.append(frame_name)
    
        for prop_number, prop_text in enumerate(temp_width):
            if prop_number == 0:
                plt.annotate(f'{int(prop_text)}%', xy=(25,0.05), family = 'monospace',
                             ha='center', va='bottom', size=25, color='white', weight='bold')
            else:
                plt.annotate(f'{int(prop_text)}%', xy=(75,0.05), family = 'monospace',
                             ha='center', va='bottom', size=25, color='white', weight='bold')
                    
            for i in range(1):
                frames.append(frame_name)
        
        #add extra time in the end
        if frame_number == n_frames:
            for i in range(15):
                frames.append(frame_name)
        
        #add extra time in the beginning
        if frame_number == 0:
            for i in range(5):
                frames.append(frame_name)
            
        axes = plt.gca()
        axes.set_ylim([-0.5,0.5])
        plt.savefig(frame_name, pad_inches=0.3, bbox_inches = 'tight')
        plt.close()


with imageio.get_writer('capital_interior.gif', mode='I') as writer:
    for frame_name in frames:
        image = imageio.imread(frame_name)
        writer.append_data(image)


for frame_name in set(frames):
    os.remove(frame_name)  