from numpy import *
from scipy.optimize import minimize 

def profitFunc(quantity):
    price = 12; unit_cost = 3
    profit = []
    for n in range(N):
        profit.append(price * min(quantity, demand[n]) - unit_cost * quantity)
    return - mean(profit)

def profitFunc2(quantity):
    price = 12; unit_cost = 3
    profit = []
    for n in range(N):
        profit.append(price * min(quantity, demand[n]) - unit_cost * quantity)
    return std(profit)

def newsvendor():
    quantity0 = 60
    # Objective function
    cons = ({'type': 'ineq', 'fun': lambda x: 125 - profitFunc2(x)})
    bnds = [(0, None)]
    res = minimize(profitFunc, quantity0, method='SLSQP', bounds=bnds,
        constraints=cons)
    x = round(res.x, 1)
    print - profitFunc(x) 

def main():
    global N
    global demand
    N = 50
    mu = 52.81; sigma = 15.1
    demand = random.normal(mu, sigma, N)
    newsvendor()

if __name__ == '__main__':
    main()
