#Contains room specific mechanics
def city_shop(): #City Shop mechanics
    global browsing
    global inventory
    potion = 25
    smoke_bomb = 35
    antd = 30
    ether = 40
    lantern_price = 200
    
    while True:
        print(
            "Purchase a POTION for [25GP], an ANTIDOTE for [30GP], an ETHER for [40GP], a SMOKE BOMB for [35GP], or a LANTERN for [200GP]. Type your selection or BACK to leave shopping window."
        )

        selc = (input().upper()).strip()
        print("")

        if (selc == 'POTION' and p1.GP >= potion) and p1.POTS < p1.MaxPOTS:
            p1.GP -= 25
            p1.POTS = min(p1.POTS + 1, p1.MaxPOTS)
            print(
                f'{p1.name} purchases a POTION and puts it in their bag. {p1.name} now has {p1.POTS} POTIONS and {p1.GP}GP.\n'
            )
          

        elif (selc == 'SMOKE BOMB'
              and p1.GP >= smoke_bomb) and p1.SMB < p1.MaxSMB:
            p1.GP -= 35
            p1.SMB = min(p1.SMB + 1, p1.MaxSMB)
            print(
                f'{p1.name} purchases a SMOKE BOMB and puts it in their bag. {p1.name} now has {p1.SMB} SMOKE BOMBS and {p1.GP}GP.\n'
            )

        elif (selc == 'ANTIDOTE' and p1.GP >= antd) and p1.ANT < p1.MaxANT:
            p1.GP -= 30
            p1.ANT = min(p1.ANT + 1, p1.MaxANT)
            print(
                f'{p1.name} purchases an ANTIDOTE and puts it in their bag. {p1.name} now has {p1.ANT} ANTIDOTES and {p1.GP}GP.\n'
            )

        elif (selc == 'ETHER' and p1.GP >= ether) and p1.ETR < p1.MaxETR:
            p1.GP -= 40
            p1.ETR = min(p1.ETR + 1, p1.MaxETR)
            print(
                f'{p1.name} purchases an ETHER and puts it in their bag. {p1.name} now has {p1.ETR} ETHERS and {p1.GP}GP.\n'
            )     

        elif (selc == 'LANTERN'
              and 'Lantern' not in inventory) and p1.GP >= lantern_price:
            p1.GP -= 200
            inventory.append('LANTERN')
            print(
                f'{p1.name} purchases a LANTERN and straps it to their belt. {p1.name} can stop being afraid of the dark! {p1.GP}GP remaining.\n'
            )

        elif selc == 'LANTERN' and 'Lantern'in inventory:
            print('"Sorry; only one of this item allowed per customer"\n')

        elif (selc == 'POTION' and p1.GP < potion) or (
                selc == 'SMOKE BOMB' and p1.GP < smoke_bomb) or (
                    selc == 'ANTIDOTE'
                    and p1.GP < antd) or (selc == 'ETHER' and p1.GP < ether) or ((selc == 'LANTERN'
              and 'Lantern'in inventory) and p1.GP >= lantern_price):
            print(
                f'{p1.name} does not have enough GP to purchase this item.\n')

        elif ((selc == "POTION" and p1.POTS == p1.MaxPOTS) or
              (selc == "SMOKE BOMB" and p1.SMB == p1.MaxSMB)) or (
                  (selc == "ANTIDOTE" and p1.ANT == p1.MaxANT) or
                  (selc == "ETHER" and p1.ETR == p1.MaxETR)):
            print(
                f'\n"Hey, looks like your inventory is full."\n\n{p1.name} is unable to purchase more of this item.\n'
            )

        elif selc == "BACK":
          break
        else:
           print('That command is invalid.\n')


def city_inn():  #Inn Mechanics
    inn_room = 40
    
    while True:

        if p1.GP >= inn_room:
            p1.GP -= 40
            heal = random.randrange(50, 100)
            p1.HP = min(max(p1.HP + heal, 0), p1.MaxHP)
            print(
                f'\n{p1.name} took a well earned rest and restored HP. {p1.name} has {p1.HP}/{p1.MaxHP}HP, and {p1.GP}GP.\n'
            )
            break

        elif p1.GP < inn_room:
            print(
                f'{p1.name} does not have enough GP in their wallet. {p1.name} has {p1.GP}GP.\n'
            )
            break
