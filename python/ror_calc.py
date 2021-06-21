import random
import math

def calculate(name='', aps = 10, proc_co = 1, dmg_modifier = 90):
    dps = aps * (dmg_modifier * (dmg_modifier/100))
    proc_rate = proc_co*aps
    print('Name: {}:\tBase Damage/second: {:.1f}%\tProc Rate/second: {:.1f}'.format(name, dps, proc_rate))


calculate()
calculate("Nailgun", 12, 0.6, 70)
calculate("Buzzsaw", 10, 1, 100)
calculate("Huntress Flurry (No Crit)", 3/1.3, 0.7, 100)
calculate("Huntress Flurry (Max Crit)", 6/1.3, 0.7, 100)
calculate("Commando", 6, 1, 100)
