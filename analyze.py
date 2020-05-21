import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    ex = np.genfromtxt('./Ex.csv')
    rho = np.genfromtxt('./Rho.csv')
    x = np.genfromtxt('./x.csv')


    dx = x[1]-x[0]
    tol = 0.0001
    ex = np.array(ex)
    s = ex < tol
    b = ex > -tol
    t = s*b
    t = t==True
    x_ = x[t]
    t_ = t[t]
    t_[:] = 0

    ind=np.where(t==True)
    ind=ind[0]
    #integrate
    print(np.sum(abs(ex[ind[0]:ind[1]]))*dx/2)
    

    plt.figure()
    plt.scatter(x_,t_)
    plt.plot(x,ex/np.max(abs(ex)),'r--',label='ex')
    plt.plot(x,rho/np.max(abs(rho)),'b-',label='rho')
    plt.legend()
    plt.show()