def village_smith():
  while True:
    if p1.GrLvl < 5:
        print(f"Improve WEAPON or ARMOR for {rooms['Smith']['upgrade_cost']}GP or go BACK?")
        selc = (input().upper()).strip()
        print("")
        if selc == "WEAPON" and p1.GP >= rooms['Smith']['upgrade_cost']:
          p1.GrLvl += 1
          p1.ATK += 1
          p1.GP -= rooms['Smith']['upgrade_cost']
          rooms['Smith']['upgrade_cost'] = rooms['Smith']['upgrade_cost'] * 2
          print(f"The SMITH takes back {p1.name}'s WEAPON and begins making improvements. After a while he returns with your UPGRADED gear.")
          stat_check()
        elif selc == "ARMOR" and p1.GP >= rooms['Smith']['upgrade_cost']:
          p1.GrLvl += 1
          p1.DEF = max(p1.DEF - .5, 3)
          p1.GP -= rooms['Smith']['upgrade_cost']
          rooms['Smith']['upgrade_cost'] = rooms['Smith']['upgrade_cost'] * 2
          print(f"The SMITH takes back {p1.name}'s ARMOR and begins making improvements. After a while he returns with your UPGRADED gear.")
          stat_check()
        elif (selc == "WEAPON" or selc == "ARMOR") and p1.GP < rooms['Smith']['upgrade_cost']:
          print( f"{p1.name} does not have enough GP for an UPGRADE. {p1.name} only has {p1.GP} GP.\n")
        elif selc == "BACK":
          break
        else:
          print('Invalid command. Please select WEAPON or ARMOR, or BACK to leave.') 
    else:
        print(line1903)
        break
def potion_healing():
  heal = 15 + p1.RJ
  p1.POTS -= 1
  p1.HP = min(max(p1.HP + heal, 0), p1.MaxHP)
  print(
      f'{p1.name} drinks a POTION and heals {heal} HP. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
  )
def camp_healing(): #Camp resting mechanics
  while True:
    if rooms['Camp']['fire'] > 0:
      heal = random.randrange(10, 20)
      p1.HP = min(max(p1.HP + heal, 0), p1.MaxHP)
      rooms['Camp']['fire'] -= 1
      print(f'\n{p1.name} has rested and restored {heal}HP. {p1.name} now has {p1.HP}/{p1.MaxHP}HP.\n')
      if rooms['Camp']['fire'] > 0:
        print(f"{p1.name} may rest {rooms['Camp']['fire']} times before the camp fire dies.")
        break
      else:
        rooms['Camp']['intro'] = line102
        print(
                f'The fire has finally died and {p1.name} is unable to rest here.'
            )
        break
    else:
      print(
              f'The fire has finally died and {p1.name} is unable to rest here.'
          )
      break

def shrine_pray():
  if p1.GP >= 35:
    p1.MP = p1.MaxMP
    p1.GP -= 35
    print(f"{p1.name} drops 35 GP into an ornate donation box and kneels between the lanterns at the alter. {p1.name} is filled with a surge of power. {p1.name}'s MP is fully restored.")
  else:
    print(f"{p1.name} is too poor to spend on charity.")

def cliff_examine():
  global inventory
  global current_room
  while True:
    if rooms['Cliff']['chest'] == "CLOSED" and 'AXE' not in inventory:
      print(line604)
    elif rooms['Cliff']['chest'] == "CLOSED" and 'AXE' in inventory:
      print(line605)
      selc = (input().upper()).strip()
      print("")
      
      if selc == "CUT":
          print(line605b)
          rooms['Cave2']['chest'] = "OPEN"
          inventory.append('PENDANT')
          rooms['Cliff']['EXPLORE'] = line603
          break

      elif selc == "BACK" or selc == "BACK OUT":
          print(line605c)
          break
      else:
          print('That command is invalid.\n')
    else:
      print(line605d)
      break

