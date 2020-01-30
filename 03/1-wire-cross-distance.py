#        _       _                 _            __     ___          _      
#       /_\   __| |_   _____ _ __ | |_    ___  / _|   / __\___   __| | ___ 
#      //_\\ / _` \ \ / / _ \ '_ \| __|  / _ \| |_   / /  / _ \ / _` |/ _ \
#     /  _  \ (_| |\ V /  __/ | | | |_  | (_) |  _| / /__| (_) | (_| |  __/
#     \_/ \_/\__,_| \_/ \___|_| |_|\__|  \___/|_|   \____/\___/ \__,_|\___|
#                                                                          
#                        ___                 _____                         
#                       /   \__ _ _   _     |___ /                         
#                      / /\ / _` | | | |      |_ \                         
#                     / /_// (_| | |_| |     ___) |                        
#                    /___,' \__,_|\__, |    |____/                         
#                                 |___/                                         

############################
#         Imports          #
############################

import sys

############################
#         Functions        #
############################

def move_left(current_point, distance):
  points = []
  for i in range(current_point[0]-1, current_point[0]-distance-1, -1):
    points.append((i, current_point[1]))
  return points

def move_right(current_point, distance):
  points = []
  for i in range(current_point[0]+1, current_point[0]+distance+1):
    points.append((i, current_point[1]))
  return points

def move_down(current_point, distance):
  points = []
  for i in range(current_point[1]-1, current_point[1]-distance-1, -1):
    points.append((current_point[0], i))
  return points

def move_up(current_point, distance):
  points = []
  for i in range(current_point[1]+1, current_point[1]+distance+1):
    points.append((current_point[0], i))
  return points

def get_points(path):
  current_point = [0, 0]
  points = []
  for movement in path:
    direction = movement[:1]
    distance = int(movement[1:])

    if direction == 'L':
      for point in move_left(current_point, distance):
        points.append(point)
      current_point[0] -= distance
    
    elif direction == 'R':
      for point in move_right(current_point, distance):
        points.append(point)
      current_point[0] += distance
    
    elif direction == 'D':
      for point in move_down(current_point, distance):
        points.append(point)
      current_point[1] -= distance
    
    elif direction == 'U':
      for point in move_up(current_point, distance):
        points.append(point)
      current_point[1] += distance
    else:
      print("ERROR: Unknown direction " + direction)
  return set(points)
    
def manhattan_distance(point):
  return abs(point[0]) + abs(point[1])

############################
#  Beginning of execution  #
############################

f = open("input.txt", 'r')
first_wire_path = f.readline().replace("\n", "").split(",")
second_wire_path = f.readline().replace("\n", "").split(",")

#first_wire_path = ['R4','D4','R4','U4','L4']
#second_wire_path = ['D4','R4','L4','U4','R4']

#Set of points where the wires pass
first_wire_points = get_points(first_wire_path)
second_wire_points = get_points(second_wire_path)

print(first_wire_points)
print(second_wire_points)

intersections = first_wire_points.intersection(second_wire_points)
intersections_distances = sorted(set([(manhattan_distance(x), x) for x in intersections]))

print(intersections)
print(intersections_distances)

print("\nNearest intersection: " + str(intersections_distances[0]))