#        _       _                 _            __     ___          _      
#       /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#      //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#     /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#     \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                          
#                         ___                  __                          
#                       /   \__ _ _   _      / /_                         
#                      / /\ / _` | | | |    | '_ \                        
#                     / /_// (_| | |_| |    | (_) |                       
#                    /___,' \__,_|\__, |     \___/                        
#                                |___/                                   

############################
#         Imports          #
############################

############################
#        Definitions       #
############################
class spaceObject:
  def __init__(self, name):
    self.name = name
    self.father = None
    self.satellites = []
    self.nOrbits = 0

  def set_father(self, father):
    self.father = father
    update_nOrbits(self)
  
  def append_satellite(self, satellite):
    self.satellites.append(satellite)
    satellite.set_father(self)

def find_object(root, name):
  if root.name == name:
    return root
  for obj in root.satellites:
    if find_object(obj, name) != None:
      return obj

def update_nOrbits(root):
  root.nOrbits = root.father.nOrbits + 1
  for obj in root.satellites:
    update_nOrbits(obj)

############################
#  Beginning of execution  #
############################

#Universal Center of Mass
com = spaceObject("COM")
#The orbitMap is just a list of all objects for the mere purpose of kno.
#The structure of the orbits is accessed iterating through COM's children.
orbitMap = []
orbitMap.append(com)

a = spaceObject("A")
b = spaceObject("B")
c = spaceObject("C")
d = spaceObject("D")
e = spaceObject("E")
f = spaceObject("F")

com.append_satellite(a)
a.append_satellite(b)
b.append_satellite(c)
c.append_satellite(d)
d.append_satellite(e)
e.append_satellite(f)

print(find_object(com, "COM").nOrbits)
print(find_object(com, "A").satellites[0].name)
print(find_object(com, "B").satellites[0].name)
print(find_object(com, "C").satellites[0].name)
print(find_object(com, "D").satellites[0].name)
print(find_object(com, "E").satellites[0].name)
print(find_object(com, "F").satellites[0].name)

print([x.name for x in com.satellites])

f = open("input.txt", "r")
for line in f:
  objs = line.split(")")
  if objs != []:
    a = objs[0]
    b = objs[1]