def hill_examine():
  global inventory
  while True:
    if rooms['Hill']['SOUTH'] == 'LOCKED':
      if 'AXE' not in inventory:
        print(line805)
        break
      elif 'AXE' in inventory:
        print(line1405)
        selc = (input().upper()).strip()
        print("")
        if selc == 'CUT':
          print(line806)
          rooms['Hill']['SOUTH'] = 'Berry'
          rooms['Hill']['EXPLORE'] = line804
          break
        elif selc == 'LEAVE':
          print(line806b)
          break
        else:
          print('That command is invalid.\n')
    else:
      print(line1408)
      break
def waterfall_examine():
  global current_room
  global inventory
  while True:
    if rooms['Waterfall']['chest'] == 'CLOSED':
      print(line1302b)
      selc = (input().upper()).strip()
      print("")
      if selc == "TAKE":
          print(line1303)
          inventory.append('SALMON')
          rooms['Waterfall']['chest'] = 'OPEN'
          break
      elif selc == "SAVE":
          print(line1304)
          rooms['Waterfall']['chest'] = 'OPEN'
          rooms['Waterfall']['event'] = 1
          break
      elif selc == "LEAVE":
          print(line1305)
          break
      else:
          print('That command is invalid.\n')
    elif rooms['Waterfall']['chest'] == 'OPEN':
      if rooms['Waterfall']['event'] == 1:
        print(line1307)
        p1.GP += 100
        rooms['Waterfall']['event'] = 2
        print(f'\n{p1.name} has {p1.GP}GP.\n')
        break
      else:
        print(line1308)
        break 
          
def lake_examine():
  global inventory
  while True:
    if rooms['Lake']['EAST'] == 'LOCKED':
      if 'AXE' not in inventory:
        print(line1404)
        break
      elif 'AXE' in inventory:
        print(line1405)
        selc = (input().upper()).strip()
        print("")
        if selc == 'CUT':
          print(line1406)
          boss_initiaiton()
          print(line1408)
          rooms['Lake']['EAST'] = 'Mushroom'
          rooms['Lake']['EXPLORE'] = line1403
          break
        elif selc == 'LEAVE':
          print(line1407)
          break
        else:
          print('That command is invalid.\n')
    else:
      print(line1408)
      break
  
def cave_examine():
  global inventory
  global current_room
  while True:
    if 'Bear' in rooms[current_room]['boss']:
      if 'SALMON' not in inventory:
        print(f'\n{line903}')
      else:
        print(f'\n{line904}')
      selc = (input().upper()).strip()
      print("")
      if selc == "POKE":
          print(line911)
          boss_initiaiton()
          rooms['Cave']['boss'].remove('Bear')
          inventory.append('AXE')
          rooms['Cave']['intro'] = line902
          rooms['Cave']['EXPLORE'] = line906b
          print(line912)
          break

      elif selc == "FEED" and 'SALMON' in inventory:
          inventory.remove('SALMON')
          rooms['Cave']['boss'].remove('Bear')
          inventory.append('AXE')
          rooms['Cave']['intro'] = line902
          rooms['Cave']['EXPLORE'] = line906b
          print(line913)
          break
      elif selc == "BACK" or selc == "BACK OUT":
          print(line907)
          break
      else:
          print('That command is invalid.\n')
    else:
      print(line912b)
      break
    

def cave2_examine():
  global inventory
  global current_room
  while True:
    if rooms['Cave2']['chest'] == "CLOSED":
      print(line925)
      selc = (input().upper()).strip()
      print("")
      if selc == "OPEN":
          print(line926)
          boss_initiaiton()
          rooms['Cave2']['chest'] = "OPEN"
          inventory.append('IRON KEY')
          rooms['Cave2']['EXPLORE'] = line924
          print(line927)
          break

      elif selc == "BACK" or selc == "BACK OUT":
          print(line928)
          break
      else:
          print('That command is invalid.\n')
    else:
      print(line928b)
      break
    

