import csv
import os

FILE_PATH = './students.csv'

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Science', 'English'])
        writer.writerow(['Alice', 85, 90, 88])
        writer.writerow(['Bob', 78, 82, 75])
        writer.writerow(['Charlie', 92, 88, 94])

students = []

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        math = float(row['Math'])
        science = float(row['Science'])
        english = float(row['English'])
        
        avg = round((math + science + english) / 3, 2)
        students.append({
            'Name': name,
            'Math': math,
            'Science': science,
            'English': english,
            'Average': avg
        })

total_math = sum(s['Math'] for s in students)
total_science = sum(s['Science'] for s in students)
total_english = sum(s['English'] for s in students)
count = len(students)

class_avg_math = round(total_math / count, 2)
class_avg_science = round(total_science / count, 2)
class_avg_english = round(total_english / count, 2)

top_student = max(students, key=lambda s: s['Average'])

with open('student_report.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Name', 'Math', 'Science', 'English', 'Average']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
    

print("Student Report Generated")
print("------------------------")

for s in students:
    print(f"{s['Name']} - Average: {s['Average']}")

print("Class Averages:")
print(f"Math: {class_avg_math}")
print(f"Science: {class_avg_science}")
print(f"English: {class_avg_english}")

print(f"Top Performer: {top_student['Name']} ({top_student['Average']})")
print("Report saved to 'student_report.csv'")