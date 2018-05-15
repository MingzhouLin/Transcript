# -*- coding: UTF-8 -*-
import compute

class StudentGrade:
    'students grade'

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.a1 = ""
        self.a2 = ""
        self.project = ""
        self.test1 = ""
        self.test2 = ""
        self.GR = ""
        self.FL = ""

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

    def set_GR(self, GR):
        self.GR = GR

    def set_FL(self, FL):
        self.FL = FL


class FullPoint:
    'full point'

    def __init__(self):
        self.A1 = 0
        self.A2 = 0
        self.PR = 0
        self.T1 = 0
        self.T2 = 0

    def set_A1(self, A1):
        self.A1 = A1

    def set_A2(self, A2):
        self.A2 = A2

    def set_PR(self, PR):
        self.PR = PR

    def set_T1(self, T1):
        self.T1 = T1

    def set_T2(self, T2):
        self.T2 = T2


students = {}
fullPoint = FullPoint()

classes = open("class.txt", "r")
student = classes.readline().strip("\n")
while student != "":
    studentAttrs = student.split("|")
    stu = StudentGrade(studentAttrs[0], studentAttrs[1], studentAttrs[2])
    students[studentAttrs[0]] = stu
    student = classes.readline().strip("\n")
classes.close()

a1 = open("a1.txt", "r")
fullPoint.set_A1(int(a1.readline()))
ass1 = a1.readline().strip("\n")
while ass1 != "":
    a1Score = ass1.split("|")
    students[a1Score[0]].set_a1(a1Score[1])
    ass1 = a1.readline().strip("\n")
a1.close()

a2 = open("a2.txt", "r")
fullPoint.set_A2(int(a2.readline()))
ass2 = a2.readline().strip("\n")
while ass2 != "":
    a2Score = ass2.split("|")
    students[a2Score[0]].set_a2(a2Score[1])
    ass2 = a2.readline().strip("\n")
a2.close()

projects = open("project.txt", "r")
fullPoint.set_PR(int(projects.readline()))
project = projects.readline().strip("\n")
while project != "":
    projectScore = project.split("|")
    students[projectScore[0]].set_project(projectScore[1])
    project = projects.readline().strip("\n")
projects.close()

test1 = open("test1.txt", "r")
fullPoint.set_T1(int(test1.readline()))
test = test1.readline().strip("\n")
while test != "":
    testScore = test.split("|")
    students[testScore[0]].set_test1(testScore[1])
    test = test1.readline().strip("\n")
test1.close()

test2 = open("test2.txt", "r")
fullPoint.set_T2(int(test2.readline()))
test = test2.readline().strip("\n")
while test != "":
    testScore = test.split("|")
    students[testScore[0]].set_test2(testScore[1])
    test = test2.readline().strip("\n")
test2.close()

students = compute.sort_based_on_id(students.values())
compute.add_GR(students, fullPoint)
compute.add_FL(students)
print("1> Display individual component")
print("2> Display component average")
print("3> Display Standard Report")
print("4> Sort by alternate column")
print("5> Change Pass/Fail point")
print("6> Exit")
option = input("Please input your option:")
while compute.process_option(str(option), students, fullPoint):
    students = compute.sort_based_on_id(students)
    compute.add_GR(students, fullPoint)
    compute.add_FL(students)
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display Standard Report")
    print("4> Sort by alternate column")
    print("5> Change Pass/Fail point")
    print("6> Exit")
    option = input("Please input your option:")
