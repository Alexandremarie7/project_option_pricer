import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from pages import *

logo = html.Img(src=dash.get_asset_url("logo.jpeg"), height="30px")

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Option Pricer", href="/opt_pricer")),
        dbc.NavItem(dbc.NavLink("Call Pricer", href="/c_pricer")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Our team", href="/our_team"), #Page menant à la présentation de notre équipe
                dbc.DropdownMenuItem("The github", href="https://www.lien vers le github"), #A modifier
                dbc.DropdownMenuItem("Useful ressources", href="/ressources") #Liens ayant permi la réalisation de cet outil
            ],
            nav=True,
            in_navbar=True,
            label="Credits",
        ),
    ],
    brand=html.A([html.A("Call & Put Pricer Project for this guy :   "),
                  logo
                  ]),
    brand_href="/",
    color="dark",
    dark=True,
)