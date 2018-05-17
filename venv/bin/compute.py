a1Percentage = 7.5
a2Percentage = 7.5
projectPercentage = 25
t1Percentage = 30
t2Percentage = 30


class FailGrade:
    def __init__(self):
        self.failGrade = 50

    def set_failGrade(self, grade):
        self.failGrade = grade


fail = FailGrade()


def convertUnitermToFinal(fullPoint, score, item):
    fullPoint = int(fullPoint)
    if score != "":
        score = float(score)
    else:
        score = 0
    switcher = {
        "a1": score / fullPoint * a1Percentage,
        "a2": score / fullPoint * a2Percentage,
        "project": score / fullPoint * projectPercentage,
        "t1": score / fullPoint * t1Percentage,
        "t2": score / fullPoint * t2Percentage,
    }
    return switcher.get(item, 0)


def letterGrade(score):
    score = float(score)
    switcher = {
        "A+": fail.failGrade + 6 * ((100 - fail.failGrade) / 7),
        "A": fail.failGrade + 5 * ((100 - fail.failGrade) / 7),
        "A-": fail.failGrade + 4 * ((100 - fail.failGrade) / 7),
        "B+": fail.failGrade + 3 * ((100 - fail.failGrade) / 7),
        "B": fail.failGrade + 2 * ((100 - fail.failGrade) / 7),
        "B-": fail.failGrade + ((100 - fail.failGrade) / 7),
        "C": fail.failGrade,
    }
    if score > switcher["A+"]:
        return "A+"
    elif score > switcher["A"]:
        return "A"
    elif score > switcher["A-"]:
        return "A-"
    elif score > switcher["B+"]:
        return "B+"
    elif score > switcher["B"]:
        return "B"
    elif score > switcher["B-"]:
        return "B-"
    elif score > switcher["C"]:
        return "C"
    else:
        return "F"


def by_name(t):
    return t.lastName.lower()


def by_score(t):
    return float(t.GR)


def by_id(t):
    return int(t.id)


def sort_based_on_name(list):
    return sorted(list, key=by_name)


def sort_based_on_score(list):
    return sorted(list, key=by_score, reverse=1)


def sort_based_on_id(list):
    return sorted(list, key=by_id)


def change_fail_grade(grade):
    fail.set_failGrade(grade)


def add_GR(students, fullPoint):
    for student in students:
        a1 = convertUnitermToFinal(fullPoint.A1, student.a1, "a1")
        a2 = convertUnitermToFinal(fullPoint.A2, student.a2, "a2")
        project = convertUnitermToFinal(fullPoint.PR, student.project, "project")
        t1 = convertUnitermToFinal(fullPoint.T1, student.test1, "t1")
        t2 = convertUnitermToFinal(fullPoint.T2, student.test2, "t2")
        student.set_GR(round(a1 + a2 + project + t1 + t2, 2))


def add_FL(students):
    for student in students:
        FL = letterGrade(student.GR)
        student.set_FL(FL)


def process_option(option, students, fullPoint):
    if option == "1":
        process_option1(students, fullPoint)
    elif option == "2":
        print(process_option2(students, fullPoint))
    elif option == "3":
        process_option3(students)
    elif option == "4":
        process_option4(students)
    elif option == "5":
        process_option5(students)
    else:
        print("GoodBye")
    if option == "6":
        return 0
    else:
        return 1


