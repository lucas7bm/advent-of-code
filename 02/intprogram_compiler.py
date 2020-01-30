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

intprogram = compile_intprogram(intprogram)
print("Output: " + str(intprogram[0]))