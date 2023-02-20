class Student:
    def __init__(self,name,usn,branch):
        self.name = name
        self.usn = usn
        self.branch = branch

    def update_branch(self, new_branch):
        self.branch = new_branch

    def display_details(self):
        print("Student name:",self.name)
        print("usn:",self.usn)
        print("Branch:",self.branch)

Student_db = [
    Student("umesh bharude","007","mech"),
    Student("ganeh bharude","009","cs"),
    Student("anusaya bharude","006","it")
]

search_queary = input("Enter your search queary for the student name:")
data = [x for x in student_data if x.name.count(input1)>=1]
if data:
    data[0].display_details()
else:
    print("No data")