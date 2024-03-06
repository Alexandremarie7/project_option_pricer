#File to collect risk free rate data and to make it easier to manipulate

from bs4 import BeautifulSoup as bs
import requests
import plotly.graph_objects as go

maturities = ['1-month', #Wanted maturties
              '3-months',
              '6-months',
              '9-months',
              '1-year',
              '2-years',
              '3-years',
              '4-years',
              '5-years'
              ]

def get_rates () :  #TO scrap the website
    rates = [] #Rates that will be added one by one
    for x in maturities :
        url = 'http://www.worldgovernmentbonds.com/bond-historical-data/germany/' + x #Add the wanted maturity to the URL
        soup = bs(requests.get(url).text, 'html') #Scap the page
        data= soup.find_all("div", class_ ="w3-cell") #Search for the html container that have the rate
        percent_loc = str(data).find("%") #Find the position of the % symbol in the string 
        percent = str(data)[percent_loc-5:percent_loc] #Collect the 5 characters before the % symbol (i.e. the rate)
        rates.append(percent) #Add it to the list

    return rates

rates = get_rates () #Store the rates in a variable to use it for the graph

def graph_yield_curve () : #Produce the yield curve graph for the german risk free rates
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


def find_adjusted_rate (time_period) : #This function is to select the best maturity in function of the nb of trading days to have the corresponding risk free rate
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