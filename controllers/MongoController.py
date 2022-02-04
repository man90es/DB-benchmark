import pymongo


class MongoController():
	name = "MongoDB"

	def __init__(self, host, port):
		client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
		db = client["bench"]
		self.collection = db["bench"]

	def create_one(self, identifier, data):
		_data = data.copy()
		_data["_id"] = identifier
		result = self.collection.insert_one(_data)
		return result.inserted_id

	def read_one(self, identifier):
		result = self.collection.find_one({"_id": identifier})
		return result

	def update_one(self, identifier, data):
		result = self.collection.update_one({"_id": identifier}, {"$set": data})
		return result.modified_count

	def delete_one(self, identifier):
		result = self.collection.delete_one({"_id": identifier})
		return result.deleted_count
