class Student:
    def __init__(self, first_name, last_name, GPA, major, FacultyAdvisor, isDeleted):
        self.first_name = first_name
        self.last_name = last_name
        self.GPA = GPA
        self.major = major
        self.FacultyAdvisor = FacultyAdvisor
        self.isDeleted = isDeleted

    def getFirstname(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getGPA(self):
        return self.GPA

    def getMajor(self):
        return self.major

    def getFacultyAdvisor(self):
        return self.FacultyAdvisor

    def getIsDeleted(self):
        return self.isDeleted

    # return tuple of student
    def getStudent(self):
        return (self.getFirstname(), self.getLastName(), self.getGPA(), self.getMajor(), self.getFacultyAdvisor(),
                self.getIsDeleted())
