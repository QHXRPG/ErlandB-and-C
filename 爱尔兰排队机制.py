"""Erland B、C"""
def jiecheng(s):
    a = 1
    for i in range(1,s+1):
        a = a*i
    return a

def P0(s,a):
    sum1 = 0
    for i in range(s):
        sum1 = sum1 + (a**i)/jiecheng(i)
    p0 = 1/(sum1 + ((a**s)/jiecheng(s))*(1/(1-(a/s))))
    return p0

def Lq(s,a):
    return ((a**s)*(a/s)*P0(s,a))/(jiecheng(s)*((1-(a/s))**(2)))

def P_C(s,a):
    return ((a**s)/(jiecheng(s))) * ((P0(s,a))/(1-(a/s)))

def P_B(s,a):
    fenzi = (a**s)/jiecheng(s)
    sum=0
    for i in range(s+1):
        sum = sum + (a**i)/(jiecheng(i))
    return fenzi/sum
