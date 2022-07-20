#Contains combat mechanics for player item /player and enemy skills 

def use_item():
    global turn_count
  
    items_list = "ON"
    while items_list == "ON":
        print(
            f"Select item to use or BACK to return to battle commands:\nPOTION: {p1.POTS}\nANTIDOTE: {p1.ANT}\nETHER: {p1.ETR}"
        )
        command = (input().upper())
        if command == "POTION" and p1.POTS > 0:
            turn_count += 1
            heal = random.randrange(5, 16) + p1.RJ
            p1.POTS -= 1
            p1.HP = min(max(p1.HP + heal, 0), p1.MaxHP)
            foe.TDEF = 10
            items_list = "OFF"
            print(
                f'{p1.name} drinks a POTION and heals {heal} HP. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
            )
            enemy_death_and_commands()
        elif command == "ANTIDOTE" and p1.ANT > 0:
            turn_count += 1
            p1.ANT -= 1
            p1.POISON = 0
            foe.TDEF = 10
            items_list = "OFF"
            print(f"{p1.name} drinks an ANTIDOTE and is relieved of POISON!\n")
            enemy_death_and_commands()
        elif command == "ETHER" and p1.ETR > 0:
            turn_count += 1
            heal = random.randrange(3, 6)
            p1.ETR -= 1
            p1.MP = min(max(p1.MP + heal, 0), p1.MaxMP)
            foe.TDEF = 10
            items_list = "OFF"
            print(
                f"{p1.name} drinks an ETHER and restores {heal} MP. {p1.name} has {p1.MP}/{p1.MaxMP} MP. \n"
            )
            enemy_death_and_commands()
        elif command == "POTION" and p1.POTS == 0:
            print('Unable to use a POTION at this time.')
        elif command == "ANTIDOTE" and p1.ANT == 0:
            print('Unable to use an ANTIDOTE at this time.')
        elif command == "ETHER" and p1.ETR == 0:
            print('Unable to use an ETHER at this time.')
        elif command == "BACK":
            items_list = "OFF"


