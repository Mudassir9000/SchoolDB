# Python equivalent using pymongo
from pymongo import MongoClient

# Connect to MongoDB (default localhost:27017)
client = MongoClient('mongodb://localhost:27017/')

db = client['schoolDB']
students_collection = db['students']

# Insert documents into the students collection
students_collection.insert_many([
    { 'id': '001', 'name': 'Anas', 'age': 15, 'grade': '10' },
    { 'id': '002', 'name': 'Sana', 'age': 15, 'grade': '10th' },
    { 'id': '003', 'name': 'Ahmed', 'age': 13, 'grade': '8th' },
    { 'id': '005', 'name': 'kaka', 'age': 26, 'grade': 'c' }
])

# Find and print all students
all_students = list(students_collection.find({}, {'_id': 0}))
print('Sample Output:', all_students)
