#The file that gather many ressources for graph/values productions 

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

import plotly.graph_objects as go
from math import *

from data.stock_data import *
from data.divers import *

from arch import arch_model
from arch.__future__ import reindexing


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

def GARCH_model_vol_prediciton_testing (stock, company, nb_days): #To test the GARCH model
    rolling_predictions = []
    test_size = nb_days
    Return = get_stock_total_return(stock)
    for i in range(test_size):
        train = Return[:-(test_size-i)] #Définition du dataset à utiliser (toutes les données - celles à prédire)
        model = arch_model(train,
                           p=1,
                           q=1,
                           mean = 'constant',
                           vol = 'GARCH',
                           dist = 'normal') #création du modèles 
        model_fit = model.fit(disp='off')
        pred = model_fit.forecast(horizon=1) #Prédiction pour le jour à venir 
        rolling_predictions.append(np.sqrt(pred.variance.values[-1,:][0])) #Ajout de la prédiction journalière 
    

    annualized_predicted_vol= sqrt((1/test_size)*sum(rolling_predictions)**2)

    rolling_predictions = pd.Series(rolling_predictions, index=Return.index[-nb_days:]) #Mise en forme de la série de prédiction

    fig = go.Figure(
        data=go.Scatter(
            y=Return[-nb_days:],
            x=Return[-nb_days:].index,
            name='True Daily Return'
        )
    )

    fig.add_trace(
        go.Scatter(
            y=rolling_predictions, #Mise en forme du graph de sortie
            x=rolling_predictions.index,
            name='Predicted Volatility',
            line=dict(width=4)
        )
    )

    fig.update_layout(
        title=f"{company}'s Volatility Prediction (GARCH Rolling Forecast over last year)",
        title_font_size=16,
        autosize=False,
        height=320,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(
        title='Date',
        showgrid=False
    )

    fig.update_yaxes(
        title='Variance',
    )

    return fig, annualized_predicted_vol

def GARCH_model_vol_prediciton (stock, nb_days): #To predict the volatility wth GARCH model for the option period
    Return = get_stock_total_return(stock)

    model = arch_model(Return,
                       p=1,
                       q=1,
                       mean='Zero',
                       vol = 'GARCH',
                       dist = 'normal') #création du modèles 
    model_fit = model.fit(disp='off')
    pred = model_fit.forecast(horizon=nb_days)#.variance #Prédiction pour le jour à venir 
    vol_predict = sqrt((sum(pred.variance.values[-1, :])**2)*(1/nb_days))


    return vol_predict

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