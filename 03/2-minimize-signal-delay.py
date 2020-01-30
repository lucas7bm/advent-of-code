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
  return points
    
def manhattan_distance(point):
  return abs(point[0]) + abs(point[1])

def signal_distance(point, wire_path):
  i = 0
  found = False
  while i < len(wire_path):
    if point == wire_path[i]:
      return i+1
    i+=1
  if not found:
    print(point)
    print(wire_path)
    return -1
############################
#  Beginning of execution  #
############################

f = open("input.txt", 'r')
first_wire_path = f.readline().replace("\n", "").split(",")
second_wire_path = f.readline().replace("\n", "").split(",")

#Set of points where the wires pass
first_wire_points = get_points(first_wire_path)
second_wire_points = get_points(second_wire_path)

intersections = set(first_wire_points).intersection(set(second_wire_points))

intersections_signal_dist = []
for point in intersections:
  dist = signal_distance(point, first_wire_points)
  dist += signal_distance(point, second_wire_points)
  intersections_signal_dist.append((dist, point))

print(sorted(set(intersections_signal_dist))[0])