def warrior_skill():
    heal = random.randrange(p1.MaxHP // 10, p1.MaxHP // 3)
    p1.HP = min(max(p1.HP + heal, 0), p1.MaxHP)
    p1.TDEF = p1.DEF * 2
    p1.MP -= 1
    foe.TDEF = 10
    print(
        f'{p1.name} has bolstered their constitution. {p1.name} healed {heal} HP and shielded themself this turn. {p1.name} has {p1.HP}/{p1.MaxHP} HP \n'
    )


def warrior_wildstrikes():
    print(f'{p1.name} strikes wildly at the enemy {foe.name}.')
    hit = random.randrange(0, 4)
    if hit >= 1:
        dam = random.randrange(p1.ATK // 1.5, p1.ATK)
        damage1 = max(round(dam * foe.DEF * .1 * foe.TDEF * .1), 0)
        print(f'{p1.name} strikes for {damage1} damage!')
    else:
        damage1 = 0
        print(f'{p1.name} strikes and misses!')
    hit = random.randrange(0, 4)
    if hit >= 1:
        dam = random.randrange(p1.ATK // 1.5, p1.ATK)
        damage2 = max(round(dam * foe.DEF * .1 * foe.TDEF * .1), 0)
        print(f'{p1.name} strikes for {damage2} damage!')
    else:
        damage2 = 0
        print(f'{p1.name} strikes and misses!')
        hit = random.randrange(0, 4)
    if hit >= 1:
        dam = random.randrange(p1.ATK // 1.5, p1.ATK)
        damage3 = max(round(dam * foe.DEF * .1 * foe.TDEF * .1), 0)
        print(f'{p1.name} strikes for {damage3} damage!')
    else:
        damage3 = 0
        print(f'{p1.name} strikes and misses!')
    tl_damage = damage1 + damage2 + damage3
    foe.HP = min(max(foe.HP - tl_damage, 0), foe.MaxHP)
    foe.TDEF = 10
    p1.MP -= 1
    print(
        f'{foe.name} has taken {tl_damage} total damage. {foe.name} has {foe.HP}/{foe.MaxHP} HP.'
    )


    #Wizard skill
def wizard_spell():
    global focus
    dam = random.randrange(p1.ATK, round(p1.ATK * 1.5))
    damage = max(round(dam * foe.DEF * 0.1 * foe.TDEF * 0.1 * focus), 0)
    foe.HP = min(max(foe.HP - damage, 0), foe.MaxHP)
    foe.TDEF = 10
    focus = 1
    p1.MP -= 1
    print(
        f'{p1.name} casts a magical bolt at the enemy {foe.name}.\n{foe.name} has taken {damage} damage. {foe.name} has {foe.HP}/{foe.MaxHP} HP.'
    )


def wizard_focus():
    global focus
    focus = 1.4
    foe.TDEF = 10
    print(f'{p1.name} concentrates their power.')
    concentrate = random.randrange(0, 5)
    if concentrate == 0:
        conc = random.randrange(1, p1.MaxMP)
        p1.MP = min(max(p1.MP + conc, 0), p1.MaxMP)
        print(
            f'{p1.name} restores some MP! {p1.name} has {p1.MP}/{p1.MaxMP} MP.'
        )
    else:
        p1.MP -= 1


#Thief skill
def thief_steal():
    mug = random.randrange(0, 5)
    if mug >= 2:
        GPE = random.randrange(foe.MinGP, round(foe.MaxGP * 0.8))
        p1.GP = p1.GP + GPE
        p1.MP -= 1
        print(
            f'{p1.name} manages to steal {GPE}GP from the enemy {foe.name}. {p1.name} now has {p1.GP}GP.\n'
        )

    elif mug == 1:
        p1.MP -= 1
        print(f'{p1.name} failed to steal anything!\n')

    elif mug == 0:
        p1.MP -= 1
        bribe = foe.MinGP // 3
        p1.GP = p1.GP - bribe
        print(f'{p1.name} failed to steal anything and dropped {bribe}! \n')


def thief_poisondagger():

    dagger = 0
    print(f'{p1.name} throws a handful of poison daggers!')
    hit = random.randrange(0, 3)
    if hit >= 1:
        foe.POISON += 2
        dagger += 1
        damage1 = random.randrange(1, 5)
    else:
        damage1 = 0
    hit = random.randrange(0, 3)
    if hit >= 1:
        foe.POISON += 2
        dagger += 1
        damage2 = random.randrange(1, 5)
    else:
        damage2 = 0
    hit = random.randrange(0, 3)
    if hit >= 1:
        foe.POISON += 2
        dagger += 1
        damage3 = random.randrange(1, 5)
    else:
        damage3 = 0
    tl_damage = damage1 + damage2 + damage3
    foe.HP = min(max(foe.HP - tl_damage, 0), foe.MaxHP)
    foe.TDEF = 10
    p1.MP -= 1
    print(
        f'{p1.name} hit the enemy {foe.name} with {dagger} poison dagger(s)! The enemy {foe.name} has taken {tl_damage} total damage and is poisoned for {foe.POISON} turns. {foe.name} has {foe.HP}/{foe.MaxHP} HP'
    )


# Enemy Skills
def enemy_skills():
    global battle
    global combat
    global encounter

    if foe.skill == 1:  #FLee
        foe.MP -= 1
        escape = random.randrange(0, 4)
        if escape >= 2:
            battle = 'INACTIVE'
            combat = 'END'
            encouter = 0
            print(
                f'The enemy {foe.name} scuttles away! You earn nothing. Sucks to suck.\n'
            )
            print("**********Enemy Escape!**********")
            foe.HP = foe.MaxHP
            foe.POTS = foe.MaxPOTS
        else:
            print(
                f'Enemy {foe.name} attempted to escape but stumbled and failed!\n'
            )

    elif foe.skill == 2:  #Cleave
        dam = random.randrange(round(foe.ATK // 1.5), foe.ATK)
        damage = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(f'The enemy {foe.name} strikes with a cleaving blow!')
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
        )

    elif foe.skill == 3:  #MAul
        dam = random.randrange(foe.ATK // 2, foe.ATK)
        damage = damage = max(round(dam + 3 * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(f'The enemy {foe.name} charges wildly and mauls {p1.name}!')
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
        )

    elif foe.skill == 4:  #Magic Bolt
        dam = random.randrange(foe.ATK, round(foe.ATK * 1.3))
        damage = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(
            f'The enemy {foe.name} concentrates their power into a magic bolt and hurls it at {p1.name}!'
        )
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
        )

    elif foe.skill == 5:  #Steal
        mug = random.randrange(0, 3)
        if mug >= 2:
            GPL = random.randrange(foe.MinGP, round(foe.MaxGP // 1.5))
            p1.GP = p1.GP + GPL
            foe.MP -= 1
            print(
                f'The enemy {foe.name} manages to steal {GPL}GP from {p1.name}. {p1.name} now has {p1.GP}GP.\n'
            )
        elif mug < 2:
            foe.MP -= 1
            print(
                f'{foe.name} attempted to steal but failed to grab anything!\n'
            )

    elif foe.skill == 6:  #Fire Breath
        dam = random.randrange(foe.ATK, round(foe.ATK * 1.2))
        damage = max(round(dam + 6 * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(
            f"Fire bellows from the enemy {foe.name}'s mouth scorching '{p1.name}!"
        )
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP} HP remaining. \n'
        )

    elif foe.skill == 7:  #Sting
        dam = random.randrange(foe.ATK // 2 + 4, foe.ATK + 4)
        damage = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
        pdamage = random.randrange(1, 3)
        p1.POISON += pdamage
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        damage2 = 4
        foe.HP = min(max(foe.HP - damage2, 0), foe.MaxHP)

        if foe.HP < 0:
            foe.HP = 0

        print(f'The enemy {foe.name} rushes at {p1.name} with their stinger!')
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
        )
        print(
            f'{foe.name} has taken {damage2} damage. {foe.name} has {foe.HP}/{foe.MaxHP} HP. \n'
        )
        if foe.HP <= 0:
            battle = 'INACTIVE'
            combat = 'END'
            encouter = 0
            GPE = random.randrange(foe.MinGP, foe.MaxGP)
            p1.GP = p1.GP + GPE
            p1.xp = p1.xp + foe.exp
            print(f'{foe.name} killed themself.')
            print(
                f'{p1.name} gained {GPE}GP and {foe.exp}EXP. {p1.name} has {p1.GP}GP'
            )
    elif foe.skill == 8:  #Poison Mist
        pdamage = random.randrange(1, 4)
        p1.POISON += pdamage
        print(
            f'{foe.name} spews a poison mist at {p1.name}! {p1.name} is poisoned for {pdamage} turns.'
        )

    elif foe.skill == 9:  #Quake
        damage = max(
            random.randrange(round(foe.ATK // 2), round(foe.ATK * 0.8)), 0)
        p1.HP = min(max(p1.HP - damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(
            f'The enemy {foe.name} strikes with the ground causing a mighty quake!'
        )
        print(
            f'{p1.name} has taken {damage} damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP. \n'
        )

    elif foe.skill == 10:  #Summon Swarm
        print(
            f'{foe.name} summons a swarm of smaller BEES to attack {foe.name}.'
        )

        hit = random.randrange(0, 4)
        if hit >= 1:
            dam = random.randrange(foe.ATK // 2, foe.ATK // 1.5)
            damage1 = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
            p1.POISON += 1
            print(f'{p1.name} is stung for {damage1} damage and is poisoned!')
        else:
            damage1 = 0
            print(f'{p1.name} swats a BEE away!')

        hit = random.randrange(0, 4)
        if hit >= 1:
            dam = random.randrange(foe.ATK // 2, foe.ATK // 1.5)
            damage2 = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
            p1.POISON += 1
            print(f'{p1.name} is stung for {damage2} damage and is poisoned!')
        else:
            damage2 = 0
            print(f'{p1.name} swats a BEE away!')

            hit = random.randrange(0, 4)
        if hit >= 1:
            dam = random.randrange(foe.ATK // 2, foe.ATK // 1.5)
            damage3 = max(round(dam * p1.DEF * 0.1 * p1.TDEF * 0.1), 0)
            p1.POISON += 1
            print(f'{p1.name} is stung for {damage3} damage and is poisoned!')
        else:
            damage3 = 0
            print(f'{p1.name} swats a BEE away!')

        tl_damage = damage1 + damage2 + damage3
        p1.HP = min(max(p1.HP - tl_damage, 0), p1.MaxHP)
        foe.MP -= 1
        print(
            f'{p1.name} has taken {tl_damage} total damage. {p1.name} has {p1.HP}/{p1.MaxHP} HP.'
        )
