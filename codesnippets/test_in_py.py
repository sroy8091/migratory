import csv
from pymongo import MongoClient

client = MongoClient()
db = client.bird_db

rows = []
with open('migratory_species.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	rows = [row for row in reader]

	#db.bird_list.drop()  #if discarding previous data
	result = db.bird_list.insert_one({'header': reader.fieldnames})
	result = db.bird_list.insert_many(rows)