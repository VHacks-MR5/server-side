import sqlite3
from faker import Faker
import random
fake = Faker('es_MX')

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE refugees (id integer PRIMARY KEY, first_name text, last_name text, phone text, email text, picturepath text UNIQUE, last_seen text, age integer, gender text, nationality text, nickname text, trafficked bool)")

for i in range(1,5566):
	name = fake.name().split(' ')
	addr = fake.address().split('\n')
	trafficked = random.randint(0,1)
	cursor.execute("""
	INSERT INTO refugees (first_name, last_name, nickname, last_seen, picturepath, trafficked) VALUES ("{}", "{}", "{}", "{}", "{:07d}", "{}") 
	""".format(name[-2],name[-1],name[0],addr[-1],i,trafficked))
#print(l1)	
cursor.execute("SELECT * FROM refugees")
print(cursor.fetchall())
db.commit()
db.close()
