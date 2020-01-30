#        _       _                 _            __     ___          _      
#       /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#      //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#     /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#     \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                          
#                         ___                 ____                         
#                        /   \__ _ _   _     | ___|                        
#                       / /\ / _` | | | |    |___ \                        
#                      / /_// (_| | |_| |     ___) |                       
#                     /___,' \__,_|\__, |    |____/                        
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
    #ADD instruction
    if intprogram[pc] == 1:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] + intprogram[intprogram[pc+2]]
      pc += 4
    #ADD instruction with parameters
    elif str(intprogram[pc])[-2:] == '01':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'

      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION ADD ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION ADD ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True

      intprogram[intprogram[pc+3]] = firstParam + secondParam
      pc += 4
    
    #MULT instruction
    elif intprogram[pc] == 2:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] * intprogram[intprogram[pc+2]]
      pc += 4
    #MULT instruction with parameters
    elif str(intprogram[pc])[-2:] == '02':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'

      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION MULT ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION MULT ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True

      intprogram[intprogram[pc+3]] = firstParam * secondParam
      pc += 4
    
    #READ instruction
    elif intprogram[pc] == 3:
      print(intprogram[intprogram[pc+1]])
      intprogram[intprogram[pc+1]] = int(input())
      pc += 2

    #PRINT instruction
    elif intprogram[pc] == 4:
      print(intprogram[intprogram[pc+1]])
      pc += 2
    #PRINT INSTRUCTION with parameter
    elif str(intprogram[pc])[-2:] == '04':
      paramMode = str(intprogram[pc])[-3]
      if paramMode == '0':
        print(intprogram[intprogram[pc+1]])
      elif paramMode == '1':
        print(intprogram[pc+1])
      else:
        print("PRINT INSTRUCTION ERROR: Invalid mode '" + str(paramMode) + "' for single parameter.")
      pc += 2
    
    #JUMP-IF-TRUE INSTRUCTION
    elif intprogram[pc] == 5:
      if intprogram[intprogram[pc+1]] != 0:
        pc = intprogram[intprogram[pc+2]]
      else:
        pc += 3
    #JUMP-IF-TRUE INSTRUCTION with parameters
    elif str(intprogram[pc])[-2:] == '05':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'
      
      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION JUMP-IF-TRUE ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION MULT ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True
      
      if firstParam != 0:
        pc = secondParam
      else:
        pc += 3

    #JUMP-IF-FALSE INSTRUCTION
    elif intprogram[pc] == 6:
      if intprogram[intprogram[pc+1]] == 0:
        pc = intprogram[intprogram[pc+2]]
      else:
        pc += 3
    #JUMP-IF-FALSE INSTRUCTION with parameter
    elif str(intprogram[pc])[-2:] == '06':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'
      
      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION JUMP-IF-TRUE ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION JUMP-IF-TRUE ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True
      
      if firstParam == 0:
        pc = secondParam
      else:
        pc += 3
    #LESS-THAN INSTRUCTION
    elif intprogram[pc] == 7:
      intprogram[intprogram[pc+3]] = 1 if intprogram[intprogram[pc+1]] < intprogram[intprogram[pc+2]] else 0 
      pc += 4
    #LESS-THAN INSTRUCTION with parameters
    elif str(intprogram[pc])[-2:] == '07':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'
      
      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION LESS-THAN ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION LESS-THAN ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True
      
      intprogram[intprogram[pc+3]] = 1 if firstParam < secondParam else 0
      pc += 4

    #EQUALS INSTRUCTION
    elif intprogram[pc] == 8:
      intprogram[intprogram[pc+3]] = 1 if intprogram[intprogram[pc+1]] == intprogram[intprogram[pc+2]] else 0 
      pc += 4
    #EQUALS INSTRUCTION with parameters
    elif str(intprogram[pc])[-2:] == '08':
      firstParamMode = str(intprogram[pc])[-3]
      try:
        secondParamMode = str(intprogram[pc])[-4]
      except:
        secondParamMode = '0'
      
      if firstParamMode == '0':
        firstParam = intprogram[intprogram[pc+1]]
      elif firstParamMode == '1':
        firstParam = intprogram[pc+1]
      else:
        print("INSTRUCTION EQUALS ERROR: Invalid mode '" + str(firstParamMode) + "' for first parameter.")
        end_of_program = True

      if secondParamMode == '0':
        secondParam = intprogram[intprogram[pc+2]]
      elif secondParamMode == '1':
        secondParam = intprogram[pc+2]
      else:
        print("INSTRUCTION EQUALS ERROR: Invalid mode '" + str(secondParamMode) + "' for second parameter.")
        end_of_program = True
      
      intprogram[intprogram[pc+3]] = 1 if firstParam == secondParam else 0
      pc += 4

    #END INSTRUCTION
    elif intprogram[pc] == 99:
      end_of_program = True
    else:
      print("ERROR: Undefined '" + str(intprogram[pc]) +"' opcode on position " + str(pc) + ". Something went wrong!")
      end_of_program = True
  return intprogram

############################
#  Beginning of execution  #
############################

f = open("input.txt", 'r')
intprogram = [int(x) for x in f.readline().split(",")]

result = compile_intprogram(intprogram)