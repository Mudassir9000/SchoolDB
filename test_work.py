#Run file --->  python3 -m unittest SchoolDB/test_work.py

import unittest
import os
import json
from work import Student, SchoolDatabase

class TestSchoolDatabase(unittest.TestCase):
    TEST_DB = "test_school_db.json"

    def setUp(self):
        # Ensure test DB is clean before each test
        if os.path.exists(self.TEST_DB):
            os.remove(self.TEST_DB)
        self.db = SchoolDatabase(filename=self.TEST_DB)

    def tearDown(self):
        # Clean up test DB after each test
        if os.path.exists(self.TEST_DB):
            os.remove(self.TEST_DB)

    def test_append_and_get_student(self):
        print("\nTest: Append and Get Student")
        student = Student("1", "Alice", 15, "10th")
        self.db.append_student(student)
        result = self.db.get_student("1")
        self.assertIsNotNone(result, "Student with ID '1' should exist after being added.")
        self.assertEqual(result["name"], "Alice", "Student name should be 'Alice'.")
        self.assertEqual(result["age"], 15, "Student age should be 15.")
        self.assertEqual(result["grade"], "10th", "Student grade should be '10th'.")
        print("Student added and retrieved successfully.")

    def test_get_nonexistent_student(self):
        print("\nTest: Get Nonexistent Student")
        result = self.db.get_student("999")
        self.assertIsNone(result, "Should return None for a nonexistent student.")
        print("Correctly handled retrieval of nonexistent student.")

    def test_update_student(self):
        print("\nTest: Update Student")
        student = Student("2", "Bob", 16, "11th")
        self.db.append_student(student)
        updated = self.db.update_student("2", name="Bobby", age=17, grade="12th")
        self.assertTrue(updated, "Update should return True for existing student.")
        result = self.db.get_student("2")
        self.assertEqual(result["name"], "Bobby", "Student name should be updated to 'Bobby'.")
        self.assertEqual(result["age"], 17, "Student age should be updated to 17.")
        self.assertEqual(result["grade"], "12th", "Student grade should be updated to '12th'.")
        print("Student updated successfully.")

    def test_update_nonexistent_student(self):
        print("\nTest: Update Nonexistent Student")
        updated = self.db.update_student("999", name="Ghost")
        self.assertFalse(updated, "Update should return False for nonexistent student.")
        print("Correctly handled update of nonexistent student.")

    def test_delete_student(self):
        print("\nTest: Delete Student")
        student = Student("3", "Charlie", 14, "9th")
        self.db.append_student(student)
        deleted = self.db.delete_student("3")
        self.assertTrue(deleted, "Delete should return True for existing student.")
        self.assertIsNone(self.db.get_student("3"), "Student should not exist after deletion.")
        print("Student deleted successfully.")

    def test_delete_nonexistent_student(self):
        print("\nTest: Delete Nonexistent Student")
        deleted = self.db.delete_student("999")
        self.assertFalse(deleted, "Delete should return False for nonexistent student.")
        print("Correctly handled deletion of nonexistent student.")

    def test_persistence(self):
        print("\nTest: Persistence of Data")
        student = Student("4", "Dana", 13, "8th")
        self.db.append_student(student)
        # Reload database to check persistence
        db2 = SchoolDatabase(filename=self.TEST_DB)
        result = db2.get_student("4")
        self.assertIsNotNone(result, "Student should persist after reloading database.")
        self.assertEqual(result["name"], "Dana", "Student name should persist as 'Dana'.")
        print("Student data persisted and loaded successfully.")

if __name__ == "__main__":
    unittest.main()
