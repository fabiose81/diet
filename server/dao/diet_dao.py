import logging
from bson.objectid import ObjectId

logging.basicConfig(level=logging.INFO)

class DietDAO:
    def __init__(self, db):
        self.collection = db['diet'] 

    def add(self, diet_entry):
        result = self.collection.insert_one(diet_entry)    
        return str(result.inserted_id)

    def get_all(self):
        return list(self.collection.find())
    
    def get(self, id):
        return self.collection.find_one({"_id" : ObjectId(id)})

    def update(self, id, diet_entry):
        result = self.collection.update_one({'_id': ObjectId(id)}, {'$set': diet_entry})
        return result.modified_count

    def delete(self, id):
        result = self.collection.delete_one({'_id': ObjectId(id)})
        return result.deleted_count