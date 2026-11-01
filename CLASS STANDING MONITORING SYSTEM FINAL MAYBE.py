subjects = ["GEN 001", "GEN 002", "GEN 006", "MAT 152", "PED 030"]
student_id = ["02-2627-009431", "02-2627-013346", "02-2627-009850", "02-2627-009329", "02-2627-009145"]


quiz_earned    = [[0] * 5 for _ in range(5)]
quiz_overall   = [[0] * 5 for _ in range(5)]
module_earned  = [[0] * 5 for _ in range(5)]
module_overall = [[0] * 5 for _ in range(5)]

quiz_list   = [[[] for _ in range(5)] for _ in range(5)]
module_list = [[[] for _ in range(5)] for _ in range(5)]

#=====================================================================================================================
#USED BY BOTH ADMIN AND STUDENT MENUS



def choose_students():
    print("========================================")
    print("Select the Available Student IDs")
    print("========================================")
    for student in range(5):
        print(str(student + 1) + ".", student_id[student])
    print("0. Back")

    choice = input ("Select the Available Choices:")
    while choice not in ("0","1", "2", "3", "4", "5"):
        print("Invalid Choice")
        choice = input ("Select the Available Choices:")
    if choice == "0":
        return None
    return int (choice) - 1


def choose_subjects():
    print("========================================")
    print("Select the Available Subject Choices")
    print("========================================")
    for subject in range(5):
        print(str(subject + 1) + ".", subjects[subject])
    print("0. Back")


    choice = input ("Select the Available Choices:")
    while choice not in ("0","1","2", "3", "4", "5"):
        print("Invalid Choice")
        choice = input ("Select the Available Choices:")
    if choice == "0":
        return None
    return int(choice) - 1


def quiz(scr, sub):
    print("===== QUIZ SCORES =====")
    n = 1
    for item in quiz_list[scr][sub]:
        print("Quiz", n, ":", item)
        n += 1
    print("Quizzes Total:", quiz_earned[scr][sub], "/", quiz_overall[scr][sub])
    print("========================================")


def module(scr, sub):
    print("===== MODULE SCORES =====")
    n = 1
    for item in module_list[scr][sub]:
        print("Module", n, ":", item)
        n += 1
    print("Modules Total:", module_earned[scr][sub], "/", module_overall[scr][sub])
    print("========================================")


def class_standing(scr, sub):
    if quiz_overall[scr][sub] > 0:
        quiz_percent = quiz_earned[scr][sub] / quiz_overall[scr][sub] * 100
    else:
        quiz_percent = 0

    if module_overall[scr][sub] > 0:
        module_percent = module_earned[scr][sub] / module_overall[scr][sub] * 100
    else:
        module_percent = 0

    quiz_score = quiz_percent * 0.30
    module_score = module_percent * 0.30
    standing = quiz_score + module_score
    standing_percent = standing / 60 * 100

    print("===== ESTIMATED CLASS STANDING =====")

    n = 1
    for item in quiz_list[scr][sub]:
        print("Quiz", n, ":", item)
        n += 1
    print("Quizzes Total:", quiz_earned[scr][sub], "/", quiz_overall[scr][sub])
    print("========================================")

    n = 1
    for item in module_list[scr][sub]:
        print("Module", n, ":", item)
        n += 1
    print("Module Total:", module_earned[scr][sub], "/", module_overall[scr][sub])
    print("========================================")

    print("Student's Estimated Class Standing Grade:", round(standing_percent, 2), "%")
    print("========================================")

#================================================================================================================

Arima = True

while Arima:
    print("===== CLASS STANDING MONITORING SYSTEM =====")
    print("1. Faculty Login")
    print("2. Student Login")
    print("3. Exit")

    Kishou = input("Pick the Available Choices:")
    while Kishou not in ("1", "2", "3"):
        print("Invalid Choice")
        Kishou = input("Pick the Available Choices:")

#================================================================================================================
# IF ADMIN PICKS 1:

    if Kishou == "1":
        print("===== FACULTY LOGIN =====")
        logged = False
        tries = 0

        while tries < 2 and not logged:
            username = input("Enter your username:")
            password = input("Enter your password:")

            if username == "admin" and password == "admin123":
                print("========================================")
                logged = True

            else:
                tries += 1
                print("Invalid username or password.")
                print("========================================")

        if not logged:
            print("Too many attempts. Returning to Menu.")

