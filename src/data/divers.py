#Just a file to store some useful variable with dash layout. 

from dash import html
import dash_bootstrap_components as dbc

r_space = dbc.Row(html.P('')) #To make an empty row
c_space = dbc.Col(html.P('')) #To make an empty column
space = html.Label(style={'margin-left':'5px'}) #To make a space character between callbacks values & strings directly declared