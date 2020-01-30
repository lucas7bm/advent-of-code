#        _       _                 _            __     ___          _      
#       /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#      //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#     /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#     \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                          
#                         ___                 _  _                         
#                        /   \__ _ _   _     | || |                        
#                       / /\ / _` | | | |    | || |_                       
#                      / /_// (_| | |_| |    |__   _|                      
#                     /___,' \__,_|\__, |       |_|                        
#                                  |___/                                      

############################
#         Imports          #
############################

############################
#         Functions        #
############################

def double_digits_test(pwd):
  i=1
  while i < len(pwd)-2:
    if pwd[i] == pwd[i+1] and pwd[i] != pwd[i-1] and pwd[i+1] != pwd[i+2]:
      return True
    i += 1
  if pwd[-1] == pwd[-2] and pwd[-2] != pwd[-3]:
    return True
  if pwd[0] == pwd[1] and pwd[1] != pwd[2]:
    return True
  return False

def always_crescent_test(pwd):
  i=0
  while i < len(pwd) -1:
    if pwd[i] > pwd[i+1]:
      return False
    i += 1
  return True
    

def validate_pwd(pwd):
  if double_digits_test(pwd) and always_crescent_test(pwd):
    return True
  return False


############################
#  Beginning of execution  #
############################

count = 0
for pwd in range(136760, 595730):
  if validate_pwd(str(pwd)):
    count += 1
print(count)