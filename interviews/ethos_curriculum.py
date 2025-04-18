"""You're developing a system for scheduling advising meetings with students in a Computer Science program.
Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses
share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course
that the student will be taking when they are halfway through their program. (If a track has an even
number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
    Software Design
    Computer Networks
    Computer Architecture
    Data Structures
    Algorithms
    Foundations of Computer Science
    Operating Systems

Sample output 1:
    "Data Structures"


Sample input 2:
prereqs_courses2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]


Sample output 2:
    "Foundations of Computer Science"

Sample input 3:
prereqs_courses3 = [
    ["Data Structures", "Algorithms"],
]


Sample output 3:
    "Data Structures"

Complexity analysis variables:

n: number of pairs in the input

time complexity: O(n)
space complexity: O(n)




"""

prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]

prereqs_courses2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]

prereqs_courses3 = [
    ["Data Structures", "Algorithms"],
]


def curriculum(prereqs_courses):
    n = len(prereqs_courses)

    courses = {}
    for first, second in prereqs_courses:
        courses[first] = courses.get(first, 0) + 1
        courses[second] = courses.get(second, 0) + 1

    outliers = []
    for course, count in courses.items():
        if count == 1:
            outliers.append(course)

    answer = []
    for course in prereqs_courses:
        if course[0] in outliers:
            answer.append(course[0])

    mapping = {}
    for first, second in prereqs_courses:
        mapping[first] = second

    while len(answer) < n + 1:
        if answer[-1] in mapping:
            answer.append(mapping[answer[-1]])
        else:
            break

    if len(answer) % 2 == 0:
        return answer[len(answer) // 2 - 1]
    else:
        return answer[len(answer) // 2]


print(curriculum(prereqs_courses1))
print(curriculum(prereqs_courses2))
print(curriculum(prereqs_courses3))





