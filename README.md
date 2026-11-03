# basic-python-console-based-system

**Class Standing Monitoring System**
# A console program written in Python that lets faculty record quiz and module scores for students and lets students view their scores and estimated class standing, per subject.

# **Features:**

**Faculty (admin)**

Log in with a username and password (2 attempts allowed)
Record quiz scores for a student in a chosen subject
Record module scores for a student in a chosen subject
View a student's estimated class standing grade

 **Student**

Select their student ID
View quiz scores per subject
View module scores per subject
View their estimated class standing grade per subject

**General**

Invalid choices only print "Invalid Choice" and ask again, without reprinting the menu
Every student and subject list has a 0. Back option
Score entries are validated: they must be whole numbers, the score cannot be higher than the overall score, and the overall score cannot be zero



# **Requirements**
Python 3.6 or newer
No extra libraries needed



# **How to use**

Default Faculty login credentials:
| Username | Password |
|----------|----------|
| `admin`  | `123`    |

## Students and subjects

| # | Student ID       | Subject Code |
|---|------------------|--------------|
| 1 | 02-2627-009431   | GEN 001      |
| 2 | 02-2627-013346   | GEN 002      |
| 3 | 02-2627-009850   | GEN 006      |
| 4 | 02-2627-009329   | MAT 152      |
| 5 | 02-2627-009145   | PED 030      |

**The two lists are independent: any student can have scores in any subject.**



1.Run the program. The main menu shows Faculty Login, Student Login, and Exit.

2.Faculty: log in, then choose to record quizzes, record modules, or view a class standing.
-Pick a student, then a subject.
-When recording, type each score and its overall score (for example 8 then 10 for 8/10). Type B at the score prompt when you are finished.

3.Student: pick your student ID, then choose to view quizzes, modules, or class standing. You pick a subject each time.

4.Choose Logout or Exit from a menu to go back.


# How the class standing is computed

quiz %    = total quiz points earned   / total quiz points possible   x 100
module %  = total module points earned / total module points possible x 100

standing  = (quiz % x 0.30) + (module % x 0.30)
class standing grade = standing / 60 x 100

## Project Structure (Single File)

All data is kept in memory using Python lists:

- `subjects`, `student_id`
- `quiz_earned`, `quiz_overall`, `quiz_list`
- `module_earned`, `module_overall`, `module_list`
- Each list is indexed as `[student][subject]`

No external libraries or database are required, only the Python standard library.




# **Limitations**
1.Scores are kept in memory only, so they are lost when the program closes.

2.The faculty username and password are written in the code.

3.The lists of five students and five subjects are fixed in the code.






