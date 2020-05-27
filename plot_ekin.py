import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    ekin = [125,112,101,91,84,77,72,67,63,59]
    n = np.linspace(0.012,0.03,10)
    ekin_t = 2/n

    fig, ax = plt.subplots(nrows=1, ncols=2,figsize=(10,5))
    #fig.set_figsize([10,10])
    
    ax[0].plot(n,ekin,'.',label='Maximal kinetic energy from simulation')
    ax[0].plot(n,ekin_t,'*',label ='Maximal theoretical value')
    ax[0].legend()
    ax[0].set_title('Kinetic energy')
    ax[0].set_xlabel(r'n' + ' (code units)')
    ax[0].set_ylabel(r'$E_{kin}$'+ ' (code units)')


    E_max = np.array([0.17,0.18,0.19,0.195,0.209,0.218,0.22,0.247,0.243,0.236])
    lambda_p = np.array([76,72,67,60,56.8,53.8,52.4,52.2,42.98,43.48])
    L_acc = np.array(ekin)/E_max
    L_acc_t = 2/n**(3/2)
    vg = np.sqrt(1-n)
    L_acc_ = (lambda_p/4)*(1/np.sqrt(1-vg**2))

    ax[1].plot(n,L_acc_,'.',label=r'$L_{acc}$' + ' from simulation')
    ax[1].plot(n,L_acc_t,'*',label = 'Theoretical ' + r'$L_{acc}$')
    #ax[1].plot(n,L_acc,'*',label = 'Theoretical ' + r'$L_{acc}$')
    ax[1].set_ylabel(r'$L_{acc}$' + ' (code units)')
    ax[1].set_xlabel(r'n' + ' (code units)')
    ax[1].set_title('Acceleration length')
    ax[1].legend()
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    fig.suptitle('Acceleration parameters as a function of electron density n',fontsize=16,y=0.98)#,x =0.58)





    plt.show()
