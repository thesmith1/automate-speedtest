import plotly as ply
import plotly.graph_objs as go


def plot_timeseries(x: list, y: list, legend: list, title='My Plot', filename='plot.html',
                    xaxis_title='X Axis', yaxis_title='Y Axis'):
    data = []
    for idx, tr in enumerate(x):
        trace = go.Scatter(x=tr, y=y[idx], name=legend[idx])
        data.append(trace)
    layout = go.Layout(title=title,
                       xaxis=dict(
                           title=xaxis_title,
                           autorange=True,
                           showticklabels=True
                       ),
                       yaxis=dict(
                           title=yaxis_title,
                           autorange=True,
                           showticklabels=True
                       ))
    ply.offline.plot({
        'data': data,
        'layout': layout
    }, auto_open=False, filename=filename)
