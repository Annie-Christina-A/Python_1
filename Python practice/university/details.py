class University:
    def __init__(self,uni_name):
        self.uni=uni_name
    def Show_detail(self):
        print("University Name:",self.uni)
class Course(University):
    def __init__(self, uni_name,course_name):
        super().__init__(uni_name)
        self.course_name=course_name
    def Show_detail(self):
        print("course name:",self.course_name)
class Branch(University):
    def __init__(self, uni_name,branch):
        super().__init__(uni_name)
        self.branch=branch
    def Show_detail(self):
        print("Branch name:",self.branch)
class Student(Course,Branch):
    def __init__(self, branch, course_name,name):
        super().__init__(branch, course_name)
        self.name=name
    def Show_detail(self):
        print("Student name:",self.name)
class Faculty(Branch):
    def __init__(self, uni_name, branch,faculty):
        super().__init__(uni_name, branch)
        self.faculty=faculty
    def Show_detail(self):
        print("Faculty name:",self.course_name)

stud=Student("CSE","Python","Arul")