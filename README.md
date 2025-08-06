# **SCHOOL DATABASE**

This is a simple command-line-based Student Management System written in Python. It allows users to perform basic CRUD operations (Create, Read, Update, Delete) on student records, which are stored in a JSON file.

---

## 📁 Features

- Add (append) new students
- View (call) student details by ID
- Update student details
- Delete student records
- Stores data persistently using a JSON file (`students.json`)

---

## 🛠️ Technologies Used

- Python 3
- JSON for data storage
- File I/O

---

## ✅ Standard Library Modules Used

- `json` — To read from and write to JSON files
- `os` — To check if the JSON file exists

---

## 📦 Project Structure

```
SchoolDB/
├── .gitignore
├── playground-1.mongodb.js
├── README.md
├── requirements.txt
├── SchoolDB.code-workspace
├── students.json
├── work.py
```

---

## 🚀 How to Use

1. Make sure you have Python 3 installed.
2. Run the program from the terminal:
   ```sh
   python3 work.py
   ```
3. Follow the on-screen prompts to manage student records.

All student data is stored in `students.json` in the project directory.

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

- No external dependencies are required for the main functionality.
- The `requirements.txt` lists packages for optional HTTP requests (not used in the main program).
- There is a MongoDB playground script (`playground-1.mongodb.js`) for database experimentation (not required for the Python app).
- All CRUD operations are performed
