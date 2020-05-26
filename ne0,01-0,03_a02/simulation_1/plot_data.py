import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    ex = np.genfromtxt('./Ex.csv')
    rho = np.genfromtxt('./Rho.csv')
    x = np.genfromtxt('./x.csv')

    fig, ax1 = plt.subplots()
    fig.suptitle('Plasma wake')

    color = 'tab:red'
    ax1.set_xlabel('z (code units)')
    ax1.set_ylabel('E-field (code units)', color=color)
    ax1.plot(x, ex,'--', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Charge density (code units)', color=color)  
    ax2.plot(x, rho, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(-0.2,0.2)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.subplots_adjust(top=0.9)
    fig.suptitle('High electric field amplitude plasma wake',fontsize=16,y=0.98)


    ekin_x = np.genfromtxt('./Ekin_x.csv')
    ekin = np.genfromtxt('./Ekin.csv')
    plt.figure()
    plt.plot(ekin_x,np.log(ekin))
    plt.xlabel('Kinetic energy (code units)')
    plt.ylabel('Logaritmic number density (code units)')
    plt.title('Electron energy spectrum',fontsize=16)




    plt.show()

    '''
    plt.figure()
    plt.plot(ex/np.max(abs(ex)),'r--',label='Ex-field')
    plt.plot(rho/np.max(abs(rho)),'b-',label='Charge density')
    plt.legend()
    plt.show()
    '''
