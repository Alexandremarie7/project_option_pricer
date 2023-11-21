import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, State


import data.formules_black_scholes as fx
from data.divers import *
from data.stock_data import *
from data.formules_black_scholes import *
from data.pricer_template import *
from data.risk_free_rates import *
from pages.opt_pricer.callbacks import *



dash.register_page(
    __name__,
    path="/opt_pricer",
    title="Option Pricer",
    name="Option Pricer",
)

#figure=dcc.Graph(id='graph_prix',figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]})

title = dbc.Row([dbc.Col(""),
                 dbc.Col(
                     dbc.Card(
                         dbc.CardBody(
                             html.H1("Option Pricer",
                                     className="mt-2 text-center"
                                                      )))),
                dbc.Col("")
                ])


parameters = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.H4(children="Parameters to fill :"),
                    html.Div(
                        [
                            r_space,
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Label("Stock To Choose"),
                                        lg=4,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        html.Label("Strike Price"),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        html.Label("Select Expiration Date (max 5 years from now)",
                                                   ),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                         html.Label("Select Risk Free Rate"),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                         html.Label("Enter stock volatility (OPTIONAL)"),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    )
                                ]
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id="company-choice",
                                            multi=False,
                                            options=stocks["Nom"],
                                            placeholder="Select a stock",
                                        ),
                                        lg=4,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        dbc.Input(
                                            id="strike-price",
                                            type="number",
                                            value=0,
                                            placeholder="Enter the price here"
                                        ),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    
                                    ),
                                    dbc.Col(
                                        dbc.Row([
                                            dbc.Col(
                                                dbc.Input(
                                                    id='number-period',
                                                    type='number',
                                                    min=0,
                                                    max=1261,
                                                    value=0
                                                ),
                                                lg=5,
                                                md=1,
                                            ),
                                            dbc.Col(
                                                dbc.Select(
                                                    ["Days", "Months", "Years"],
                                                    id='period-choice',
                                                    value='Days'
                                                )
                                            )
                                        ]),
                                        lg=2,
                                        md=4,
                                        sm=12,  
                                    ),   
                                    dbc.Col(
                                        dbc.Input(
                                            id="user-rate",
                                            type="number",
                                            #value=0,
                                            placeholder="in %"
                                        ),
                                        lg=2,
                                        md=4,
                                        sm=12,
                                    ),
                                    dbc.Col(
                                        dbc.Input(
                                            id="user-volatility",
                                            #value=0,
                                            placeholder='in %',
                                            type='number')
                                    )
                                ]
                            ),
                            

                        ],
                    ),
                    r_space,
                    dbc.Row([
                        dbc.Col(
                            html.H4(children="Type of volatility :")
                        ),
                        dbc.Col(
                            html.H4(children="Type of risk-free rate :")
                        )
                    ]),
                    r_space,
                    dbc.Row([
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "User's volatility", "value": 1},
                                    {"label": "Historical volatility (over same period of time as the expiration date)", "value": 2},
                                    {"label": "Historical volatility (based on the volatility of past 5 years)", "value": 3},
                                    {"label": "GARCH model predicted volatility", "value": 4}
                                    ],
                                value=1,
                                id="volatility-selector-type"
                            )
                        ),
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "User's rate", "value": 1},
                                    {"label": "Automatiezd risk-free rate (German Bonds adjusted to maturity)", "value": 2},
                                    ],
                                value=1,
                                id="rate-selector-type"
                            )
                        )
                    ]),
                    r_space,
                    dbc.Row([
                        dbc.Col(
                            html.Div([
                                dbc.Button(
                                    "Search",
                                    id="put-pricer-button",
                                    n_clicks=0,
                                    color="primary"
                                    )
                                ],
                                style={"text-align": "center"},
                                className="p-3",
                            )
                        ),
                    ]),
                ]
            )
        ]
    ),
    class_name="mb-3",
)

import time

get_callbacks_pricer ()

# Informations = dbc.Card(
#                 dbc.CardBody(
                    


#                 )
# )

historical_layout = dbc.Card(dbc.CardBody([
                                dbc.Row([c_space,
                                        dbc.Col(dbc.Card(dbc.CardBody(html.H4("Historical Data",
                                                                    className="mt-2 text-center"
                                                                    )
                                        ))),
                                        c_space,
                                ]),
                                dcc.Loading(dcc.Graph(id='stock-graph', #style={'height': '70vh'})),
                                )),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.Card(dbc.CardBody([
                                            html.Label('Actual price : '),
                                            space,
                                            html.Label(id='last-price',
                                                       style={"font-weight": "bold"}
                                            )
                                        ]))
                                    ),
                                    dbc.Col(
                                        dbc.Card(dbc.CardBody([
                                            html.Label('Variation over last'),
                                            space,
                                            html.Label(id='nb-days'),
                                            space,
                                            html.Label('days :'),
                                            space,
                                            html.Label(id='variation-last-period')
                                        ]))
                                    )
                                ])
                    ]))

