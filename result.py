import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Project1"]
                    
students_collection = db["User"]

query = {"_id": id}

result = students_collection.find(query)

name = result.get("Name")

department = result.get("Department")

print(name)
print(department)