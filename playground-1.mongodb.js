// Select the database to use.
use('schoolDB');

// Insert a few documents into the students collection.
db.getCollection('students').insertMany([
  { id: '001', name: 'Anas', age: 15, grade: '10' },
  { id: '002', name: 'Sana', age: 15, grade: '10th' },
  { id: '003', name: 'Ahmed', age: 13, grade: '8th' },
  { id: '005', name: 'kaka', age: 26, grade: 'c' }
]);

// Find and print all students
const allStudents = db.getCollection('students').find().toArray();
console.log('Sample Output:', allStudents);