def cave4_examine():
  global inventory
  global current_room
  while True:
     if rooms['Cave4']['EAST'] == 'LOCKED':
      if 'IRON KEY' not in inventory:
        print(f'\n{line940}')
        break
      else:
        print(f'\n{line940b}')
        selc = (input().upper()).strip()
        print("")
        if selc == "OPEN":
            print(line941)
            rooms['Cave4']['EAST'] = 'Cave5'
            rooms['Cave4']['EXPLORE'] = line939
            break
        elif selc == "BACK" or selc == "BACK OUT":
            print(line941b)
            break
        else:
            print('That command is invalid.\n')
  


def berry_examine():
  while True:
    if rooms['Berry']['chest'] == 'CLOSED':
      print(line1002b)
      selc = (input().upper()).strip()
      print("")
      if selc == "PICK":
        print(line1003)
        boss_initiaiton()
        print(line1004)
        berriesPicked = random.randrange(2, 6)
        p1.POTS = min(p1.POTS + berriesPicked, p1.MaxPOTS)
        rooms['Berry']['chest'] = "OPEN"
        rooms['Berry']['EXPLORE'] = line1005
        print(f'{p1.name} has made {berriesPicked} POTIONS. {p1.name} has {p1.POTS} POTS.')
        break
      elif selc == "LEAVE":
        print(line1002c)
        break
      else:
            print('That command is invalid.\n')
    else:
      print(line1006)
      break

def oak_examine():
  global current_room
  while True:
    print(line2003)
    selc = (input().upper()).strip()
    print("")
    if selc == "CLIMB":
      print(line2004)
      current_room = 'Hive'
      rooms[current_room]['boss_ambush']()
      print(f"\n**********[ {rooms[current_room]['name']} ]**********\n")
      print(rooms[current_room]['intro'])
      break
    elif selc == "BACK":
      print(line2005)
      break
    else:
      print('That command is invalid.\n')

def hive_examine():
  global current_room
  while True:
    if rooms['Hive']['chest'] == "CLOSED":
      print(line2105b)
      p1.POTS = min(p1.POTS + 3, p1.MaxPOTS)
      rooms['Hive']['EXPLORE'] = line2106
      rooms['Hive']['chest'] = "OPEN"
      break
    else:
      print(line2106b)
      break

def mushroom_examine():
  while True:
    if goblin_count >= 10 and rooms['Mushroom']['chest'] == 'CLOSED':
      print(line1604)
      inventory.append('HEROS MEDAL')
      rooms['Mushroom']['chest'] = 'OPEN'
      break
    elif goblin_count >= 10 and rooms['Mushroom']['chest'] == 'OPEN':
      print(line1604b)
      break
    else:
      print(line1603)
      break
def hill_lock():
  while True:
    if rooms['Hill']['SOUTH'] == 'LOCKED':
      print(line811)
      break
    else:
      continue
def lake_lock():
  while True:
    if rooms['Lake']['EAST'] == 'LOCKED':
      print(line1410)
      break
    else:
      continue
def cave_lock():
  while True:
    if 'Bear' in rooms['Cave']['boss']:
      print(line914)
      break
    elif (selc == 'EAST' and rooms['Cave']['EAST'] == 'LOCKED') and "LANTERN" not in inventory:
      print(line909)
      break
    elif (selc == 'EAST' and rooms['Cave']['EAST'] == 'LOCKED') and "LANTERN" in inventory:
      print(line915)
      rooms['Cave']['EAST'] = 'Cave1'
      break
    else:
      continue
      
      
def cave4_lock():
  while True:
    if rooms['Cave4']['EAST'] == 'LOCKED':
      print(line943)
      break
    else:
      continue

      
def cave4_boss_ambush(): 
  global current_room
  while True:
    if 'Hobgoblin Gang' in rooms['Cave4']['boss']:
      print(line935)
      boss_initiaiton()
      rooms['Cave4']['boss'].remove('Hobgoblin Gang')
      rooms['Cave4']['spawn_rate'] = 4
      print(line936)
    else:
      break
