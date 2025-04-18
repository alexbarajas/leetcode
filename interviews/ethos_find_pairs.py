"""
You are a developer for a university. Your current project is to develop a system for students to find
courses they share with friends. The university has a system for querying courses students are enrolled
in, returned as a list of (ID, course) pairs.

Write a function that takes in a list of (student ID number, course name) pairs and returns, for every
pair of students, a list of all courses they share.
"""


student_course_pairs_1 = [
    ("0", "Math"),
    ("1", "Math"),
    ("2", "Math"),
    ("0", "Science"),
    ("2", "Science"),
    ("1", "Gym"),
    ("3", "Gym"),
    ("3", "Physics")
]

student_course_pairs_2 = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
]


def find_pairs(student_course_pairs):
    student_courses = {}
    students = []

    for student, course in student_course_pairs:
        if student not in student_courses:
            student_courses[student] = [course]
        else:
            student_courses[student].append(course)
        if student not in students:
            students.append(student)

    answer = {}
    for first in range(len(students) - 1):
        for second in range(first + 1, len(students)):
            answer[(students[first], students[second])] = []

    for first, second in answer:
        for value in student_courses[first]:
            if value in student_courses[second]:
                answer[(first, second)].append(value)

    return answer


print(find_pairs(student_course_pairs_1))
print(find_pairs(student_course_pairs_2))

