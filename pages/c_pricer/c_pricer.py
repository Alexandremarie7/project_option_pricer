import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

layout = dbc.Container(
    [html.H1("Call pricer"),
     dbc.Row( dcc.Graph(figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}))]
)