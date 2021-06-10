import plotly.graph_objects as go
import numpy as np

def waterfall_plot(cashflow, label=""):
    n = cashflow.shape[0]
    fig = go.Figure(
        go.Waterfall(
            name="",
            orientation="v",
            measure=["absolute"] * n,
            x=["Mês " + str(x) for x in range(n)],
            textposition="outside",
            y=cashflow,
            connector={"line": {"width": 0,"color": "black"}},
            totals = {"marker":{"color":"#ff774a", "line":{"color":"black", "width":1}}}
        )
    )
    fig.update_layout(
        title={"text": label, "x": 0.5, "xanchor": "center"}, showlegend=False,
    )
    fig.show()

#example
waterfall_plot(np.array([-100,20,30,60]),label='Cashflow')  
