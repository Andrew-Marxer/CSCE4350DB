import sqlite3
#POPULATE
connection = sqlite3.connect("osrs.db")

cursor1 = connection.cursor()
cursor2 = connection.cursor()
cursor3 = connection.cursor()

#monsters
data1 = [("Vorkath",732,"Ungael"),
         ("Dagganoth Prime",303, "Waterbirth Island"),
         ("Dagganoth Rex",303, "Waterbirth Island"),
         ("Dagganoth Supreme",303, "Waterbirth Island"),
         ("Alchemical Hydra", 194, "Karuulm Slayer Dungeon"),
         ("Nightmare of Ashihama", 814, "Sisterhood Sanctuary"),
         ("Demonic Gorilla", 275, "Crash Site Cavern"),
         ("Zulrah", 725, "Zul-Andra")]
for monster in data1:
    name = monster[0]
    lvl = monster[1]
    location = monster[2]
    doInsert = """INSERT INTO monster(Monster_name, level, Location) VALUES (?,?,?);"""
    data_tuple = (name,lvl,location)
    cursor1.execute(doInsert, data_tuple)
cursor1.execute("SELECT * FROM monster;")
print(cursor1.fetchall())

#items
data2 = [("Dragon Platelegs/plateskirt", 161000, True),
         ("Vorkath Head", 0, False),
         ("Draconic Visage", 4053861, True),
         ("Skeletal Visage", 14589662, True),
         ("Onyx bolt tips", 250000, True),
         ("Seer's Ring", 355278, True),
         ("Berserker's Ring", 2548618, True),
         ("Warrior's Ring", 26568, True),
         ("Archer's Ring", 4548584, True),
         ("Hydra Leather", 5667705, False),
         ("Hydra Claw", 59322322,False),
         ("Inquisitor's helm", 162049024, True),
         ("Inquisitor's hauberk", 302279995, True),
         ("Inquisitor's plateskirt", 302200986, True),
         ("Inquisitor's mace", 764078982, True),
         ("Eldritch orb", 102310225, False),
         ("Harmonized orb", 1130596059, False),
         ("Volatile orb", 182179783, False),
         ("Zenyte shard", 10781436, False),
         ("Monkey tail",438360,False),
         ("Tanzanite fang", 3056007,True),
         ("Magic fang", 2944049, True),
         ("Serpentine visage", 2924368, True),
         ("Uncut onyx", 1439325, False)]

for item in data2:
    doInsert = """INSERT INTO item(Item_name, value, combat_item) VALUES (?,?,?);"""
    data_tuple = (item[0], item[1], item[2])
    cursor1.execute(doInsert, data_tuple)
cursor1.execute("SELECT * FROM item;")
print(cursor1.fetchall())
#drops -- relation between monster and item'

data3 = [(75, "Vorkath", "Dragon Platelegs/plateskirt"),
         (50, "Vorkath", "Vorkath Head"),
         (5000, "Vorkath", "Draconic Visage"),
         (5000, "Vorkath", "Skeletal Visage"),
         (370, "Vorkath", "Onyx bolt tips"),
         (128, "Dagganoth Rex", "Berserker's Ring"),
         (128, "Dagganoth Rex", "Warrior's Ring"),
         (128, "Dagganoth Supreme", "Archer's Ring"),
         (514, "Alchemical Hydra", "Hydra Leather"),
         (1000, "Alchemical Hydra", "Hydra Claw"),
         (343, "Nightmare of Ashihama", "Inquisitor's helm"),
         (343, "Nightmare of Ashihama", "Inquisitor's hauberk"),
         (343, "Nightmare of Ashihama", "Inquisitor's plateskirt"),
         (686, "Nightmare of Ashihama", "Inquisitor's mace"),
         (1029, "Nightmare of Ashihama", "Eldritch orb"),
         (1029, "Nightmare of Ashihama", "Harmonized orb"),
         (1029, "Nightmare of Ashihama", "Volatile orb"),
         (300, "Demonic Gorilla", "Zenyte shard"),
         (300, "Demonic Gorilla", "Monkey tail"),
         (612, "Zulrah", "Tanzanite fang"),
         (612, "Zulrah", "Magic fang"),
         (612, "Zulrah", "Serpentine visage"),
         (612, "Zulrah", "Uncut onyx")]

for drop in data3:
    doInsert = """INSERT INTO drops(dropRate, Monster_name, Item_name) VALUES (?,?,?);"""
    data_tuple = (drop[0], drop[1], drop[2])
    cursor1.execute(doInsert, data_tuple)
cursor1.execute("SELECT * FROM drops;")
print(cursor1.fetchall())
connection.commit()