#from cutecharts.globals import use_jupyter_lab; use_jupyter_lab() - if using JupyterLab
from cutecharts.charts import Pie
import imageio

chart = Pie('Biscoito ou Bolacha (%)',width='500px',height='600px')
chart.set_options(
    labels=list(['Bolacha', 'Biscoito', 'Tanto faz']),
    inner_radius=0,
    colors = ["#ff774a", "#20a483","#918f8e"],
    legend_pos = 'upRight',
    font_family = 'monospace'
 )
chart.add_series(list([71.4, 14.3, 14.3])) 

#chart.load_javascript() - if using JupyterLab

#chart.render_notebook() - if using JupyterLab
chart.render()

#save each interactive state of the chart as picture using screencapture or selenium package. 
#we used screeshots since we only had 3 states in the pie: cute_charts_{picture_number}.png

cute_frames = []
for number in range(3):
    for i in range(10):
        cute_frames.append(f'cute_charts_{number + 1}.png')
        
with imageio.get_writer('biscoito_bolacha.gif', mode='I') as writer:
    for frame_name in cute_frames:
        image = imageio.imread(frame_name)
        writer.append_data(image)