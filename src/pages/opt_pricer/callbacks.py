from dash.dependencies import Input, Output, State
from dash import callback, Output, Input, State
from data.formules_black_scholes import *
from data.stock_data import *
from data.pricer_template import *
from data.risk_free_rates import *
import plotly.graph_objects as go

from server import app


def get_callbacks_pricer (): #Tous les cllbacks du pricer
    @callback(
        Output('stock-graph', 'figure'),
        Output('risk-free-graph', 'figure'),
        Output('risk-free-graph-histo', 'figure'),
        Output('last-price', 'children'),
        Output('nb-days', 'children'),
        Output('variation-last-period', 'children'),
        Output('german-rates-adjusted', 'children'),
        Output('call-price', 'children'),
        Output('put-price', 'children'),
        Output('graph-long-call', 'figure'),
        Output('graph-long-put', 'figure'),
        Output('graph-short-call', 'figure'),
        Output('graph-short-put', 'figure'),

        Input('put-pricer-button', 'n_clicks'),
        State('company-choice', 'value'),
        State('number-period', 'value'),
        State('period-choice', 'value'),
        State('rate-selector-type', 'value'),   
        State('volatility-selector-type', 'value'),
        State('user-rate', 'value'),
        State('user-volatility', 'value'),
        State('strike-price', 'value')
    )
    def option_price_producer(n_clicks : int, company, nb_period, period_type, type_rate, type_vol, user_rate, user_vol, strike_price):

        if period_type == 'Days' : #Calcul du nombre de jours en fonction du type de période donnée en entrée
            nb_days = nb_period
        elif period_type == 'Months' : #22 jours de trading dans un mois
            nb_days = nb_period * 22
        elif period_type == 'Years' :
            nb_days = nb_period * 252 #Nb de jours de cotation dans l'année

        temp_stock = stocks['Symbol'].loc[stocks["Nom"].str.contains(company)].iat[0] #Aller chercher  le ticker associée au nom de la société séléctionnée

        latest_price = get_stock_latest_price(temp_stock) #Dernier prix connu
        var_last_period = variation_rendering(round(get_stock_return(temp_stock, nb_days),2)) #Variation du cours sur la période de l'option

        adjusted_rates =  find_adjusted_rate(nb_days) #Taux allemand sans risque pour la période de l'option

        hist_vol_past_days = round(get_hist_volatility_given_period(temp_stock, nb_days),2) #Volatilité sur la période de l'option 
        hist_vol_5_years = round(get_hist_volatility(temp_stock, nb_days),2) #Volatilité sur 5 ans ajustée à la période de l'option
        

        graph_prix = graph_prix_stock (temp_stock, company) #Stock prices history
        graph_risk = graph_yield_curve () #Yield graph (German risk free rates)
        graph_histo_risk = graph_yield_curve_evolution () #Yield evolution graph

        
        if type_rate == 1 : #Risk-free rate choice
            final_rate = float(user_rate) #The one provided by the user
        else : 
            final_rate = float(adjusted_rates) #The one given by the german yield curve
        
        if type_vol == 1 : #User's vol
            final_vol = user_vol
        elif type_vol == 2 : #We take the historical volatility of the same period of time in the past
            final_vol = hist_vol_past_days
        elif type_vol == 3 : #We take the historical volatility of the past 5 years, adjusted for our number of days
            final_vol = hist_vol_5_years

        call_price = call (latest_price, strike_price, final_rate/100, final_vol/100, nb_days/252) #Computation of the call price

        
        put_price = put (latest_price, strike_price, final_rate, final_vol, nb_days/252) #Computation of the put price

        graph_long_call = graph_long_call_profit (latest_price, strike_price, call_price, company) #Production of the 4 graphs for each situation for each option
        graph_long_put = graph_long_put_profit (latest_price, strike_price, put_price, company)
        graph_short_call = graph_short_call_profit (latest_price, strike_price, call_price, company)
        graph_short_put = graph_short_put_profit (latest_price, strike_price, put_price, company)

        return [graph_prix,
                graph_risk,
                graph_histo_risk, 
                str(round(latest_price,2)) + ' €',
                nb_days,
                var_last_period,
                adjusted_rates,
                round(call_price, 2),
                round(put_price,2),
                graph_long_call,
                graph_long_put,
                graph_short_call,
                graph_short_put,
        ]