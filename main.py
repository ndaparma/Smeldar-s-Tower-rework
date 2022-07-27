import os
import sys
import random
from script import *

exec(open('character.py').read())
exec(open('combat.py').read())
exec(open('skills.py').read())
exec(open('mechanics.py').read())
exec(open('world.py').read())


def move_rooms():
  global current_room 
  global player_choice
  while True:
    if selc in rooms[current_room] and rooms[current_room][selc] == 'LOCKED':
        rooms[current_room]['LOCK']()
        break
    elif selc in rooms[current_room] and rooms[current_room][selc] != 'LOCKED':
        current_room = rooms[current_room][selc]
        print(f'\nYou move to the {selc}.\n')
        encounter_initiaiton()
        player_choice = 1
        if 'boss_ambush' in rooms[current_room]:
          rooms[current_room]['boss_ambush']()
          break
        break
    else:
        print (f'\nYou can\'t go to the {selc.lower()}\n')
        break
      
def take_actions():
  global current_room
  global player_choice
  while True:

    if selc == "EXPLORE":
      print(rooms[current_room][selc])
      break
    elif selc == "EXAMINE" and selc in rooms[current_room]:
      rooms[current_room]['EXAMINE']()
      break
    elif selc == "SPEAK" and selc in rooms[current_room]:
      rooms[current_room]['SPEAK']()
      break  
    elif selc == "HEAL":
      if p1.POTS > 0:
        potion_healing()  
        break
      else:
          print(
              f'{p1.name} is out of POTIONS and unable to heal at this time')
    elif selc == 'BUY' and selc in rooms[current_room]:
      city_shop()
      break
    elif selc == 'REST' and selc in rooms[current_room]:
      if rooms[current_room]['name'] == 'Camp Site':
        camp_healing()
        break
      elif rooms[current_room]['name'] in inns:
        city_inn()
        break
    elif selc == 'PRAY' and selc in rooms[current_room]:
      shrine_pray()
      break
    elif selc == "UPGRADE" and selc in rooms[current_room]:
      village_smith()
      break
    elif selc == "TEST" and selc in rooms[current_room]:
      rooms[current_room]['TEST']()
      break
    else:
      print('Unable to do that here.')
      break
        
def helper_actions():
  global current_room
  global player_choice

  while True:
    if selc == "HELP":
      world_menu()
      break
    elif selc == "STATS":
      stat_check()
      break
    elif selc == "ITEMS":
      item_check()
      break 

directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'EXIT']
actions = ['EXPLORE', 'EXAMINE', 'SPEAK', 'HEAL', 'REST', 'PRAY', 'BUY', "UPGRADE"]
helper = ['HELP', 'STATS', 'ITEMS']

game_setup = 0
inns = ['Inn', 'Tavern & Inn']
current_room = 'Camp'

inventory = []
goblin_count = 0

while True:
  while game_setup == 0:
    player_setup()
  print(f"**********[ {rooms[current_room]['name']} ]**********\n")
  print(rooms[current_room]['intro'])
  player_choice = 0
  while player_choice == 0:
    print('\nEnter command:')
    selc = input().upper().strip()
    if selc in directions:
      move_rooms()
    
    elif selc in actions:
      take_actions()

    elif selc in helper:
      helper_actions()
      
    else:
      print('invalid')
  
  


  