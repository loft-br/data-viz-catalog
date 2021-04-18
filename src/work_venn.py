from matplotlib_venn import venn2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,12))
venn = venn2(
    subsets=[29, 9, 62], 
    set_labels=('',''), 
    set_colors=("#618eb8", "#f0620a"),
    alpha=0.7
)

for text in venn.set_labels:
    text.set_fontsize(16)
    text.set_fontfamily('monospace')

for i, text in enumerate(venn.subset_labels):
    if text:
        if i==1:
            text.set_position((0.7,0))
        text.set_fontsize(20)
        text.set_fontfamily('monospace')

id_list = ['10', '01', '11']      

for circle_id in id_list:
    venn.get_patch_by_id(circle_id).set_edgecolor('black')
    
venn.get_label_by_id('10').set_text('Apenas\n remoto\n(29%)')
venn.get_label_by_id('01').set_text('Apenas\n presencial\n(9%)')
venn.get_label_by_id('11').set_text('Meio a meio\n(62%)')

venn.get_patch_by_id('10').set_facecolor('#20a483')


plt.title('Modalidade de trabalho preferida', family='monospace', size=20, y=0.97)

plt.annotate(
    ' ', 
    xy=venn.get_label_by_id('01').get_position() + np.array([0.05, -0.05]),
    xytext=(100,-60),
    ha='center',
    textcoords='offset points',
    arrowprops=dict(
        arrowstyle='->', 
        connectionstyle='arc3,rad=0.5',
        color='black',
        lw='2'
    )
)

plt.savefig('work_venn.jpg', bbox_inches='tight')