import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from data.divers import *

dash.register_page(
    __name__,
    path='/methodology',
    title='Methodology',
    name='Methodology',
)

data_methodology = [dbc.Row(html.H4('Collection of stocks data :')),
r_space,
dbc.Row(html.Label('All stocks data are from YahooFinance and are collected via the python library. It is then stored into a pandas DataFrame that includes all stocks informations for 40 stocks (closing price, opening price, highest intraday price, ...).')),
dbc.Row(html.Label('Then we use a plotly graph_object candlestick graph to vizualize the historical prices of the choosen stock. All the needed informations are contained in the same pandas DataFrame')),
dbc.Row(html.Label('Then, we select the latest closing price of the stock to diplay it, as well as the stock return for the same period of time of the option')),
]

volatility_methodology = [dbc.Row(html.H4('Volatility calculation :')),
r_space,
dbc.Row(html.Label('Volatility can a manual input of the user, or can be computed by 3 different methods : ')),
dbc.Row(html.Label('The first method is to compute the volatility on the same period of time as the option. If the user have decided on a option lasting a year, the volatility will be calculated over the daily return of the stock on last year.')),
dbc.Row(html.Label('The second method  is to compute the volatitlity over the whole available dataset (5 last years) and to adjust the value for the given period of time the user have selected for the option.')),
dbc.Row(html.Label('The last method is the most intersting :')),
dbc.Row(html.Label('We use a GARCH time-series model to predict the volatility over the option life based on the data collected over the past 5 years. To do so, we use the arch python library and we compute th evolatility for the number of trading days the user have selected, with garch model parameters (p=1, q=1).')),
html.Label('Those parameters were choosen based on a research paper available on the '),
space,
dcc.Link(html.Label('Ressources page'),
             href='/ressources'
)
]

rate_methodology = [dbc.Row(html.H4('Rate methodology :')),
r_space,
dbc.Row(html.Label('The risk-free rate can a manual input of the user, or can be computed automatically : ')),
html.Label('The BeautifulSoup library allows us to collect data by webscrapping the german government bills/bonds rates from'),
space,
dcc.Link(html.Label('worldgovernmentbonds.com'),
         href='http://www.worldgovernmentbonds.com'
),
dbc.Row(html.Label('. Then, the rate used for computation is the one corresponding to the closest maturity (if the option expiration is in 1.5 years, the rate applied will be the one for the 1 year bond)'))
]

option_methodology = [dbc.Row(html.H4('Option price computation methodology :')),
r_space,
dbc.Row(html.Label('Options prices are computed using the Black & Scholes formula with the selected parameters. Then the respective profits are ploted using basics plotly.scatterplot objects.'))
]

layout = dbc.Container([
    r_space,
    dbc.Row([
        dbc.Col(html.Div(''),lg=3),
        dbc.Col(
            dbc.Card(dbc.CardBody(
                html.H1('Presentation of our methodology',
                        className="mt-2 text-center")
            ))
        ),
        dbc.Col(html.Div(''),lg=3)
    ]),
    r_space,
    dbc.Card(dbc.CardBody([
        html.Div(data_methodology),
        r_space, r_space,
        html.Div(volatility_methodology),
        r_space, r_space,
        html.Div(rate_methodology),
        r_space, r_space,
        html.Div(option_methodology)
    ]))
])


