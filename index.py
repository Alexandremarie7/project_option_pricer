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


"""
A simply Dash multi-page app template by Karsten Eckhardt.
GitHub: https://github.com/R4h4/
Medium: https://medium.com/@karsteneckhardt
LinkedIn: https://linkedin.com/in/karsten-eckhardt/

Created at: 2019-05-26
"""

app.title = "Dash Application"

url_bar_navbar_content = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        children=[
            navigation.navbar,
            html.Div(id='page-content')
        ]
    )
])


# When developing a multi-page app, this part will ensure that all callbacks are validated before serving the app
# See: https://dash.plot.ly/urls
def serve_layout():
    if flask.has_request_context():
        return url_bar_navbar_content
    return 


app.layout = html.Div([
        url_bar_navbar_content,
        #home.layout,
    ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def routes(pathname):
    if pathname == '/':
        return home.layout
    elif pathname =="/opt_pricer" :
        return opt_pricer.layout
    elif pathname == "/c_pricer" :
        return methodology.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8065, debug=True, threaded=True)
