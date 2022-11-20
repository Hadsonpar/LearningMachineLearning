import numpy as np

def load_data():
    data = np.loadtxt("data/dataset01.txt", delimiter=',')
    #data = np.loadtxt("data/dataset02.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def pies_mts(x):
    pies = float(x)
    pulgadas=pies*12
    #yardas=pies/3
    cm=pulgadas*2.54
    metros=cm/100
    return metros

def mts_pies(mts):
    m = mts * 3.28084
    return m


def formatNumber(number, decimals, espanol=True):
    if type(number) != int and type(number) != float:
        return number

    d={'.':',', ',':'.'}
    return ''.join(d.get(s, s) for s in f"{number:,.{decimals}f}") \
        if espanol \
        else f"{number:,.{decimals}f}"