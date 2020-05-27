import json
import numpy as np
import argparse


if __name__=='__main__':

    # parse argument from command line
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('it_nbr', type=int,
                            help='an integer for the each iteration')
    args = parser.parse_args()
    it_nbr = args.it_nbr

    # set iteration parameter
    start = 0.01
    stop = 0.012
    iterations = 2
    step_len = (stop-start)/iterations
    ne = step_len*it_nbr + start

    # configuration parameters
    N_patch_x = 2**4 #2**6
    ppc = 100
    

    # resolution:
    l0 = 2.0*np.pi                          # wavelength in normalized units
    #ne = 0.0256                             # electron density in critical densities
    wpe = np.sqrt(ne)                       # plasma frequency in normalized units
    lp = 2.*np.pi/wpe                       # plasma wavelength in normalized units
    rest = 57.0                         # nb of timestep in 1 optical cycle
    resx = 50.0                         # nb cells in 1 wavelength
    t0 = l0                                 # optical cycle in normalized units
    dt = t0 / rest                          # temporal step
    dx = l0 / resx                          # spatial step in x
    dx_patch = dx * N_patch_x               # patch length in x
    st = 15*60*l0                              # simulation time
    lt = t0*18                              # duration gaussian pulse
    a0 = 1                               # amplitude of vectorpotential



    # geometry along x:
    Lpx = 10*60 * l0                           # plasma plateau length in x
    Rpx = 0.2 * lp                          # plasma linear ramp length in x
    Lvlx = lp / 2.                          # space before plasma plateau in x
    Lvrx = lp                               # space behind plasma plateau in x
    L0x = Lvlx + Lpx + Lvrx + 2.*Rpx        # box length along x
    L0x = lp*8
    L0x_div = np.ceil(L0x / dx_patch) * dx_patch    # corrected length, to give a cell number 
                                                    # divisible  by the number of patches
    L0x = L0x_div
     

    config = {
                'N_patch_x' : N_patch_x,
                'l0'  : l0,
                'ne'  : ne,
                'wpe' : wpe,
                'lp'  : lp,
                'rest': rest,
                'resx': resx,
                't0'  : t0,
                'st'  : st,
                'dt'  : dt,
                'dx'  : dx,
                'lt'  : lt,
                'dx_patch' : dx_patch,
                'Lpx' : Lpx,
                'Rpx' : Rpx,
                'Lvlx': Lvlx,
                'Lvrx': Lvrx,
                'L0x' : L0x_div,
                'a0'  : a0
    }

    with open('config.json', 'w') as fp:
            json.dump(config, fp)


    '''
    pi = np.pi
    c = 3*10**8
    lambda_SI = 800**(-9) # wavelength (m)

    f_SI = 2*pi*c/lambda_SI # angular freq (s^-1)
    Lx_SI = 60*lambda_SI # grid length (m)
    sim_time_SI = 10*Lx_SI/c # simulation time (s)

    Lx = Lx_SI*f_SI/c #/2pi # grid length (c/omega)
    sim_time = sim_time_SI*f_SI # simulation time (omega^-1)


    nx = 32*int(Lx_SI/lambda_SI)
    #nx = 896
    npatch_x = 32
    dx = Lx/nx #0.125

    freq = 1/(2*pi)
    duration = 18/freq
    #omega_ = 2*3.1415*freq
    laser_fwhm = duration/3 #40*freq #2*freq
    '''

