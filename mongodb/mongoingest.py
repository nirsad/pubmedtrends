#Ingest article titles, author, and citation information into MongoDB
#A new collection is created on each day the pipeline is run

cluster = MongoClient('localhost', 27017)
database = cluster['ArticleData']
new_collection_name = date.today().strftime("%b_%d_%Y")
collection = database[new_collection_name]
with open(os.path.join(os.getcwd(), '..','article_data.csv'), 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for id, row in enumerate(reader):
		if row[0] == 'Title' and row[1] == 'Authors':
			pass
		else:
			collection.insert_one({'_id':id, 'Title':row[0], 'Authors':row[1], 'Citations':row[2]}) 