import yfinance as yf
from datetime import datetime
import pandas as pd
import math
import numpy as np

Date_5=f"2017{str(datetime.now().date())[-6:]}"

stocks = pd.read_csv("./data/CAC40_tickers_v2.csv", on_bad_lines="skip", delimiter=";")


y_tickers = yf.Tickers(list(stocks["Symbol"].values))
stocks_data = y_tickers.history(start=Date_5)







# import arch
# from arch import arch_model
# import matplotlib.pyplot as pyplot

# test['Return'] = 100*(test['ACA.PA'].pct_change())

# test.dropna(inplace=True)

# pyplot.plot(test['Return'], label = 'Daily Returns')
# pyplot.legend(loc='upper right')
# pyplot.title('Daily Returns Over Time')

# daily_volatility = test['Return'].std()

# monthly_volatility = math.sqrt(21) * daily_volatility

# print()

# annual_volatility = math.sqrt(252) * daily_volatility

# from arch import arch_model
# from arch.__future__ import reindexing

# garch_model = arch_model(test['Return'], p = 1, q = 1,
#                       mean = 'constant', vol = 'GARCH', dist = 'normal')

# gm_result = garch_model.fit(disp='off')
# print(gm_result.params)

# print('\n')

# gm_forecast = gm_result.forecast(horizon = 3)
# print(gm_forecast)

# rolling_predictions = []
# test_size = 365

# for i in range(test_size):
#     train = test['Return'][:-(test_size-i)] #Définition du dataset à utiliser (toutes les données - celles à prédire)
#     model = arch_model(train, p=1, q=1) #création du modèles 
#     model_fit = model.fit(disp='off')
#     pred = model_fit.forecast(horizon=1) #Prédiction pour le jour à venir 
#     rolling_predictions.append(np.sqrt(pred.variance.values[-1,:][0])) #Ajout de la prédiction journalière 
    
# rolling_predictions = pd.Series(rolling_predictions, index=test['Return'].index[-365:]) #Mise en forme de la série de prédiction

# fig,ax = pyplot.subplots(figsize=(10,4))
# ax.spines[['top','right']].set_visible(False)
# pyplot.plot(rolling_predictions)
# pyplot.title('Rolling Prediction')


# fig,ax = pyplot.subplots(figsize=(13,4))
# ax.grid(which="major", axis='y', color='#758D99', alpha=0.3, zorder=1)
# ax.spines[['top','right']].set_visible(False)
# pyplot.plot(test['Return'][-365:])
# pyplot.plot(rolling_predictions)
# pyplot.title('Tesla Volatility Prediction - Rolling Forecast')
# pyplot.legend(['True Daily Returns', 'Predicted Volatility'])

# pyplot.show()