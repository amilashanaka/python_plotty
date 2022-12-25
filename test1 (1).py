
count= [23,17,35,29,12]
alert_type=['Critical', 'Warning', 'Info']

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "xy"}, {"type": "polar"}],
           [{"type": "domain"}, {"type": "scene"}]],
)
df = pd.DataFrame({
    "Type": ["Critical", "Warning", "Info"],
    "Count": [4, 1, 2,]
})

# data = px.bar(df, x="Type", y="Count", color = 'Type', color_discrete_sequence=['#A7171A', '#fed766', '#00b2ee'])

data = px.bar(df, go.Bar(y=count, x=alert_type))

fig.add_trace(data)

fig.add_trace(go.Barpolar(theta=[0, 45, 90], r=[2, 3, 1]),
              row=1, col=2)

fig.add_trace(go.Pie(values=[2, 3, 1]),
              row=2, col=1)

fig.add_trace(go.Scatter3d(x=[2, 3, 1], y=[0, 0, 0],
                           z=[0.5, 1, 2], mode="lines"),
              row=2, col=2)

fig.update_layout(height=700, showlegend=False)

fig.show()
