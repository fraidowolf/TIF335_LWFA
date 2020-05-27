import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    ex = np.genfromtxt('./Ex.csv')
    p = np.genfromtxt('./px.csv')
    py =  np.genfromtxt('./px_axis.csv')
    x = np.genfromtxt('./x.csv')

    #p= np.rot90(p)

    fig, ax1 = plt.subplots()
    fig.suptitle('Plasma wake')
    
 
    color = 'tab:red'
    ax1.set_xlabel('z (code units)')
    ax1.set_ylabel('E-field (code units)', color=color)
    ax1.plot(x, ex,'--', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
 

  
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Momentum (code units)', color=color)  
    im = ax2.imshow(np.log(np.flipud(p.T)),extent=[x[0],x[-1],py[0],py[-1]], aspect="auto",vmax=100)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(-80, 80)




    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.subplots_adjust(top=0.9)
    fig.suptitle('High electric field amplitude plasma wake',fontsize=16,y=0.98)
    #fig.colorbar(im,ax=[ax1],location='left')

    ekin_x = np.genfromtxt('./Ekin_x.csv')
    ekin = np.genfromtxt('./Ekin.csv')
    plt.figure()
    plt.plot(ekin_x,np.log(ekin))
    plt.xlabel('Kinetic energy (code units)')
    plt.ylabel('Logaritmic number density (code units)')
    plt.title('Electron energy spectrum',fontsize=16)

    plt.show()

