#The file that gather many ressources for graph/values productions 

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

import plotly.graph_objects as go
from math import *

from data.stock_data import *
from data.divers import *


def graph_prix_stock (stock, stock_name): #Produce the candlestick graph for the layout
    graph_prix = go.Figure(data=go.Candlestick(x=stocks_data.index,
                                            open=stocks_data['Open'][stock],
                                            high=stocks_data['High'][stock],
                                            low=stocks_data['Low'][stock],
                                            close=stocks_data['Close'][stock])) #Si problème ajouter un [] avant data et à la fin
    graph_prix.update_layout(title=f"Evolution of {stock_name}'s price during the 5 past years",
                            title_font_size=16,
                            autosize=False,
                            height=600,
                            )
    graph_prix.update_xaxes(title='Year',
                            )
    graph_prix.update_yaxes(title='Cours',
                            )
    return graph_prix

def get_stock_latest_price (stock): #In the name 
    latest_price = stocks_data['Close'][stock].iat[len(stocks_data['Close'][stock])-1]
    return latest_price

def get_stock_return (stock, nb_days) : #To obtain return on a giver period of time 
    price_period_before = stocks_data['Close'][stock][-nb_days:-(nb_days)+1].iat[-1]
    latest_price = get_stock_latest_price(stock)
    stock_return = 100*(latest_price-price_period_before)/price_period_before
    return stock_return

def get_stock_daily_return (stock, time_period) : #Used later for volatiltity computation
    daily_return = 100*(stocks_data['Close'][stock][-time_period:].pct_change())
    daily_return.dropna(inplace=True)
    return daily_return

def get_stock_total_return (stock) : #Useful for the GARCH model later
    total_return = 100*(stocks_data['Close'][stock].pct_change())
    total_return.dropna(inplace=True)
    return total_return

def get_hist_volatility_given_period (stock, time_period) : #To get the historical volatitlity on a given time period for a given stock
    vol = get_stock_daily_return(stock,time_period).std()
    vol = vol*sqrt(time_period)
    return vol

def get_hist_volatility (stock, time_period) : #To get the historical volatitlity for a given stock on the whole 5 years available dataset
    vol = get_stock_total_return(stock).std()
    vol = vol*sqrt(time_period)
    return vol

def variation_rendering (number) : #Just to have green for positive variation and red for negative one

    if number < 0 :
        converted = html.Label(
            ' ' + str(number) + ' %',
            style={'color': 'red',
                   'font-weight': 'bold'})
    else :
          converted = html.Label(
              ' +' + str(number) + ' %',
              style={'color': 'green',
                     'font-weight': 'bold'})
          
    return converted