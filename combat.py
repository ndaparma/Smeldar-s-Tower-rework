def standard_battle():
    global encounter
    global foe
    global battle
    global damage
    global command
    global boss
    global focus
    global turn_count
    
    command = None
    turn_count = 1
    damage = 0
    focus = 1
    skill_command = ["HARDEN", "STRIKE", "BOLT", "FOCUS", "STEAL", "THROW"]
  
    print("\n**********COMBAT START**********")
    print(f"\nYou encounter a {foe.name}!\n")

    stat_check()

    print(foe.name)
    print(f'{foe.HP} HP')
    print(f'{foe.ATK} ATK')
    print(f'{(10 - foe.DEF) * 10}% DEF \n')

    #start of combat script
    battle = 'ACTIVE'
    while battle == 'ACTIVE':
        print(f"********** Turn[{turn_count}] **********")
        poison_effect()
        poison_effect_foe()
        #player death
        player_death()
        print("Type battle command or type HELP for command list:")
        #in the krieg
        player_turn = 1
        while player_turn == 1:
          if p1.HP >= 1: 
              p1.TDEF = 0
  
              command = (input().upper())
              print("")
              #player attack
              if command == "ATK":
                  turn_count += 1
                  dam = random.randrange((p1.ATK // 4), p1.ATK)
                  damage = max(
                      round(dam * (foe.DEF * 0.1 * foe.TDEF * 0.1) * focus),
                      0)
                  foe.HP = min(max(foe.HP - damage, 0), foe.MaxHP)
                  foe.TDEF = 10
                  focus = 1
                  if foe.HP < 0:
                      foe.HP = 0
                  print(
                      f'{foe.name} has taken {damage} damage. {foe.name} has {foe.HP}/{foe.MaxHP} HP.'
                  )
                  #enemy reaction 
                  enemy_death_and_commands()
                  break
  
              #player Item
              elif command == "ITEM":
                  use_item()
                  break
  
              #player DEF
              elif command == "DEF":
                  turn_count += 1
                  p1.TDEF = p1.DEF // 2
                  print(f'{p1.name} is defending!')
                  foe.TDEF = 10
                  #enemy reactions 
                  enemy_death_and_commands()
                  break
  
  #Player escapes from combat
              elif command == "FLEE" and boss == 0:
                  if p1.SMB > 0:
                    turn_count += 1
                    p1.SMB -= 1
                    print(f'{p1.name} threw a SMOKE BOMB and escaped from combat! \n')
                    battle = 'INACTIVE'
                    encouter = 0
                    break
                  elif p1.SMB <= 0:
                    print(f'{p1.name} is out of SMOKE BOMBS and is unable to escape at this time \n')
  
              elif command == "FLEE" and boss == 1:
                  print(f'{p1.name} is unable to escape from the boss!')
  
  #Player skills
              elif command in skill_command and p1.MP > 0:
                  if command == "HARDEN" and p1.job == "WARRIOR":
                      warrior_skill()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  elif command == "STRIKE" and p1.job == "WARRIOR":
                      warrior_wildstrikes()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  elif command == "BOLT" and p1.job == "WIZARD":
                      wizard_spell()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  elif command == "FOCUS" and p1.job == "WIZARD":
                      wizard_focus()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  elif command == "STEAL" and p1.job == "THIEF":
                      thief_steal()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  elif command == "THROW" and p1.job == "THIEF":
                      thief_poisondagger()
                      enemy_death_and_commands()
                      turn_count += 1
                      break
                  else:
                      print('That command is invalid.\n')
  
              elif (
                  ((command == "STRIKE" or command == "HARDEN") or
                   (command == "BOLT" or command == "FOCUS")) or
                  (command == "STEAL" or command == "THROW")) and p1.MP == 0:
                  print(
                      f'{p1.name} is out of MP and unable to use their SKILL \n'
                  )
  #Player needs commands/help
              elif command == "STATS":
                  stat_check()
              elif command == "HELP":
                  combat_menu()
              else:
                  print('That command is invalid.\n')


def poison_effect():
    if p1.POISON > 0:
        p1_pdamage = p1.MaxHP // 25
        p1.HP = p1.HP - p1_pdamage
        p1.POISON = max(p1.POISON - 1, 0)
        print(
            f"{p1.name} is suffering from the effects of poison! {p1.name} takes {p1_pdamage} poison damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP"
        )
        player_death()


def poison_effect_foe():
    if foe.POISON > 0:
        foe_pdamage = (foe.MaxHP // 15) + 1
        foe.HP = max(foe.HP - foe_pdamage, 0)
        foe.POISON = max(foe.POISON - 1, 0)
  
        print(
            f"{foe.name} is suffering from the effects of poison! {foe.name} takes {foe_pdamage} poison damage. {foe.name} has {foe.HP}/{foe.MaxHP} HP"
        )
        #foe_pdamage = 0
        enemy_death()


def player_death():
    if p1.HP <= 0:
        battle = 'INACTIVE'
        combat = 'END'
        encouter = 0
        print(f'{p1.name} is DEAD')
        print('\n Do you wish to retry? YES or NO')
        dead = "DEAD"
        while dead == "DEAD":
            restart = (input().upper())
            if restart == 'YES':
                sys.stdout.flush()
                os.execv(sys.executable, ['python'] + sys.argv)
            elif restart == 'NO':
                quit()
            else:
                print('Please select YES or NO.')


def enemy_death():
    global foe
    global encounter
    global battle
    global command
    global damage
    global goblin_count
    global goblin_mobs
    global player_turn
    global enemy_turn
    if foe.HP <= 0:
        enemy_turn = 0
        player_turn = 0
        GPE = random.randrange(foe.MinGP, foe.MaxGP)
        p1.GP = p1.GP + GPE
        p1.xp = p1.xp + foe.exp
        if foe.name in goblin_mobs:
            goblin_count += 1
        if command == "BOLT" and p1.job == "WIZARD":
            print(f'{p1.name} vaporized the enemy!')
        elif damage >= foe.MaxHP // 2:
            print(f'{p1.name} obliterated the enemy!')
        elif command == "STRIKE" and p1.job == "WARRIOR":
            print(f'{p1.name} pulverised the enemy!')
        else:
            print(f'{p1.name} killed the enemy.')
        print(
            f'{p1.name} gained {GPE}GP and {foe.exp}EXP. {p1.name} has {p1.GP}GP'
        )
        level_up()
        print("********** VICTORY!!! **********")
        foe.HP = foe.MaxHP
        foe.POTS = foe.MaxPOTS
        foe.MP = foe.MaxMP
        foe.POISON = 0
        p1.POISON = 0
        battle = 'INACTIVE'
        encouter = 0


#script after an attack command by player to initate enemy half of turn
def enemy_death_and_commands():
    global foe
    global encounter
    global battle
    global command
    global damage
    global goblin_count
    global player_turn
    global enemy_turn
    enemy_turn = 1
    #Enemy Death
    enemy_death()

    while enemy_turn == 1:
        command2 = random.randrange(0, 7)
        #Enemy Commands [1]
        if command2 <= 2:  #ATTACK
            dam = random.randrange(foe.ATK // 3, foe.ATK)
            damage = max(round(dam - (p1.DEF * 0.1 - p1.TDEF * 0.1)), 0)
            p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
            player_turn = 0
            enemy_turn = 0
            print(f'The enemy {foe.name} ATTACKS')
            print(
                f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
            )

        elif command2 == 3 or command2 == 4:  #DEFEND
            foe.TDEF = foe.DEF // 2
            player_turn = 0
            enemy_turn = 0
            print(f'The enemy {foe.name} DEFENDS')
            print(f'{foe.name} has raised its defenses! \n')

        elif (command2 == 5 and foe.POTS > 0) and foe.HP < foe.MaxHP:  #HEAL
            print(f'The enemy {foe.name} HEALS')
            player_turn = 0
            enemy_turn = 0
            heal = random.randrange(5, 10)
            foe.HP = min(max(foe.HP + heal, 0), foe.MaxHP)
            foe.POTS -= 1
            print(
                f'{foe.name} has healed {heal} HP. {foe.name} has {foe.HP}/{foe.MaxHP} HP'
            )

        elif command2 == 6 and foe.MP > 0:  #SKILL
            enemy_skills()
            player_turn = 0
            enemy_turn = 0
        else:
            enemy_turn = 1


#Script for random encounters


def encounter_initiaiton():
    global foe
    global boss
    global current_room
    boss = 0
    encounter = random.randrange(1, 6)
    if encounter <= rooms[current_room]['spawn_rate']:
        foe = random.choice(rooms[current_room]['enemy_spawn_set'])
        standard_battle()


def ambush_initiaiton():
    global foe
    global boss
    global current_room
    boss = 0
    encounter = random.randrange(0, 6)
    if encounter >= spawn_rate:
        print(f'{p1.name} is ambushed by an enemy!')
        foe = random.choice(enemy_spawn_set)
        standard_battle()


#Scripts for boss encounters


#Bear
def boss_initiaiton():
    global foe
    global boss
    global current_room
    boss = 1
    foe = rooms[current_room]['foe']
    standard_battle()
