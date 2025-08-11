# **SCHOOL DATABASE**

This is a command-line-based Student Management System written in Python. It allows users to perform basic CRUD operations (Create, Read, Update, Delete) on student records, which are stored both in a local JSON file and in a MongoDB database.


---

## 📁 Features

- Add (append) new students
- View (call) student details by ID
- Update student details
- Delete student records
- Stores data persistently using a local JSON file (`school_db.json`) and MongoDB (`students` collection)

---

## 🛠️ Technologies Used

- Python 3
- JSON for local data storage
- MongoDB for database storage
- File I/O

---

## ✅ Required Modules

- `json` — To read from and write to JSON files
- `os` — To check if the JSON file exists
- `pymongo` — To interact with MongoDB

---

## 📦 Project Structure

```
SchoolDB/
├── .gitignore
├── playground-1.mongodb.js
├── README.md
├── requirements.txt
├── SchoolDB.code-workspace
├── school_db.json
├── students.json (legacy, not used by default)
├── work.py
```

---

## 🚀 How to Use

1. Make sure you have Python 3 installed.
2. Install required dependencies:
   ```sh
   pip install pymongo
   ```
3. Ensure you have a running MongoDB instance (default: mongodb://localhost:27017/).
4. Run the program from the terminal:
   ```sh
   python3 work.py
   ```
5. Follow the on-screen prompts to manage student records.

All student data is stored in `school_db.json` locally and in the `students` collection in MongoDB.

---

## 📝 Example Student Record

```json
{
    "id": "001",
    "name": "Anas",
    "age": 15,
    "grade": "10"
}
```

---

## ⚠️ Notes

- The main program requires the `pymongo` package and a running MongoDB server.
- The `requirements.txt` may list additional packages for experimentation (e.g., HTTP requests), but only `pymongo` is required for core functionality.
- There is a MongoDB playground script (`playground-1.mongodb.js`) for database experimentation (not required for the Python app).
- All CRUD operations are performed both locally and in MongoDB.
