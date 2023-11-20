import numpy as np
from scipy.stats import norm

#S0 = input("Quelle est la valeure de S0 ?")
#K = input("Quelle est la valeure de K ?")
#r = input("Quelle est la valeure de r ?")
#delta = input("Quelle est la valeure de delta ?")
#T = input("Quelle est la valeure de T ?")
#sigma = input("Quelle est la valeure de sigma ? (optionnel)")


def call (S0, K, r, delta, T, sigma) :
    if sigma != 0 and type(sigma) != "<class 'str'>" :
        S0 = S0*np.exp(-sigma*T)
    PVK = K*np.exp(-r*T)
    D1=(np.log(S0/K)+(r+delta**2/2)*T)/(delta*np.sqrt(T))
    D2=D1-delta*np.sqrt(T)
    call=S0*norm.cdf(D1)-PVK*norm.cdf(D2)
    return call

def put (S0, K, r, delta, T, sigma) :
    if sigma != 0 and type(sigma) != "<class 'str'>" :
        S0 = S0*np.exp(-sigma*T)
    PVK = K*np.exp(-r*T)
    D1=(np.log(S0/K)+(r+delta**2/2)*T)/(delta*np.sqrt(T))
    D2=D1-delta*np.sqrt(T)
    put=PVK*norm.cdf(-D2)-S0*norm.cdf(-D1)
    return put