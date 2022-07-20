#Contains room and item information


#define rooms/areas for game


rooms = {
    '' : {
        'name' : '',
        'intro' : '',
        'NORTH' : None,
        'EAST' : None,
        'SOUTH' : None,
        'WEST' : None,
        'EXPLORE': '',
        'EXAMINE' : None,
        'SPEAK' : None,
        'REST' : 'rest',
        'PRAY' : 'pray',
        'BUY' : "BUY",
        'speach' : None,
        'spawn_rate' : 0,
        'enemy_spawn_set' : None,
        'boss' : [],
        'boss_ambush' : None,
        'foe' : None,
        'LOCK' : None,
        'chest' : None,
        'event' : None,
    },

    'Camp' : {
        'name' : 'Camp Site',
        'intro' : line101,
        'NORTH' : 'Forest',
        'SOUTH' : 'Town',
        'WEST' : 'Cliff',
        'EXPLORE': line103,
        'REST': 'rest',
        'fire' : 3,
        'spawn_rate' : 0,
    },

    'Cliff' : {
        'name' : 'Cliff Side',
        'intro' : line601,
        'EAST' : 'Camp',
        'EXPLORE': line602,
        'EXAMINE' : cliff_examine,
        'spawn_rate' : 2,
        'enemy_spawn_set' : enemy_spawn0,
        'chest' : 'CLOSED',
    },
#Town start
  'Town' : {
        'name' : 'Town Center',
        'intro' : line201,
        'NORTH' : 'Camp',
        'EAST' : 'Shop',
        'SOUTH' : 'Castle',
        'WEST' : 'Inn',
        'EXPLORE': line202,
        'spawn_rate' : 0,
    },

  'Shop' : {
        'name' : 'Shop',
        'intro' : line301,
        'WEST' : 'Town',
        'EXIT' : 'Town',
        'EXPLORE': line304,
        'BUY' : "BUY",
        'spawn_rate' : 0,
    },

  'Inn' : {
        'name' : 'Inn',
        'intro' : line401,
        'EAST' : 'Town',
        'EXIT' : 'Town',
        'EXPLORE': line404,
        'REST' : 'rest',
        'spawn_rate' : 0,
    },

  'Castle' : {
        'name' : 'Royal Castle',
        'intro' : line501,
        'NORTH' : 'Town',
        'EXIT' : 'Town',
        'EXPLORE': line502,
        'spawn_rate' : 0,
        'SPEAK' : castle_speak,
        'speach' : 0,
        'event' : 0,
    }, #Town end

  'Forest' : {
        'name' : 'Deep Forest',
        'intro' : line701,
        #'NORTH' : 'Thicket',
        'EAST' : 'Hill',
        'SOUTH' : 'Camp',
        'WEST' : 'River',
        'EXPLORE': line702,
        'spawn_rate' : 2,
        'enemy_spawn_set' : enemy_spawn1,
    },

  'Hill' : {
        'name' : 'Rocky Hill',
        'intro' : line801,
        'NORTH' : 'Shrine',
        'EAST' : 'Cave',
        'SOUTH' : 'LOCKED',
        'WEST' : 'Forest',
        'EXPLORE' : line802,
        'EXAMINE' : hill_examine, 
        'spawn_rate': 3,
        'enemy_spawn_set' : enemy_spawn6,
        'LOCK' : hill_lock,
    },
  
  'Shrine' : {
        'name' : 'Mystic Shrine',
        'intro' : line1101,
        'SOUTH' : 'Hill',
        'EXPLORE': line1102,
        'SPEAK' : shrine_speak,
        'PRAY' : 'PRAY',
        'speach' : 0,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn4,
    },
#Dungeon 1 start
  'Cave' : {
        'name' : 'Bear Cave',
        'intro' : line901,
        'WEST' : 'Hill',
        'EAST' : 'LOCKED',
        'EXPLORE': line906,
        'EXAMINE' : cave_examine,
        'spawn_rate' : 0,
        'boss' : ['Bear'],
        'foe' : p12,
        'LOCK' : cave_lock,
    },

  'Cave1' : {
        'name' : 'Rocky Cave',
        'intro' : line916,
        'NORTH' : 'Cave2',
        'SOUTH' : 'Cave3',
        'WEST' : 'Cave',
        'EXPLORE': line917,
        'spawn_rate' : 4,
        'enemy_spawn_set' : enemy_spawn8,
    },

  'Cave2' : {
        'name' : 'Rocky Cave',
        'intro' : line922,
        'SOUTH' : 'Cave1',
        'EXPLORE': line923,
        'EXAMINE' : cave2_examine,
        'spawn_rate' : 4,
        'enemy_spawn_set' : enemy_spawn8,
        'chest' : 'CLOSED',
    },
  'Cave3' : {
        'name' : 'Rocky Cave',
        'intro' : line931,
        'NORTH' : 'Cave1',
        'SOUTH' : 'Cave4',
        'EXPLORE': line932a,
        'spawn_rate' : 4,
        'enemy_spawn_set' : enemy_spawn8,
    },
  'Cave4' : {
        'name' : 'Rocky Cave',
        'intro' : line937,
        'NORTH' : 'Cave3',
        'EAST' : 'LOCKED',
        'EXPLORE' : line938,
        'EXAMINE' : cave4_examine,
        'spawn_rate' : 0,
        'enemy_spawn_set' : enemy_spawn8,
        'boss' : ['Hobgoblin Gang'],
        'boss_ambush' : cave4_boss_ambush,
        'foe' :  p23,
        'LOCK' : cave4_lock,
    },
  'Cave5' : {
        'name' : "Queen's Chamber",
        'intro' : line948,
        'WEST' : 'Cave4',
        'EXPLORE': line950,
        'spawn_rate' : 0,
        'boss' : ['Goblin Queen'],
        'boss_ambush' : cave5_boss_ambush,
        'foe' : p22,
    }, #Dungeon 1 end

  'River' : {
        'name' : 'River Channel',
        'intro' : line1201,
        'NORTH' : 'Lake',
        'EAST' : 'Forest',
        'SOUTH' : 'Waterfall',
        'EXPLORE': line1202,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn5,
    },

  'Waterfall' : {
        'name' : 'Waterfall Pool',
        'intro' : line1301,
        'NORTH' : 'River',
        'EXPLORE': line1302,
        'EXAMINE' : waterfall_examine,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn5,
        'chest' : 'CLOSED',
        'event' : 0,
    },

  'Lake' : {
        'name' : 'Lake Beach',
        'intro' : line1401,
        'NORTH' : 'Boat',
        'EAST' : 'LOCKED',
        'SOUTH' : 'River',
        'EXPLORE': line1402,
        'EXAMINE': lake_examine,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn5,
        'foe' : p16,
        "LOCK" : lake_lock,
    },

  'Boat' : {
        'name' : 'Boat House',
        'intro' : line1501,
        'SOUTH' : 'Lake',
        'EXPLORE': line1502,
        'SPEAK' : boat_speak,
        'speach' : 0,
        'spawn_rate' : 0,
    },

  'Berry' : {
        'name' : 'Berry Patch',
        'intro' : line1001,
        'NORTH' : 'Hill',
        'EAST' : 'Meadow',
        'EXPLORE': line1002,
        'EXAMINE' : berry_examine,
        'spawn_rate' : 2,
        'enemy_spawn_set' : enemy_spawn3,
        'foe' : p15,
        'chest' : 'CLOSED',
    },

  'Meadow' : {
        'name' : 'Flower Meadow',
        'intro' : line1701,
        #'NORTH' : 'Witch',
        'EAST' : 'Oak',
        'SOUTH' : 'Village',
        'WEST' : 'Berry',
        'EXPLORE': line1702,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn9,
        'foe' : None,
        'chest' : None,
        'event' : None,
    },
#Quite Village start
  'Village' : {
        'name' : 'Quiet Village',
        'intro' : line1801,
        'NORTH' : 'Meadow',
        #'EAST' : 'Farm',
        'SOUTH' : 'Tavern',
        'WEST' : 'Smith',
        'EXPLORE': line1802,
        'spawn_rate' : 0,
    },

  'Tavern' : {
        'name' : 'Tavern & Inn',
        'intro' : line401b,
        'NORTH' : 'Village',
        'EXIT' : 'Village',
        'EXPLORE': line404b,
        'REST' : 'rest',
        'spawn_rate' : 0,
    },

  'Smith' : {
        'name' : "Smith's Workshop",
        'intro' : line1901,
        'EAST' : 'Village',
        'EXIT' : 'Village',
        'EXPLORE': line1902,
        'UPGRADE' : village_smith,
        'upgrade_cost' : 75,
        'spawn_rate' : 0,
    },

#Quite Village end
  'Oak' : {
        'name' : 'Great Oak',
        'intro' : line2001,
        'WEST' : 'Meadow',
        'EXPLORE': line2002,
        'EXAMINE' : oak_examine,
        'spawn_rate' : 0,
 
    },

  'Hive' : {
        'name' : 'Bee Hive',
        'intro' : line2104,
        'EXIT' : 'Oak',
        'EXPLORE': line2105,
        'EXAMINE' : hive_examine,
        'spawn_rate' : 7,
        'enemy_spawn_set' : enemy_spawn10,
        'boss' : ['Giant Bee Queen'],
        'boss_ambush' : hive_boss_ambush,
        'foe' : p24,
        'chest' : "CLOSED",
    },
  'Mushroom' : {
        'name' : 'Mushroom Grove',
        'intro' : line1601,
        #'NORTH' : 'Swamp',
        #'SOUTH' : 'Fairy',
        'WEST' : 'Lake',
        'EXPLORE': line1602,
        'EXAMINE' : mushroom_examine,
        'spawn_rate' : 3,
        'enemy_spawn_set' : enemy_spawn7,
        #'LOCK' : None,
        'chest' : "CLOSED",
        #'event' : None,
    },
}


