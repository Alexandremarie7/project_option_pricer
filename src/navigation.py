import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from pages import *

navbar = dbc.NavbarSimple( #LA bar de navigation présente en haut de page
    children=[
        dbc.NavItem(dbc.NavLink("Option Pricer", href="/opt_pricer")), #Lien menant vers le pricer
        dbc.NavItem(dbc.NavLink("Methodology", href="/methodology")), #Explicatioon de son fonctionnement
        dbc.NavItem(dbc.NavLink("Ressources", href="/ressources")), #Liens et ressources ayant permi la réalisation de cet outil
    ],
    brand=html.A(html.A("European Option Pricer Project")), #Titre de la navbar
    brand_href="/opt_pricer", #Page par défaut
    color="dark",
    dark=True,
)