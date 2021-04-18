from pywaffle import Waffle
from matplotlib import pyplot as plt

plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=[86, 9, 5],
    # Hexadecimal color
    colors=["#FFA500", "#4384FF", "#64228a"],
    # Specify icons for sunny days, showers, and snow
    icons=['python', 'r-project', 'h-square'],
    font_size=22,
    icon_style=['brands','brands', 'solid'],
    icon_legend=True,
    legend={
        'labels': ['Python (86%)', 'R (9%)', 'Haskell (5%)'], 
        'loc': 'lower center', 
        'bbox_to_anchor': (0.5, -0.3),
        'ncol': 3,
        'fontsize': 16
    },
    figsize=(14,6)
)

plt.title("Linguagem de programação favorita (%)", fontsize=18, family='monospace')
plt.savefig("programming_waffle.png", bbox_inches="tight")