#================================================================================================================
#IF LOGIN IS SUCCESSFUL

        if logged:
            admin_menu = True
            while admin_menu:
                print("Admin Menu:")
                print("1. Record Student Quiz")
                print("2. Record Student Module")
                print("3. View Student Class Standing Grade")
                print("4. Logout")

                admin_choice = input("Pick the Available Choices:")
                while admin_choice not in ("1", "2", "3", "4"):
                    print("Invalid Choice.")
                    admin_choice = input("Pick the Available Choices:")


                if admin_choice == "1":
                    student_index = choose_students()
                    if student_index is None:
                        continue

                    subject_index = choose_subjects()
                    if subject_index is None:
                        continue
                    quiz_number = len(quiz_list[student_index][subject_index]) + 1

                    while True:
                        print("=====", quiz_number, "=====")
                        score = input("Enter the Student's Quiz score (Or type 'B' to Finish):")

                        if score.upper() == "B":
                            break

                        overall = input("Enter the Quiz Overall Score (Or type 'B' to Finish):")

                        if not score.isdigit() or not overall.isdigit():
                            print("Invalid, try again.")
                        elif int(score) > int(overall):
                            print("The score must not be higher than overall score.")
                        elif int(overall) == 0:
                            print("The Overall Score cannot be zero")
                        

                        else:
                            quiz_earned[student_index][subject_index] += int(score)
                            quiz_overall[student_index][subject_index] += int(overall)
                            quiz_list[student_index][subject_index].append(score + "/" + overall)
                            print("Recorded Quiz:", quiz_number, ":", score, "/", overall)
                            quiz_number += 1

                elif admin_choice == "2":
                    student_index = choose_students()
                    if student_index is None:
                        continue

                    subject_index = choose_subjects()
                    if subject_index is None:
                        continue
                    module_number = len(module_list[student_index][subject_index]) + 1

                    while True:
                        print("=====", module_number, "=====")
                        score2 = input("Enter the Student's Module score (Or type 'B' to Finish):")

                        if score2.upper() == "B":
                            break

                        overall2 = input("Enter the Module Overall Score (Or type 'B' to Finish):")

                        if not score2.isdigit() or not overall2.isdigit():
                            print("Invalid, try again.")
                        elif int(score2) > int(overall2):
                            print("The score must not be higher than overall score.")
                        elif int(overall2) == 0:
                            print("The Overall Score cannot be zero")

                        
                        else:
                            module_earned[student_index][subject_index] += int(score2)
                            module_overall[student_index][subject_index] += int(overall2)
                            module_list[student_index][subject_index].append(score2 + "/" + overall2)
                            print("Recorded Module:", module_number, ":", score2, "/", overall2)
                            module_number += 1


                elif admin_choice == "3":
                    student_index = choose_students()
                    if student_index is None:
                        continue

                    subject_index = choose_subjects()
                    if subject_index is None:
                        continue
                    class_standing(student_index, subject_index)
                    

                elif admin_choice == "4":
                    print("Logging out...")
                    admin_menu = False


#================================================================================================================
#STUDENT MENU

    elif Kishou == "2":
        student_index = choose_students()
        if student_index is None:
            continue

        student_menu = True
        while student_menu:
            print("Student Menu:")
            print("1. View Quiz Scores")
            print("2. View Module Scores")
            print("3. View Class Standing Grade")
            print("4. Exit")

            student_choice = input("Pick the Available Choices:")
            while student_choice not in ("1", "2", "3", "4",):
                print("Invalid Choice.")
                student_choice = input("Pick the Available Choices:")   


            if student_choice == "1":
                subject_index = choose_subjects()
                if subject_index is None:
                    continue
                quiz(student_index, subject_index)


            elif student_choice == "2":
                subject_index = choose_subjects()
                if subject_index is None:
                    continue
                module(student_index, subject_index)


            elif student_choice == "3":
                subject_index = choose_subjects()
                if subject_index is None:
                    continue
                class_standing(student_index, subject_index)


            elif student_choice == "4":
                print("Logging out...")
                student_menu = False
         

#================================================================================================================

    elif Kishou == "3":
        print("Terminating the Program...")
        Arima = False


