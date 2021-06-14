import plotly.graph_objects as go
import numpy as np

x = np.arange(100)
a = 5;
fig = go.Figure(data=go.Scatter(x=x, y=((x**2)/(4*a))))
fig.show()
input("Hello")