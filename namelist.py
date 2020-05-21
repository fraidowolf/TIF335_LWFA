import numpy as np
import json

with open('config.json', 'r') as fp:
        config = json.load(fp)



Main(
    geometry = "1Dcartesian",
    
    interpolation_order = 2,

    timestep_over_CFL=0.90,
    simulation_time = config['st'],

    cell_length  = [ config['dx'] ],
    grid_length = [ config['L0x'] ],

    number_of_patches = [ config['N_patch_x'] ],

    #clrw = config['resx']/config['N_patch_x'],
    
    EM_boundary_conditions = [
        ["silver-muller"]
    ],
    
    solve_poisson = False,
    print_every = 100,

    random_seed = smilei_mpi_rank
)


MovingWindow(
    time_start = Main.grid_length[0]*0.99,
    velocity_x = 0.9997
)

LoadBalancing(
    initial_balance = False,
    every = 20,
    cell_load = 1.,
    frozen_particle_load = 0.1
)

Species(
    name = "electron",
    position_initialization = "regular",
    momentum_initialization = "cold", #"maxwell-juettner",
    particles_per_cell = 100,
    c_part_max = 1.0,
    mass = 1.0,
    charge = -1.0,
    #number_density = 0.01,
    charge_density = trapezoidal(config['ne'], xvacuum=config['Lvlx'], 
                                 xplateau=config['Lpx'], xslope1=config['Rpx']), 
    #mean_velocity = [0.0, 0.0, 0.0],
    #temperature = [0.000001],
    pusher = "boris",
    #time_frozen = 0.0,
    boundary_conditions = [["remove", "remove"]]
)

LaserPlanar1D(
    box_side         = "xmin",
    a0              = config['a0'],
    omega = 1,
    time_envelope   =  tgaussian(duration=config['lt'], center=config['lt']/2, fwhm=config['lt']/3)
    #tconstant(start = freq/4)
)

Checkpoints(
    dump_step = 0,
    dump_minutes = 0.0,
    exit_after_dump = False,
)

list_fields = ['Ex','Rho_electron']

DiagFields(
    every = 1000,
    fields = list_fields
)

DiagParticleBinning(
    deposited_quantity = "weight",
    every = 500,
    species = ["electron"],
    axes = [
        ["moving_x", 0,config['L0x'] , 1000],
        ["px", -2, 10*np.sqrt(300), 2000]
    ]
)

DiagParticleBinning(
    deposited_quantity = "weight",
    every = 500,
    time_average = 1,
    species = ["electron"],
    axes = [ ["ekin",    0.02,    30.,   1000] ]
)

DiagPerformances(
    every = 100,
)
