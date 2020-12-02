import plotly.graph_objects as go 
from ipywidgets import FloatSlider, BoundedFloatText, Dropdown
from IPython.display import display
import numpy as np
import math

# trace 1 
A_1 = FloatSlider(value = 1.0, min = 0.0, max = 10.0, step = 0.01, description = 'A_1 [V]')
Phi_1 = FloatSlider(value = 1.0, min = -360.0, max = 360.0, step = 0.01, description = 'Phi_1 [deg]')
f_1 = BoundedFloatText(value = 1.0, min = 0.0, max = 20.0, step = 0.01, description = 'f_1 [Hz]')
w_1 = FloatSlider(value = 1.0, min = 0.0, max = 100.0, step = 0.01, description = 'w_1 [Rad/s]')

# trace 2
A_2 = FloatSlider(value = 1.0, min = 0.0, max = 10.0, step = 0.01, description = 'A_2 [V]')
Phi_2 = FloatSlider(value = 1.0, min = -360.0, max = 360.0, step = 0.01, description = 'Phi_2 [deg]')
f_2 = BoundedFloatText(value = 1.0, min = 0.0, max = 20.0, step = 0.01, description = 'f_2 [Hz]')
w_2 = FloatSlider(value = 1.0, min = 0.0, max = 100.0, step = 0.01, description = 'w_2 [Rad/s]')

# use
use = Dropdown(options = ['FREQUENCY', 'FUNCTIONS'], value = 'FUNCTIONS', description = 'Use:')

display(A_1)
display(A_2)
display(Phi_1)
display(Phi_2)
display(f_1)
display(f_2)
display(w_1)
display(w_2)
display(use)

def calculate():
    if use.value == 'FUNCTIONS':
        value_1 = A_1.value * np.sin(w_1.value * t)
        value_2 = A_2.value * np.cos(w_2.value * t)
    else:
        value_1 = A_1.value * np.sin(2 * math.pi * f_1.value*t - Phi_1.value * np.pi/180)
        value_2 = A_2.value * np.cos(2 * math.pi * f_2.value*t - Phi_2.value * np.pi/180)
    return value_1, value_2

# parameters
t = np.arange(0.0, 10.0, 0.001)
y_1, y_2 = calculate()

# figure
data = [go.Scatter(y = y_1, x = t, opacity = 0.75, name = 'Trace 1'), go.Scatter(y = y_2, x = t, opacity = 0.75, name = 'Trace 2')]
layout = {'yaxis': {'range': [-2, 2], 'title': "CALCULATED VALUE"}, 'xaxis': {'range': [0, 10], 'title': "TIME"}}
fig = go.FigureWidget(data, layout)

fig