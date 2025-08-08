import json
import os
from pymongo import MongoClient

class Student:
    def __init__(self, student_id, name, age, grade):
        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
class SchoolDatabase:
    def __init__(self, filename="school_db.json"):
        self.filename = filename
        self.students = self._load_students()
        # MongoDB setup
        self.mongo_client = MongoClient("mongodb://localhost:27017/")
        self.mongo_db = self.mongo_client["school"]
        self.mongo_collection = self.mongo_db["students"]

    def _load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return []

    def append_student(self, student):
        student_dict = student.to_dict()
        self.students.append(student_dict)
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)
        # MongoDB insert
        self.mongo_collection.insert_one(student_dict)

    def get_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        # Try MongoDB if not found in local
        mongo_student = self.mongo_collection.find_one({"id": student_id})
        if mongo_student:
            mongo_student.pop("_id", None)
            return mongo_student
        return None

    def update_student(self, student_id, name=None, age=None, grade=None):
        updated = False
        for student in self.students:
            if student["id"] == student_id:
                if name is not None:
                    student["name"] = name
                if age is not None:
                    student["age"] = age
                if grade is not None:
                    student["grade"] = grade
                with open(self.filename, "w") as file:
                    json.dump(self.students, file, indent=4)
                updated = True
                break
        # MongoDB update
        update_fields = {}
        if name is not None:
            update_fields["name"] = name
        if age is not None:
            update_fields["age"] = age
        if grade is not None:
            update_fields["grade"] = grade
        if update_fields:
            result = self.mongo_collection.update_one({"id": student_id}, {"$set": update_fields})
            if result.modified_count > 0:
                updated = True
        return updated

    def delete_student(self, student_id):
        deleted = False
        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                del self.students[i]
                with open(self.filename, "w") as file:
                    json.dump(self.students, file, indent=4)
                deleted = True
                break
        # MongoDB delete
        result = self.mongo_collection.delete_one({"id": student_id})
        if result.deleted_count > 0:
            deleted = True
        return deleted

    def call_student(self, student_id):
        student = self.get_student(student_id)
        if student:
            print(f"{student['name']} (ID: {student['id']}), age {student['age']}, grade {student['grade']}")
        else:
            print(f"No student found with ID {student_id}.")

def call_student_by_input():
    db = SchoolDatabase(filename="students.json")
    student_id = input("Enter the student ID to call: ")
    db.call_student(student_id)

def append_student_by_input():
    db = SchoolDatabase(filename="students.json")
    student_id = input("Enter new student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student = Student(student_id, name, age, grade)
    db.append_student(student)
    print(f"Student {name} added.")

def update_student_by_input():
    db = SchoolDatabase(filename="students.json")
    student_id = input("Enter the student ID to update: ")
    student = db.get_student(student_id)
    if not student:
        print("No student found with that ID.")
        return
    name = input(f"Enter new name (leave blank to keep '{student['name']}'): ") or student['name']
    age_input = input(f"Enter new age (leave blank to keep '{student['age']}'): ")
    age = int(age_input) if age_input else student['age']
    grade = input(f"Enter new grade (leave blank to keep '{student['grade']}'): ") or student['grade']
    db.update_student(student_id, name, age, grade)
    print("Student updated.")

def delete_student_by_input():
    db = SchoolDatabase(filename="students.json")
    student_id = input("Enter the student ID to delete: ")
    if db.delete_student(student_id):
        print("Student deleted.")
    else:
        print("No student found with that ID.")

if __name__ == "__main__":
    print("1. Call student by ID")
    print("2. Append new student")
    print("3. Update student")
    print("4. Delete student")
    choice = input("Choose an option (1/2/3/4): ")
    if choice == "1":
        call_student_by_input()
    elif choice == "2":
        append_student_by_input()
    elif choice == "3":
        update_student_by_input()
    elif choice == "4":
        delete_student_by_input()
    else:
        print("Invalid option.")