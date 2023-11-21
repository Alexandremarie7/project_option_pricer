import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from data.divers import *

dash.register_page(
    __name__,
    path='/ressources',
    title='Useful ressources',
    name='Useful ressources',
)

layout = html.Label('Ressources')