from bs4 import BeautifulSoup as bs
import requests
import plotly.graph_objects as go

maturities = ['1-month',
              '3-months',
              '6-months',
              '9-months',
              '1-year',
              '2-years',
              '3-years',
              '4-years',
              '5-years'
              ]

def get_rates () : 
    rates = []
    for x in maturities :
        url = 'http://www.worldgovernmentbonds.com/bond-historical-data/germany/' + x
        soup = bs(requests.get(url).text, 'html')
        data= soup.find_all("div", class_ ="w3-cell")
        percent_loc = str(data).find("%")
        percent = str(data)[percent_loc-5:percent_loc]
        rates.append(percent)

    return rates

rates = get_rates ()

def graph_yield_curve () :
    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=maturities,
            y=rates,
            text=rates,
            mode='lines+markers',
            name='German Yield Curve'
        ))
    

    fig.update_layout(title='German Yield Curve (risk-free rates)',
                      autotypenumbers='convert types',
                      xaxis_title='Maturity',
                      yaxis_title='Yield Rate',
                      )

    return fig


def find_adjusted_rate (time_period) :
    if time_period <23 :
        adjusted_rate = rates[0]
    elif time_period >22 and time_period <67 :
        adjusted_rate = rates[1]
    elif time_period >66 and time_period <133 :
        adjusted_rate = rates[2]
    elif time_period >132 and time_period <198 :
        adjusted_rate = rates[3]
    elif time_period >197 and time_period <253 :
        adjusted_rate = rates[4]
    elif time_period >252 and time_period <505 :
        adjusted_rate = rates[5]
    elif time_period >504 and time_period <757 :
        adjusted_rate = rates[6]
    elif time_period >756 and time_period <1009 :
        adjusted_rate = rates[7]
    elif time_period >1008 and time_period <1261 :
        adjusted_rate = rates[8]
    return adjusted_rate