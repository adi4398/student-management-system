from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_management_nosql"]

achievement_logs = db["achievement_logs"]


