# -*- coding: utf-8 -*
import flask
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
from server import app, server  # Import server for Gunicorn
from pages import *
from data import *
import navigation

#Ceci est le fichier central, celui d'où est exécuté l'app

app=Dash(__name__,title="European Option Pricer")

server=app.server

app.title = "European Option Pricer"

url_bar_navbar_content = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        children=[
            navigation.navbar,
            html.Div(id='page-content')
        ]
    )
])

def serve_layout():
    if flask.has_request_context():
        return url_bar_navbar_content
    return 


app.layout = html.Div([ #L'affichage de la navbar
        url_bar_navbar_content,
    ])


@app.callback(Output('page-content', 'children'), #Les callback pour aller chercher les pages
              [Input('url', 'pathname')])
def routes(pathname):
    if pathname =="/opt_pricer" :
        return opt_pricer.layout
    elif pathname == "/methodology" :
        return methodology.layout
    elif pathname == "/ressources" :
        return ressources.layout
    else:
        return '404'


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8066, debug=True, threaded=True)
