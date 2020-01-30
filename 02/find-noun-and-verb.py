#        _       _                 _            __     ___          _      
#       /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#      //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#     /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#     \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                          
#                         ___                 ____                         
#                        /   \__ _ _   _     |___ \                        
#                       / /\ / _` | | | |      __) |                       
#                      / /_// (_| | |_| |     / __/                        
#                     /___,' \__,_|\__, |    |_____|                       
#                                  |___/                                   

############################
#         Imports          #
############################

import copy

############################
#         Functions        #
############################

def compile_intprogram(intprogram):
  pc = 0
  end_of_program = False
  while(not end_of_program):
    if intprogram[pc] == 1:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] + intprogram[intprogram[pc+2]]
    elif intprogram[pc] == 2:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] * intprogram[intprogram[pc+2]]
    elif intprogram[pc] == 99:
      end_of_program = True
    else:
      print("ERROR: Undefined '" + str(intprogram[pc]) +"' opcode on position " + str(pc) + ". Something went wrong!")
    pc += 4
  return intprogram

############################
#  Beginning of execution  #
############################

f = open("input.txt", 'r')
intprogram = [int(x) for x in f.readline().split(",")]

for i in range(99):
  for j in range(99):
    aux = copy.copy(intprogram)
    aux[1] = i
    aux[2] = j
    try:
      output = compile_intprogram(aux)
    except:
      None
    if output[0] == 19690720:
      print("aeHOOO")
      print("Noun: ", output[1])
      print("Verb: ", output[2])
      print("100 * noun + verb: ", str(100 * output[1] + output[2]))