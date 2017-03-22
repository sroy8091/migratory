import csv
from pymongo import MongoClient

client = MongoClient()
db = client.bird_db

header = db.bird_list.find_one({'header': {'$exists': True}})['header']     # fetch saved header
cursor = db.bird_list.find({'SpcRecID': {'$exists': True}})    # fetches all birds (all birds have SpcRecID)

with open('bird_out.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=header)
	writer.writeheader()
	for document in cursor:
		del document['_id']
		writer.writerow(document)