def cave5_boss_ambush():
  global current_room
  global inventory
  while True:
    if 'Goblin Queen' in rooms['Cave5']['boss']:
      print(line947)
      boss_initiaiton()
      rooms['Cave5']['boss'].remove('Goblin Queen')
      inventory.append('DRAGON BONE KEY')
      print(line949)
    else:
      break
def hive_boss_ambush():
  global current_room
  global inventory
  global enemy_spawn3
  global enemy_spawn9 
  while True:
    if 'Giant Bee Queen' in rooms['Hive']['boss']:
      print(line2101)
      encounter_initiaiton()
      print(line2101b)
      encounter_initiaiton()
      print(line2101b)
      encounter_initiaiton()
      print(line2102)
      boss_initiaiton()
      rooms['Hive']['boss'].remove('Giant Bee Queen')
      rooms['Hive']['spawn_rate'] = 0
      inventory.append('ROYAL JELLY')
      enemy_spawn3.remove(p14)
      enemy_spawn9.remove(p14)
      enemy_spawn3.append(p25)
      enemy_spawn9.append(p25)
      p1.RJ += 5
      print(line2103)
      current_room = 'Oak'
     # print(f"\n**********[ {rooms[current_room]['name']} ]**********\n")
    else:
      break
def castle_speak():
  global inventory
  while True:
    if rooms['Castle']['speach'] == 0:
      print(line505)
      print(line506)
      rooms['Castle']['speach'] += 1
      break
    elif 'HEROS MEDAL' in inventory and rooms['Castle']['event'] == 0:
      print(line505)
      print(line508)
      p1.MaxHP += 25
      p1.HP = p1.MaxHP
      stat_check()
      rooms['Castle']['event'] = 1
      key_items['HEROS MEDAL']['description'] = 'A gold medal found on a corpse covered in mushrooms. Engraved with the royal crest on the front; the back reads "For Jeremy the Goblin-Slayer". You can feel the medal filling you with vigor ever since the princess unlocked its magic.'
      break
    elif rooms['Castle']['speach'] == 1:
      print(line505)
      print(line507)
      break
def boat_speak():
  global current_room
  global inventory
  while True:
    if rooms['Boat']['speach'] == 0:
      print(line1504)
      rooms['Boat']['speach'] = 1
      break
    elif rooms['Boat']['speach'] == 1 and 'SALMON' in inventory:
      print(line1506) 
      selc = (input().upper()).strip()
      print("")
      if selc == "GIVE":
        print(line1508)
        print(f'{p1.name} was given a BUCKLER! This sturdy steel shield should help block damage. {p1.name} has gained 5% DEF!')
        p1.DEF = max(p1.DEF - 1.5, 3)
        rooms['Boat']['speach'] = 2
        rooms['Boat']['EXPLORE'] = line1503
        inventory.remove('SALMON')
        inventory.append('BUCKLER')
        stat_check()
        break
      elif selc == "KEEP":
        print(line1507)
        break
      else:
        print('That command is invalid.\n')
    elif rooms['Boat']['speach'] == 1 and 'SALMON' not in inventory:
      print(line1510)
      break
    else:
      print(line1509)
      break


def shrine_speak():
  global current_room
  global inventory
  while True:
    if rooms['Boat']['speach'] == 0:
      print(line1105)
      print(line1106)
      rooms['Boat']['speach'] = 1
      break
    elif rooms['Boat']['speach'] == 1 and 'PENDANT' in inventory:
      print(line1108) 
      print(line1109) 
      print(f"{p1.name} is given the FRIAR's MESSER. This single edge sword is finely crafted. Much better than the rusty old blade you found in the trash before you started adventuring... {p1.name} gained 5 ATK")
      inventory.remove('PENDANT')
      inventory.append('MESSER')
      p1.ATK += 5
      stat_check()
      break
    elif rooms['Boat']['speach'] == 1:
      print(line1107)
      break

      