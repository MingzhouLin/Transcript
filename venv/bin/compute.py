from prettytable import PrettyTable

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
    score = float(score)
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
        student.set_GR(a1 + a2 + project + t1 + t2)


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
        print(process_option3(students))
    elif option == "4":
        print(process_option4(students))
    elif option == "5":
        print(process_option5(students))
    else:
        print("GoodBye")
    if option == "6":
        return 0
    else:
        return 1


def process_option1(students, fullPoint):
    table = PrettyTable()
    option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
    option = option.lower()
    while option == "a1" or option == "a2" or option == "pr" or option == "t1" or option == "t2":
        if option == "a1":
            print("A1 grades (", fullPoint.A1, ")")
            for student in students:
                print(student.id + "\t" + student.lastName + ", " + student.firstName + "\t" + student.a1)
            break
        elif option == "a2":
            table.add_row(["A2 grades (", fullPoint.A2, ")"])
            for student in students:
                table.add_row([student.id, student.lastName + ", " + student.firstName, student.a2])
            return table
        elif option == "pr":
            table.add_row(["PR grades (", fullPoint.PR, ")"])
            for student in students:
                table.add_row([student.id, student.lastName + ", " + student.firstName, student.project])
            return table
        elif option == "t1":
            table.add_row(["T1 grade (", fullPoint.T1, ")"])
            for student in students:
                table.add_row([student.id, student.lastName + ", " + student.firstName, student.test1])
            return table
        elif option == "t2":
            table.add_row(["T2 grade (", fullPoint.T2, ")"])
            for student in students:
                table.add_row([student.id, student.lastName + ", " + student.firstName, student.test2])
            return table
        else:
            print("Your input is error. Please input again.")
            option = raw_input("Please input the component you want to see(A1, A2, PR, T1, T2):")
            option = option.lower()


def process_option2(students, fullPoint):
    option = input("Please input the component you want to see(A1, A2, PR, T1, T2):")
    option = option.lower()
    while option == "a1" or option == "a2" or option == "pr" or option == "t1" or option == "t2":
        if option == "a1":
            sum = 0
            for student in students:
                sum += float(student.a1)
            average = sum / len(students)
            aver = "A1 average:" + str(average) + "/" + str(fullPoint.A1)
            return aver
        elif option == "a2":
            sum = 0
            for student in students:
                sum += float(student.a2)
            average = sum / len(students)
            aver = "A2 average:" + str(average) + "/" + str(fullPoint.A2)
            return aver
        elif option == "pr":
            sum = 0
            for student in students:
                sum += float(student.project)
            average = sum / len(students)
            aver = "PR average:" + str(average) + "/" + str(fullPoint.PR)
            return aver
        elif option == "t1":
            sum = 0
            for student in students:
                sum += float(student.test1)
            average = sum / len(students)
            aver = "T1 average:" + str(average) + "/" + str(fullPoint.T1)
            return aver
        elif option == "t2":
            sum = 0
            for student in students:
                sum += float(student.test2)
            average = sum / len(students)
            aver = "T2 average:" + str(average) + "/" + str(fullPoint.T2)
            return aver
        else:
            print("Your input is error. Please input again.")
            option = raw_input("Please input the component you want to see(A1, A2, PR, T1, T2):")
            option = option.lower()


def process_option3(students):
    table = PrettyTable(["ID", "LN", "FN", "A1", "A2", "PR", "T1", "T2", "GR", "FL"]);
    for student in students:
        table.add_row(
            [student.id, student.lastName, student.firstName, student.a1, student.a2, student.project, student.test1,
             student.test2, student.GR, student.FL])
    return table


def process_option4(students):
    option = input("Please select sort orders(LT/GR):")
    option = option.lower()
    while option == "lt" or option == "gr":
        if option == "lt":
            return process_option3(sort_based_on_name(students))
        elif option == "gr":
            return process_option3(sort_based_on_score(students))
        else:
            print("Your input is error. Please input again.")
            option = raw_input("Please select sort orders(LT/GR):")
            option = option.lower()


def process_option5(students):
    fail = input("Please input the Pass/Fail point:")
    change_fail_grade(int(fail))
    add_FL(students)
    change_fail_grade(50)
    return process_option3(students)
