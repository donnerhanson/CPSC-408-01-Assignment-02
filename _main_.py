# Python 2.7
# Donner Hanson
# March 14 2020
# CPSC 408-01

from sqlite3.dbapi2 import Cursor

from pandas import DataFrame

from DataBase import DataBase
from Student import Student
from inputParseFuncs import *
from Messages import *


def printSelection(table_contents):
    df = DataFrame(table_contents,
                   columns=['Student Id', 'First Name', 'Last Name', 'GPA', 'Major', 'Faculty Advisor'])
    print(df)


# swap below to use own database name
dbname = 'StudentDB2'
# dbname = getStringIn("enter database name in local folder")

db = DataBase(dbname)
c = db.cursor
conn = db.conn
isRunning = True

while isRunning:
    userChoice = getUserNumInt(main_output_message)
    input_param = ('0',)
    if userChoice == 1:
        selection = c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM '
                              'Student WHERE  isDeleted = ?', input_param)  # type: Cursor
        printSelection(selection)

    elif userChoice == 2:  # create new student
        fname = getStringIn(first_name_prompt)
        lname = getStringIn(second_name_prompt)
        stud_GPA = getUserNumFloat(GPA_prompt)
        stud_major = getStringIn(major_prompt)
        facAdv = getStringIn(faculty_advisor_prompt)

        # Insert a row of data
        # (?,?) cleanses input to avoid SQL injection
        stu = Student(fname, lname, stud_GPA, stud_major, facAdv, 0)
        c.execute("INSERT INTO Student "
                  "('FirstName', 'LastName', 'GPA', "
                  "'Major', 'FacultyAdvisor', 'isDeleted') "
                  "VALUES (?,?,?,?,?,?)", (stu.getFirstname(),
                                           stu.getLastName(),
                                           stu.getGPA(),
                                           stu.getMajor(), stu.getFacultyAdvisor(),
                                           stu.getIsDeleted(),))
        conn.commit()

    elif userChoice == 3:  # Update student
        studID = getUserNumInt(stud_id_prompt)
        userChoice = getUserNumInt(update_attribute_prompt)
        if userChoice == 1:  # major
            stud_major = getStringIn(major_prompt)
            c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (stud_major, studID,))
        elif userChoice == 2:  # fac
            facAdv = getStringIn(faculty_advisor_prompt)
            c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (facAdv, studID,))
        if 1 <= userChoice <= 2:
            conn.commit()

    elif userChoice == 4:  # Delete student
        studID = getUserNumInt(stud_id_prompt)
        input_param = (0, studID,)
        deleted = 1
        selection = c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM '
                              'Student WHERE  isDeleted = ? AND StudentId = ?', input_param,)  # type: Cursor
        # confirm deletion
        print(delete_confirmation)
        printSelection(selection)
        confirm = " "
        while confirm.lower() != "y" and confirm.lower() != "n":
            confirm = getStringIn(y_n)
        if confirm.lower() == 'y':
            c.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (deleted, studID,))
        conn.commit()

    elif userChoice == 5:  # Search by Maj GPA Adv
        userChoice = getUserNumInt(search_attribute_prompt)
        if userChoice == 1:  # maj
            stud_major = getStringIn(major_prompt)
            input_param = ('0', stud_major)

            selection = c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM '
                                  'Student WHERE  isDeleted = ? AND Major = ?', input_param,)
        elif userChoice == 2:  # gpa
            stud_GPA = getUserNumFloat(GPA_prompt)
            input_param = ('0', stud_GPA)
            selection = c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM '
                                  'Student WHERE  isDeleted = ? AND GPA = ?', input_param,)
        elif userChoice == 3:  # search by advisor
            facAdv = getStringIn(faculty_advisor_prompt)
            input_param = ('0', facAdv)
            selection = c.execute('SELECT StudentId, FirstName, LastName, GPA, Major, FacultyAdvisor FROM '
                                  'Student WHERE  isDeleted = ? AND FacultyAdvisor = ?', input_param,)
        if 1 <= userChoice <= 3:
            printSelection(selection)
    elif userChoice == 0:
        isRunning = False
