from numpy import *

# The python code is corresponding to Week 3 of Operations Analytics class.

# One question with this problem - Why can't we use the confidence interval to justify the probabily of getting a higher data usage than 20?
def dataplan():
    mu = 23; sigma = 5; N = 100
    #Us = random.normal(mu, sigma, N)
    Us = [14, 21.7, 26.1, 22.1, 28.6] 
    #Us = [14.6, 27.4, 19.6, 30.8, 25.6] 
    P = [] 
    for U in Us:
        if U > 20:
            P.append(160 + 15 * (U - 20))
        else:
            P.append(160)
    Pm = mean(P); Pstd = std(P)
    Pstd2 = std(Us) * 10
    print("The average price is %s" % (Pm))
    print("The std price is %s" % (Pstd))
    print("The std old price is %s" % (Pstd2))

def bidding():
    mu = 12; sigma = 1; N = 5 
    Bs = random.normal(mu, sigma, N)
    P = []; A = 11.5
    for B in Bs:
        if B > A: 
            P.append(.5)
        else:
            P.append(0)
    Pm = mean(P); Pstd = std(P) 
    print("The average profit of A is %s" % (Pm))
    print("The std profit of A is %s" % (Pstd))

def pricing():
    lam = 147; N = 100
    Ds = random.poisson(lam, N)
    R = []; P = 10000
    for D in Ds:
        if D <= 150: 
            R.append(D * P)
    Rm = mean(R); Rstd = std(R)
    print("The mean revenue is %s" % (Rm))
    print("The std of revenue is %s" % (Rstd))
    Rm2 = (min(R) + max(R)) / 2
    Rstd2 = sqrt(((min(R) - Rm2)**2 + (max(R) - Rm2)**2)/2)
    print("The mean revenue is %s" % (Rm2))
    print("The std of revenue is %s" % (Rstd2))

def main():
    dataplan()
    #bidding()
    #pricing()

if __name__ == '__main__':
    main()
