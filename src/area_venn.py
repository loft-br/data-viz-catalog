import matplotlib.pyplot as plt
from matplotlib_venn import venn3

plt.figure(figsize=(12,8))

venn = venn3(subsets = [80, 10, 5, 0, 5, 0, 0], set_labels = ('Exatas\n(%)', 'Humanas\n(%)', 'Biológicas\n(%)'), 
             set_colors = ("#618eb8", "#f0620a", "#599c4b"), alpha = 0.7)

for text in venn.set_labels:
    text.set_fontsize(16)
    text.set_fontfamily('monospace')

for i, text in enumerate(venn.subset_labels):
    if text:
        if i==0:
            text.set_position((0.05,0))
        text.set_fontsize(20)
        text.set_fontfamily('monospace')

plt.savefig('area_venn.jpg', bbox_inches='tight')