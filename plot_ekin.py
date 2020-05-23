import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    ekin = [125,112,101,91,84,77,72,67,63,59]
    n = np.linspace(0.012,0.03,10)
    ekin_t = 2/n

    plt.figure()
    plt.plot(n,ekin,label='Maximal kinetic energy from simulation')
    plt.plot(n,ekin_t,label ='Maximal theoretical value')
    plt.legend()
    plt.xlabel(r'n' + ' (code units)')
    plt.ylabel(r'$E_{kin}$'+ ' (code units)')
    plt.show()
