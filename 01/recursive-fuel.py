#         _       _                 _            __     ___          _      
#        /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#       //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#      /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#      \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                         
#                          ___                 _                            
#                         /   \__ _ _   _     / |                           
#                        / /\ / _` | | | |    | |                           
#                       / /_// (_| | |_| |    | |                           
#                      /___,' \__,_|\__, |    |_|                           
#                                   |___/                                    

############################
#         Imports          #
############################

import multiprocessing as mp

############################
#         Functions        #
############################

def calculate_fuel_requirement(mass):
  if (int(mass / 3) - 2) <= 0:
    return 0
  return ((int(mass / 3) - 2) + calculate_fuel_requirement((mass / 3) - 2))

############################
#  Beginning of execution  #
############################

f = open("input.txt", 'r')
array_of_modules = []
for line in f:
  array_of_modules.append(int(line))

print(calculate_fuel_requirement(1969))

pool = mp.Pool(mp.cpu_count())
results = pool.map_async(calculate_fuel_requirement, array_of_modules)
print(sum(results.get()))