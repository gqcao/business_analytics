from numpy import *
from scipy.optimize import minimize 

# The python code is corresponding to Week 2 of Operations Analytics class.

def zooter():
    x0 = [100, 500]
    # Objective function
    fun = lambda x: - 150 * x[0] - 160 * x[1]
    cons = ({'type': 'ineq', 'fun': lambda x:  5610 - 4*x[0] - 5 * x[1]},
    {'type': 'ineq', 'fun': lambda x: 2200 - 1.5 *x[0] - 2 * x[1]},
    {'type': 'ineq', 'fun': lambda x: 1200 - x[0] - .8 * x[1]})
    bnds = ((0, None), (0, None))
    res = minimize(fun, x0, method='SLSQP', bounds=bnds,
    constraints=cons)
    print res.x

def rahat():
    x0 = [10, 10, 10]
    # Objective function
    #fun = lambda x: - 5 * x[0] - 5.3 * x[1]
    cons = ({'type': 'ineq', 'fun': lambda x:  150 - .1 *x[0] - .3 * x[1]},
    {'type': 'ineq', 'fun': lambda x: 51.65 - .05 * x[0] - .1 * x[1]},
    {'type': 'ineq', 'fun': lambda x: 14.99 - .03 * x[0] - .02 * x[1]})
    bnds = [(0, None)] * 3
    res = minimize(costFunc, x0, method='SLSQP', bounds=bnds,
        constraints=cons)
    print res.x

def costFunc(quant):
    cost_keystone = [105, 135, 153, 110, 140, 137, 130, 132, 115]
    cost_colombi = [15, 21, 17, 23.5, 25.5, 22]
    cost_rahat = [-5, -5.3]
    cost = cost_rahat
    total = sum([(x*y) for x,y in zip(cost, quant)])
    return total

def sumShipping(arr, idx):
    return arr[idx] + arr[idx + 3] + arr[idx + 6] 

def keystone():
    x0 = zeros(9)
    # Objective function
    cons = ({'type': 'ineq', 'fun': lambda x: sumShipping(x, 0) - 10 },
            {'type': 'ineq', 'fun': lambda x: sumShipping(x, 1) - 13 },
            {'type': 'ineq', 'fun': lambda x: sumShipping(x, 2) - 20 },
            {'type': 'eq', 'fun': lambda x: sum(x[:3]) - 15 },
            {'type': 'eq', 'fun': lambda x: sum(x[3:6]) - 20 },
            {'type': 'eq', 'fun': lambda x: sum(x[6:9]) - 30 })
    bnds = [(0, None)] * 9
    res = minimize(costFunc, x0, method='SLSQP', bounds=bnds,
    constraints=cons)
    x = [ round(elem) for elem in res.x]
    print x
    print("The minimum cost is %s" % (costFunc(x)))

def colombi():
    x0 = zeros(6)
    # Objective function
    cons = ({'type': 'ineq', 'fun': lambda x: x[0] + x[3] - 2000 },
            {'type': 'ineq', 'fun': lambda x: x[1] + x[4] - 930 },
            {'type': 'ineq', 'fun': lambda x: x[2] + x[5] - 2200 },
            {'type': 'eq', 'fun': lambda x: sum(x[:3]) - 2500 },
            {'type': 'eq', 'fun': lambda x: sum(x[3:6]) - 2630 })
    bnds = [(0, None)] * 6 
    res = minimize(costFunc, x0, method='SLSQP', bounds=bnds,
        constraints=cons)
    x = [ round(elem) for elem in res.x]
    print x
    print("The minimum cost is %s" % (costFunc(x)))

def main():
    zooter()
    #rahat()
    #keystone()
    #colombi()

if __name__ == '__main__':
    main()
