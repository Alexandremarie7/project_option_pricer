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

layout = dbc.Container([
    r_space,
    dbc.Row([
        dbc.Col(html.Div(''),lg=3),
        dbc.Col(
            dbc.Card(dbc.CardBody(
                html.H1('Some useful links',
                        className="mt-2 text-center")
            ))
        ),
        dbc.Col(html.Div(''),lg=3)
    ]),
    r_space,
    dbc.Card(dbc.CardBody([
        dcc.Link(html.Label('GARCH model explication'),
                            href='https://machinelearningmastery.com/develop-arch-and-garch-models-for-time-series-forecasting-in-python/'
        ),
        r_space,
        dcc.Link(html.Label('Estimating the volatitlity in the Black & Scholes option pricing formula'),
                            href = 'https://machinelearningmastery.com/develop-arch-and-garch-models-for-time-series-forecasting-in-python/'
        ),
        r_space,
        dcc.Link(html.Label('A Youtube video for Dash basics'),
                            href = 'https://www.youtube.com/watch?v=7yAw1nPareM'
        ),
        r_space,
        dcc.Link(html.Label('A Youtube video for webscrapping with beautiful soup'),
                            href = 'https://www.youtube.com/watch?app=desktop&v=XVv6mJpFOb0&pp=ygUJI2JzNHVsb2Zp'
        )
    ]))
])