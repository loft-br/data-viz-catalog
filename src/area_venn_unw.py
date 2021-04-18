import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted

plt.figure(figsize=(12,8))

venn_un = venn3_unweighted(subsets = [80, 10, 5, 0, 5, 0, 0], set_labels = ('Exatas (%)', 'Humanas(%)', 'Biológicas(%)'),
                           set_colors = ("#618eb8", "#f0620a", "#599c4b"), alpha = 0.6)

for text in venn_un.set_labels:
    text.set_fontsize(16)
    text.set_fontfamily('monospace')

for text in venn_un.subset_labels:
    if text:
        text.set_fontsize(20)
        text.set_fontfamily('monospace')

#plt.title("% de pessoas que relacionam seus cursos com as grandes áreas")
plt.savefig('area_venn_unw.jpg', bbox_inches='tight')