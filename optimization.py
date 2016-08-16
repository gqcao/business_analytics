from numpy import *
from scipy.optimize import minimize 

# The python code is corresponding to Week 2 of Operations Analytics class.
# The updated version is written with class 

class optimization:
    def __init__(self):
        self.x0 = 0
        self.coeff = 0 
        self.cons = []
        self.bnds = (0, None)
    def costFunc(self, quant):
        total = sum([(x*y) for x,y in zip(self.coeff, quant)])
        return total
    def optimum(self):
        res = minimize(self.costFunc, self.x0, method='SLSQP', bounds=self.bnds, constraints=self.cons)
        x = [ round(elem) for elem in res.x]
        print x
        print("The minimum cost is %s" % (round(res.fun)))
    def sumShipping(self, arr, idx):
        return arr[idx] + arr[idx + 3] + arr[idx + 6] 

class zooter(optimization):
    def __init__(self):
        self.x0 = [100, 500]
        self.coeff = [-150, -160]
        # ineq indicates larger than.. 
        self.cons = ({'type': 'ineq', 'fun': lambda x:  5610 - 4*x[0] - 5 * x[1]},
        {'type': 'ineq', 'fun': lambda x: 2200 - 1.5 *x[0] - 2 * x[1]},
        {'type': 'ineq', 'fun': lambda x: 1200 - x[0] - .8 * x[1]})
        self.bnds = [(0, None)] * len(self.x0)

class rahat(optimization):
    def __init__(self):
        self.x0 = [10, 10, 10]
        self.coeff= [-5, -5.3]
        self.cons = ({'type': 'ineq', 'fun': lambda x:  150 - .1 *x[0] - .3 * x[1]},
        {'type': 'ineq', 'fun': lambda x: 51.65 - .05 * x[0] - .1 * x[1]},
        {'type': 'ineq', 'fun': lambda x: 14.99 - .03 * x[0] - .02 * x[1]})
        self.bnds = [(0, None)] * len(self.x0) 

class keystone(optimization):
    def __init__(self):
        self.x0 = zeros(9)
        self.cons = ({'type': 'ineq', 'fun': lambda x: self.sumShipping(x, 0) - 10 },
                {'type': 'ineq', 'fun': lambda x: self.sumShipping(x, 1) - 13 },
                {'type': 'ineq', 'fun': lambda x: self.sumShipping(x, 2) - 20 },
                {'type': 'eq', 'fun': lambda x: sum(x[:3]) - 15 },
                {'type': 'eq', 'fun': lambda x: sum(x[3:6]) - 20 },
                {'type': 'eq', 'fun': lambda x: sum(x[6:9]) - 30 })
        self.coeff = [105, 135, 153, 110, 140, 137, 130, 132, 115]
        self.bnds = [(0, None)] * len(self.x0) 

class colombi(optimization):
    def __init__(self):
        self.x0 = zeros(6)
        # Objective function
        self.cons = ({'type': 'ineq', 'fun': lambda x: x[0] + x[3] - 2000 },
                {'type': 'ineq', 'fun': lambda x: x[1] + x[4] - 930 },
                {'type': 'ineq', 'fun': lambda x: x[2] + x[5] - 2200 },
                {'type': 'eq', 'fun': lambda x: sum(x[:3]) - 2500 },
                {'type': 'eq', 'fun': lambda x: sum(x[3:6]) - 2630 })
        self.bnds = [(0, None)] * len(self.x0) 
        self.coeff = [15, 21, 17, 23.5, 25.5, 22]

def main():
    #opt = rahat()
    opt = zooter()
    #opt = keystone()
    #opt = colombi()
    opt.optimum() 

if __name__ == '__main__':
    main()
