import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    ex = np.genfromtxt('./Ex.csv')
    rho = np.genfromtxt('./Rho.csv')

    print(rho)

    plt.figure()
    plt.plot(ex/np.max(abs(ex)),'r--',label='ex')
    plt.plot(rho/np.max(abs(rho)),'b-',label='rho')
    plt.legend()
    plt.show()
