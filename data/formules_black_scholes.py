import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

#S0 = input("Quelle est la valeure de S0 ?")
#K = input("Quelle est la valeure de K ?")
#r = input("Quelle est la valeure de r ?")
#delta = input("Quelle est la valeure de delta ?")
#T = input("Quelle est la valeure de T ?")
#sigma = input("Quelle est la valeure de sigma ? (optionnel)")


def call (S0, K, r, delta, T) :
    # if sigma != 0 and type(sigma) != "<class 'str'>" :
    #     S0 = S0*np.exp(-sigma*T)
    PVK = K*np.exp(-r*T)
    D1=(np.log(S0/K)+(r+delta**2/2)*T)/(delta*np.sqrt(T))
    D2=D1-delta*np.sqrt(T)
    call=S0*norm.cdf(D1)-PVK*norm.cdf(D2)
    return call

def put (S0, K, r, delta, T) :
    # if sigma != 0 and type(sigma) != "<class 'str'>" :
    #     S0 = S0*np.exp(-sigma*T)
    PVK = K*np.exp(-r*T)
    D1=(np.log(S0/K)+(r+delta**2/2)*T)/(delta*np.sqrt(T))
    D2=D1-delta*np.sqrt(T)
    put=PVK*norm.cdf(-D2)-S0*norm.cdf(-D1)
    return put

def graph_call_profit (st, k, premium, company):
    sT = np.arange(0.7*st,1.3*st,1)
    payoff_call = np.where(sT > k, sT - k, 0) - premium

    fig = go.Figure(
        data=go.Scatter(
            y=payoff_call,
            x=sT,
            name='Payoff representation of a long call position'
        )
    )

    fig.update_xaxes(
        title=f"{company}'s stock price",
        showgrid=False
    )

    fig.update_yaxes(
        title='P&L',
    )

    fig.update_layout(
        title=f"Payoff of a long call position on {company}",
        title_font_size=16,
    )

    return fig

def graph_put_profit (st, k, premium, company):
    sT = np.arange(0.7*st,1.3*st,1)
    payoff_call = np.where(k-sT, sT < k, 0) - premium

    fig = go.Figure(
        data=go.Scatter(
            y=payoff_call,
            x=sT,
            name='Payoff representation of a long put position',
        )
    )

    fig.update_xaxes(
        title=f"{company}'s stock price",
        showgrid=False
    )

    fig.update_yaxes(
        title='P&L',
    )

    fig.update_layout(
        title=f"Payoff of a long put position on {company}",
        title_font_size=16,
    )

    return fig