variable_layout = dbc.Row([
        dbc.Col(
            dbc.Card(dbc.CardBody([
                dbc.Row([c_space,
                        dbc.Col(dbc.Card(dbc.CardBody(html.H4("Risk-free rate",
                                                              className="mt-2 text-center"
                                                      )
                        ))),
                        c_space,
                ]),
                dcc.Loading(dcc.Graph(id='risk-free-graph',
                                      style={'height': '47.5vh'}
                                      )
                ),
                r_space,
                dbc.Card(dbc.CardBody([
                    html.Label('Here is the risk-free rate adjusted on german bonds'),
                    space,
                    html.Label(id='german-rates-adjusted',
                               style={"font-weight": "bold"}
                              ),
                    space,
                    html.Label('%')
                ])),
                r_space, r_space,
                html.Label('The german bond values are directly sourced via '),
                space,
                dcc.Link(html.Label('worldgovernmentbonds.com'),
                        href='www.worldgovernmentbonds.com'
                ),
                r_space, r_space,
                dbc.Row(
                    html.Label('See the risk-free-rates.py file to see the web scrapping technique',
                               style={"font-weight": "bold"}
                    )
                ),
                r_space  
            ]))
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                dbc.Row([c_space,
                        dbc.Col(dbc.Card(dbc.CardBody(html.H4("Volatility",
                                                              className="mt-2 text-center"
                                                            )
                        ))),
                        c_space,
                ]),
                dcc.Loading(dcc.Graph(id='prediction-graph',
                                      style={'height': '47.5vh'}
                                      )
                            ),
                dbc.Row([
                        dbc.Col(dbc.Card(dbc.CardBody([
                            html.Label('Historical volatility of past'),
                            space,
                            html.Label(id='nb-days-v2'),
                            space,
                            html.Label('days :'),
                            space,
                            html.Label(id='hist-vol-past-days',
                                       style={"font-weight": "bold"}),
                            space,
                            html.Label('%')
                        ])))
                    ,
                    r_space,
                    dbc.Col(dbc.Card(dbc.CardBody([
                            html.Label('Adjusted volatility of past'),
                            space,
                            html.Label(id='nb-days-v3'),
                            space,
                            html.Label('days : (5 years data sample)'),
                            space,
                            html.Label(id='hist-vol-5-years',
                                       style={"font-weight": "bold"}),
                            space,
                            html.Label('%')
                        ])))
                    ,
                    r_space,
                    dbc.Col(
                        dbc.Card(dbc.CardBody([
                            html.Label('GARCH preidcted volatility for next'),
                            space,
                            html.Label(id='nb-days-v4'),
                            space,
                            html.Label('days :'),
                            space,
                            html.Label(id='GARCH-vol',
                                       style={"font-weight": "bold"})
                        ]))
                    )
                ])

            ]))
        )
    ])

option_prices = dbc.Row([
    dbc.Col([
        dbc.Card(dbc.CardBody([
            dbc.Row([c_space,
                    dbc.Col(dbc.Card(dbc.CardBody(html.H4("Call Option",
                                                          className="mt-2 text-center")
                    ))),
                    c_space,
            ]),
            r_space,
            dbc.Card(
                dbc.CardBody([
                    html.Label('Price of the Call option :',
                            style = {'font-size': 19}
                    ),
                    space,
                    html.Label(id='call-price',
                            style={"font-weight": "bold",
                                    'font-size': 18,
                                    }
                    )
                ])),
            r_space,
            dcc.Graph(id='graph-call') 
        ])),
        r_space,
    ]),
    dbc.Col([
        dbc.Card(dbc.CardBody([
            dbc.Row([c_space,
                    dbc.Col(dbc.Card(dbc.CardBody(html.H4("Put Option",
                                                          className="mt-2 text-center")
                    ))),
                    c_space,
            ]),
            r_space,
            dbc.Card(dbc.CardBody([
                html.Label('Price of the Put option :',
                        style={"font-size": 19} 
                ),
                space,
                html.Label(id='put-price',
                          style={"font-weight": "bold",
                                'font-size': 18,
                                }
                )
            ])),
            r_space,
            dcc.Graph(id='graph-put') 
        ])),
        r_space,
    ])
])

layout = html.Div([
            dbc.Container([
                r_space,
                dbc.Row(title),
                r_space,
                dbc.Row(parameters),
                r_space,
                dbc.Row(historical_layout)
            ]),
            r_space,
            variable_layout,
            r_space,
            option_prices
        ])

    #  pricer_template(stock_ID,"ACA.PA", "ACA.PA", "ACA.PA"), #A tester
    #  dbc.Row(html.Div(id='price-graph')),
    #  dbc.Row(html.Div(id="put-price")),
    #  dbc.Row(html.Div(id='Stock-ID')),



#dbc.card(dbc.cardbody()) #pour faire un encadré 
#dbc.container () pour faire un corps centré en rognant sur les cotés
