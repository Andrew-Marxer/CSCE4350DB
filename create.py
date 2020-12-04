import sqlite3

# CREATE
connection = sqlite3.connect("osrs.db")
cursor1 = connection.cursor()
cursor1.execute("PRAGMA foreign_keys = ON;")
# cursor2 = connection.cursor()
# cursor3 = connection.cursor()
create1 = "CREATE TABLE IF NOT EXISTS monster(Monster_name TEXT PRIMARY KEY, " \
          "level INTEGER, " \
          "Location TEXT);"
create2 = "CREATE TABLE IF NOT EXISTS item(Item_name TEXT PRIMARY KEY," \
          "value INTEGER, " \
          "combat_item BOOLEAN);"
create3 = "CREATE TABLE IF NOT EXISTS drops(" \
          "dropRate INTEGER," \
          "value INTEGER," \
          "Monster_name TEXT," \
          "Item_name TEXT, " \
          "FOREIGN KEY(Monster_name) REFERENCES monster(Monster_name), " \
          "FOREIGN KEY(Item_name) REFERENCES item(Item_name));"
cursor1.execute(create1)
cursor1.execute(create2)
cursor1.execute(create3)
connection.commit()
connection.close()
