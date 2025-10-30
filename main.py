import mysql.connector
from pymongo import MongoClient

# Connect to MySQL
mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="student_db"
)
mysql_cursor = mysql_db.cursor()

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["student_management"]
mongo_collection = mongo_db["students"]

# Create Table in MySQL (if not exists)
mysql_cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50)
)
""")

# Insert sample record in SQL
mysql_cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", ("Alice", 21, "B.Tech"))
mysql_db.commit()

# Insert same record in MongoDB
mongo_collection.insert_one({"name": "Alice", "age": 21, "course": "B.Tech"})

print("✅ Data inserted into both MySQL & MongoDB successfully!")
