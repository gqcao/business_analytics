#! /usr/bin/env python

from numpy import *
from scipy.optimize import minimize 

def profitFunc(quantity, nArgs):
    price = 12; unit_cost = 3
    profits = []
    for n in range(N):
        profits.append(round(price * min(quantity, demands[n]) - unit_cost * quantity, 2))
    return (- mean(profits), std(profits), profits)[nArgs]

def newsvendor():
    quantity0 = 60
    # Objective function
    cons = ({'type': 'ineq', 'fun': lambda x: 125 - profitFunc(x, 1)})
    bnds = [(0, None)]
    res = minimize(profitFunc, quantity0,  args=(0), method='SLSQP', bounds=bnds,
        constraints=cons)
    x = round(res.x, 1)
    return x, - profitFunc(x, 0) 

def calcProfits():
    global N
    global demands
    N = 100
    mu = 52.81; sigma = 15.1
    demands = random.normal(mu, sigma, N)
    quantity_opt, profit_opt = newsvendor()
    profits = profitFunc(quantity_opt, 2)
    print("The optimal quantity to purchase into the stock is %s" % (str(quantity_opt)))
    return demands, profits

def plots(demands, profits):
    import matplotlib.pyplot as plt
    bins = linspace(0, 100, N)
    f = plt.figure(1)
    plt.plot(bins, demands, 'ro', bins, demands, 'k')
    plt.hist(demands, bins, alpha=.6)
    f.show()
    g = plt.figure(2)
    plt.plot(bins, profits, 'go', bins, profits, 'k')
    g.show()
    raw_input()

def main():
    demands, profits = calcProfits()
    #plots(demands, profits)

if __name__ == '__main__':
    main()
