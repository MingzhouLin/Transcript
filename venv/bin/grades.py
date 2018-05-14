# -*- coding: UTF-8 -*-
class StudentGrade:
    'students grade'

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    def set_a1(self, a1):
        self.a1 = a1

    def set_a2(self, a2):
        self.a2 = a2

    def set_project(self, project):
        self.project = project

    def set_test1(self, test1):
        self.test1 = test1

    def set_test2(self, test2):
        self.test2 = test2


students = {}
classes = open("class.txt", "r")
student = classes.readline()

while student != "":
    studentAttrs = student.split("|")
    stu = StudentGrade(studentAttrs[0], studentAttrs[1], studentAttrs[2])
    students[studentAttrs[0]] = stu
    student = classes.readline()
classes.close()

a1 = open("a1.txt", "r")
fullA1 = int(a1.readline())
ass1 = a1.readline()
while ass1 != "":
    a1Score = ass1.split("|")
    students[a1Score[0]].set_a1(a1Score[1])
    ass1 = a1.readline()
a1.close()

a2 = open("a2.txt", "r")
fullA2 = int(a2.readline())
ass2 = a2.readline()
while ass2 != "":
    a2Score = ass2.split("|")
    students[a2Score[0]].set_a2(a2Score[1])
    ass2 = a2.readline()
a2.close()

projects = open("project.txt", "r")
fullProject = int(projects.readline())
project = projects.readline()
while project != "":
    projectScore = project.split("|")
    students[projectScore[0]].set_project(projectScore[1])
    project = projects.readline()
projects.close()

test1 = open("test1.txt", "r")
fullTest1 = int(test1.readline())
test = test1.readline()
while test != "":
    testScore = test.split("|")
    students[testScore[0]].set_test1(testScore[1])
    test = test1.readline()
test1.close()

test2 = open("test2.txt", "r")
fullTest2 = int(test2.readline())
test = test2.readline()
while test != "":
    testScore = test.split("|")
    students[testScore[0]].set_test2(testScore[1])
    test = test2.readline()
test2.close()

# for studentGrade in students.values():
#     print ("student ID:", studentGrade.id, ",student name:", studentGrade.firstName+" "+studentGrade.lastName,\
#     ", student a1:", studentGrade.a1);

