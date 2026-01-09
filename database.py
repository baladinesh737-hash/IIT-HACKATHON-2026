from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dca_platform"]

cases_collection = db["cases"]
users_collection = db["users"]
logs_collection = db["audit_logs"]