def process_option1(students, fullPoint):
    option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
    option = option.lower()
    while 1:
        if option == "a1":
            print("A1 grades (" + str(fullPoint.A1) + ")")
            for student in students:
                t = '{0:<5} {1:<14} {2}'.format(student.id, student.lastName + ", " + student.firstName, student.a1)
                print(str(t).strip("\n"))
            break
        elif option == "a2":
            print("A2 grades (" + str(fullPoint.A2) + ")")
            for student in students:
                t = '{0:<5} {1:<14} {2}'.format(student.id, student.lastName + ", " + student.firstName, student.a2)
                print(str(t).strip("\n"))
            break
        elif option == "pr":
            print("PR grades (" + str(fullPoint.PR) + ")")
            for student in students:
                t = '{0:<5} {1:<14} {2}'.format(student.id, student.lastName + ", " + student.firstName,
                                                student.project)
                print(str(t).strip("\n"))
            break
        elif option == "t1":
            print("T1 grades (" + str(fullPoint.T1) + ")")
            for student in students:
                t = '{0:<5} {1:<14} {2}'.format(student.id, student.lastName + ", " + student.firstName, student.test1)
                print(str(t).strip("\n"))
            break
        elif option == "t2":
            print("T2 grades (" + str(fullPoint.T2) + ")")
            for student in students:
                t = '{0:<5} {1:<14} {2}'.format(student.id, student.lastName + ", " + student.firstName, student.test2)
                print(str(t).strip("\n"))
            break
        else:
            print("Your input is error. Please input again.")
            option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
            option = option.lower()


def process_option2(students, fullPoint):
    option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
    option = option.lower()
    while 1:
        if option == "a1":
            sum = 0
            num = 0
            for student in students:
                if student.a1 != "":
                    sum += float(student.a1)
                    num += 1
            average = sum / num
            aver = "A1 average:" + str(round(average, 2)) + "/" + str(fullPoint.A1)
            return aver
        elif option == "a2":
            sum = 0
            num = 0
            for student in students:
                if student.a2 != "":
                    sum += float(student.a2)
                    num += 1
            average = sum / num
            aver = "A2 average:" + str(round(average, 2)) + "/" + str(fullPoint.A2)
            return aver
        elif option == "pr":
            sum = 0
            num = 0
            for student in students:
                if student.project != "":
                    sum += float(student.project)
                    num += 1
            average = sum / num
            aver = "PR average:" + str(round(average, 2)) + "/" + str(fullPoint.PR)
            return aver
        elif option == "t1":
            sum = 0
            num = 0
            for student in students:
                if student.test1 != "":
                    sum += float(student.test1)
                    num += 1
            average = sum / num
            aver = "T1 average:" + str(round(average, 2)) + "/" + str(fullPoint.T1)
            return aver
        elif option == "t2":
            sum = 0
            num = 0
            for student in students:
                if student.test2 != "":
                    sum += float(student.test2)
                    num += 1
            average = sum / num
            aver = "T2 average:" + str(round(average, 2)) + "/" + str(fullPoint.T2)
            return aver
        else:
            print("Your input is error. Please input again.")
            option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
            option = option.lower()


def process_option3(students):
    print("ID".ljust(6, " "), "LN".ljust(6, " "), "FN".ljust(6, " "), "A1".ljust(6, " "), "A2".ljust(6, " "),
          "PR".ljust(6, " "), "T1".ljust(6, " "), "T2".ljust(6, " "), "GR".ljust(6, " "), "FL".ljust(6, " "))
    for student in students:
        print(student.id.ljust(6, " "), student.lastName.ljust(6, " "), student.firstName.ljust(6, " "),
              student.a1.ljust(6, " "), student.a2.ljust(6, " "), student.project.ljust(6, " "),
              student.test1.ljust(6, " "), student.test2.ljust(6, " "), str(student.GR).ljust(6, " "),
              student.FL.ljust(6, " "))


def process_option4(students):
    option = input("Please select sort orders(LT/GR):")
    option = option.lower()
    while 1:
        if option == "lt":
            return process_option3(sort_based_on_name(students))
        elif option == "gr":
            return process_option3(sort_based_on_score(students))
        else:
            print("Your input is error. Please input again.")
            option = input("Please select sort orders(LT/GR):")
            option = option.lower()


def process_option5(students):
    fail = input("Please input the Pass/Fail point:")
    change_fail_grade(int(fail))
    add_FL(students)
    change_fail_grade(50)
    return process_option3(students)
