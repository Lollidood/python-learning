# Export Students to JSON


  
import csv
import json


def export_students_to_json(students: str, courses: str) -> None:
    """Экспортирует студентов и их курсы в JSON файл."""
    with open(students, "r", encoding="utf-8") as students_file, \
         open(courses, "r", encoding="utf-8") as courses_file, \
         open("student_courses.json", "w", encoding="utf-8") as out_file:

        students_reader = csv.reader(students_file, delimiter=":")
        courses_reader = csv.reader(courses_file, delimiter=":")

        next(students_reader)
        next(courses_reader)

        students_list = [row for row in students_reader]
        courses_list = [row for row in courses_reader]

        student_dict = {}
        for student in students_list:
            for course in courses_list:
                student_dict.setdefault(student[1], [student[0]])
                if student[0] == course[0]:
                    student_dict[student[1]].append(course[1])

        result = []
        for name, values in student_dict.items():
            result.append({
                "id": int(values[0]),
                "name": name,
                "courses": sorted(values[1:])
            })

        json.dump(result, out_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    export_students_to_json("students.csv", "enrollments.csv")
