import happi
import numpy as np
import json


if __name__=='__main__':

    s = happi.Open('./')
    ts = 21576
    ex = s.Field(0,'Ex',timesteps=ts).getData()
    ex_x = s.Field(0,'Ex',timesteps=ts).getAxis('x')
    rho = s.Field(0,'Rho_electron',timesteps=ts).getData()
    
    rho_mat = s.ParticleBinning(0,timesteps=ts).getData()
    px = s.ParticleBinning(0).getAxis('px')
    x = s.ParticleBinning(0).getAxis('x')
    t = s.ParticleBinning(0).getTimes()


    '''
    Pbin = {'px' : px.tolist(),
            'x'  : x.tolist(),
            't'  : t.tolist(), 
            'rho': np.array(rho_mat).tolist()
            }
    '''

    np.savetxt('Ex.csv',ex)
    np.savetxt('Rho.csv',rho)
    np.savetxt('x.csv', ex_x)

    