#define player key items

key_items = {
    '': {
        'name': '',
        'description': '',
    },
    'LANTERN': {
        'name': 'LANTERN',
        'description': 'A lantern that attaches to a belt for hands free use. Allows travel through dark areas.',   
    },
    'AXE': {
        'name': 'AXE',
        'description': 'An axe made for chopping wood. Not sure what a bear was doing with this...',
    },
    'PENDANT': {
        'name': 'PENDANT',
        'description': 'A round silver PENDANT with the words "for my love" engraved on the back. Found stuck in an olive tree burl. Who knows how many years it has been there?',
    },
  
    'SALMON': {
        'name': 'SALMON',
        'description': 'A not so lucky fish found at the Waterfall. Could make for a tasty meal.',
    },
    'BUCKLER': {
        'name': 'BUCKLER',
        'description': 'A small center-grip shield made of hardened steel. Looks like its been a little neglected over the years.',
    },
    'MESSER': {
        'name': 'Messer',
        'description': 'A long single edged sword with a knife like construction. It doesnt show signs of use, but the Friar kept it well maintained.'
    },
    'HEROS MEDAL': {
        'name': 'HEROS MEDAL',
        'description': 'A gold medal found on a corpse covered in mushrooms. Engraved with the royal crest on the front; the back reads "For Jeremy the Goblin-Slayer". Seems to have some significance to the royal family.',
    },
    'IRON KEY': {
        'name': 'IRON KEY',
        'description': 'A small key made of iron. Dropped from a pesky Hobgoblin.',
    },
    'DRAGON BONE KEY': {
        'name': 'DRAGON BONE KEY',
        'description': 'A key made of Dragon bone. Dragon Bone Keys are said to be used to secure magical seals.',
    },
    'ROYAL JELLY': {
        'name': 'ROYAL JELLY',
        'description':'A jar of Giant Bee Royal Jelly. This substance is capable of enhancing the healing properties of potions. Just a tiny bit mixed in will greatly increase the potancy.',
    },
}