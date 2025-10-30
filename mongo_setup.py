from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_management"]

print("✅ MongoDB Database Created:", db.name)
